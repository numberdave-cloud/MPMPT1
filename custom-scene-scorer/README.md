# Custom Scene Scorer

**Directory:** `custom-scene-scorer/`

## What it does
A student-driven film-scoring tool. A fixed dialogue scene is preloaded; the student pastes any YouTube link as a music bed, balances it against the dialogue, and can copy a locked share link that reproduces their exact version as a watch-only example.

## Live URL
https://numberdave-cloud.github.io/MPMPT1/custom-scene-scorer/

## Canvas embed
```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/custom-scene-scorer/"
  width="100%"
  height="820"
  style="border: none;"
  title="Custom Scene Scorer"
  allow="autoplay; clipboard-write"
  loading="lazy">
</iframe>
```
Height is 820 (taller than the curated Scene Scorer's 640) because the paste box, level fader, and Copy Link controls stack under the video. `clipboard-write` is required in `allow` for the Copy Link button to write to the clipboard cleanly inside the Canvas iframe. Confirm the height against the live Canvas column and adjust if it clips or leaves slack.

## Build / version state
Initial production ship. Pending live verification of scene start/end trimming, embed failure handling, and share-link round-trip.

## How it works
- **Scene:** fixed in the CONFIG block at the top of the script. Currently video `L_Cb1OepkY8`, trimmed to `start: 37` and `end: 130` seconds (0:37 to 2:10), and `muted: true` so the scene's own audio is silent. The scene travels with the device and cannot be changed by the student. Only the added music is heard.
- **Music:** one slot. Student pastes a link, the parser pulls the video ID plus any start timestamp (`?t=`, `&start=`, seconds or `1m23s` form; also handles `youtu.be`, `watch?v=`, `embed`, `shorts`, and bare IDs). The pasted timestamp becomes the music's in-point, aligned to the scene's first frame (0:37).
- **Level:** a single MUSIC LEVEL fader sets the music volume (0 to 100). Default 70. Since the scene is muted, this is a straight music-level control.
- **Share:** COPY LINK builds `?m=ID&t=START&vol=LEVEL`. Opening a link with `m` present puts the device in locked example mode: scene plus the student's bed, their in-point, their level shown as a dimmed non-editable fader, an EXAMPLE badge, no editing controls. State rides entirely in the URL, no backend. The copied link is the github.io URL even when the tool runs embedded in Canvas, so shared examples open standalone.

## Technical notes
- Scene start/end: `start` playerVar plus a 200 ms `getCurrentTime()` poll that pauses both players and resets to the start point at `end` (130 s). The scene's own `end` playerVar is deliberately NOT set, so YouTube never reaches its natural-end state and never shows the "More videos" end-screen overlay; the poll pauses on a mid-video frame instead.
- Music player is built once (on first load) and reused via `cueVideoById`, matching the curated device. It is NOT destroyed and recreated: tearing the player down and rebuilding it made YouTube reject even embeddable videos with a false error 150.
- Chrome crop: the video window is a cropped strip of the full 16:9 players. YouTube's top title/channel bar and bottom "More videos" bar sit at the player edges, so the players are enlarged and the window clipped to a shorter, slightly narrower shape to push that chrome out of frame. Both scene and music players are cropped identically via the same `.video-wrap` transform; the music player stays a large, viewport-intersecting element (visible strip well over 200px), so the sole-audio halt does not return. Two knobs at the top of the `.video-wrap` rule: `--frame-aspect` (window shape, 1.778 = full 16:9, higher = wider) and `--scene-zoom` (enlarge to push the bars out and pull the sides in, 1.0 = none). Defaults 2.0 and 1.18, tuned by eye against the live embed; `--scene-shift` is an optional vertical nudge. The centre play button is intentionally left visible. Not currently using an opaque paused-state cover (as Energy Dial does); add one only if title chrome bleeds in on pause and the zoom cannot kill it.
- Load resets both players: `handleLoad` calls `stopToTop()` before `loadMusic`, so pressing LOAD immediately pauses and rewinds both scene and music to their start points. The new bed cues paused at its in-point via `cueVideoById`, and PLAY starts scene and music together from the top. Prevents the old take rolling on under a newly loaded track.
- Music error handling reports the YT error code distinctly: 101/150 embedding disabled, 100 private/removed, 2 bad link, else generic. Messages are student-facing and pending final wording approval.
- Phantom error 150 on video swaps is now absorbed by a grace window. YouTube fires a false error 150 DURING a `cueVideoById` swap, then cues and plays the video fine a fraction of a second later. Isolated on a bare repro bench: 150 at +114 ms, CUED at +159 ms, then PLAYING; the video always recovered. The old handler reacted to the phantom by nulling the track and calling `stopVideo()`, which killed a load that was about to succeed, so the student saw a false "embedding switched off" message on genuinely embeddable tracks. Now a 150/101 opens an 1800 ms grace window and shows a neutral "Loading track..." rather than tearing down: if the player reaches a healthy state (CUED/PLAYING/BUFFERING/PAUSED) within the window, caught in `onMusicStateChange` or by the deadline poll in `pending150Expired`, the 150 is treated as false and playback continues. Only if the player is still dead at the deadline does the real "embedding switched off" error surface, delayed by 1.8 s and unnoticeable. Codes 100 (private) and 2 (bad link) remain instant hard failures. Copy Link is held disabled during the window so an unverified track cannot be shared. `pending150` is cleared at the top of `loadMusic` so a stale timer cannot fail a fresh load.
- Root cause note: the false 150 is specific to swapping video inside a live player via `cueVideoById`. A fresh player create (first load) never throws it. This device is the only MOTE that changes the video in an existing player at runtime, which is why the symptom appeared here and not in the curated Scene Scorer or Batman Across the Decades (fixed-videoId players).
- All players pass `origin: window.location.origin` in playerVars. YouTube's embedder-identity check (tightened mid-2025) otherwise falls back to the HTTP Referer, which is sent intermittently and produces flaky, false error 150s ("works after a few reloads"). The explicit origin gives YouTube a stable identity. The `<meta name="referrer" content="strict-origin-when-cross-origin">` remains as a second layer.
- The scene player has an `onError` that logs the code to the console (it shows no user-facing message), so a silent scene failure is diagnosable.
- Captions are unloaded on first PLAY (`unloadModule('captions'`/`'cc'`)) and `cc_load_policy: 0` is set.
- A transparent click-shield sits over the scene so YouTube never receives clicks; a click on the video runs the device's own play/pause instead, which keeps the bed from being orphaned.
- Scene controls hidden (`controls: 0`), so the device transport is the only way to drive playback.
- Music player runs full-size directly behind the scene player (z-index 1 vs 2), hidden from view by the opaque scene on top. YouTube halts playback on a player under 200x200 or not genuinely visible; with the scene muted the music is the only audio source, so it must be a compliant, in-viewport player. An earlier build hid the music player in a 200x120 near-zero-opacity box and YouTube stopped it after a few seconds with error 150.
- Page background is transparent so the rounded rack card floats on the Canvas page. The card itself keeps the dark fill.
- Embeddability is not guaranteed for pasted or shared tracks. If a link has embedding disabled, is private, or is region-locked, the player fires an error and the device shows a "won't play here" message. Audio-only, lyric, and "Artist - Topic" uploads embed most reliably; official/Vevo videos often refuse.

## Open decisions / TODOs
- Confirm embed height 820 in the real Canvas column.
- Live-verify: scene trims to 0:37 to 2:10, awkward pasted links behave, embed-failure message fires, and a copied link opened fresh rebuilds the example exactly.
- Optional: retrofit the rounded rack-card treatment onto the curated `scene-scorer` device so the pair match (separate reviewed change, that one is live in Canvas).

## Last updated
2026-08-12 (later still) - Cropped YouTube chrome out of the scene window (tunable `--frame-aspect` / `--scene-zoom` on `.video-wrap`, defaults 2.0 / 1.18, to be dialled in against the live embed) and made LOAD hard-stop and rewind both players so a new bed always starts from the top, paused. Earlier same day: fixed the false error 150 on pasted-track swaps with an 1800 ms grace window; added explicit `origin` playerVar; scene onError logging; reverted destroy/recreate; no-end-screen; muted scene; code-specific errors; initial ship.
