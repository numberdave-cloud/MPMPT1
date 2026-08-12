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
- Scene start/end handled two ways for robustness: `start`/`end` playerVars on the scene player, plus a 200 ms `getCurrentTime()` poll that pauses both players and resets to the start point when the scene reaches its end. The poll keeps scene and music stopping together at the tail.
- YouTube IFrame API drives all playback. `<meta name="referrer" content="strict-origin-when-cross-origin">` is set to satisfy YouTube's embedder-identity check (avoids error 153 on a proper origin; note that `file://` and sandboxed previews will still throw 153, so test on the live URL or a localhost server).
- Captions are unloaded on first PLAY (`unloadModule('captions'`/`'cc'`)) and `cc_load_policy: 0` is set.
- A transparent click-shield sits over the scene so YouTube never receives clicks; a click on the video runs the device's own play/pause instead, which keeps the bed from being orphaned.
- Scene controls hidden (`controls: 0`), so the device transport is the only way to drive playback.
- Music player runs hidden and audio-only, positioned in-viewport at near-zero opacity rather than `display:none` to avoid browser throttling.
- Page background is transparent so the rounded rack card floats on the Canvas page. The card itself keeps the dark fill.
- Embeddability is not guaranteed for pasted or shared tracks. If a link has embedding disabled, is private, or is region-locked, the player fires an error and the device shows a "won't play here" message. Audio-only, lyric, and "Artist - Topic" uploads embed most reliably; official/Vevo videos often refuse.

## Open decisions / TODOs
- Confirm embed height 820 in the real Canvas column.
- Live-verify: scene trims to 0:37 to 2:10, awkward pasted links behave, embed-failure message fires, and a copied link opened fresh rebuilds the example exactly.
- Optional: retrofit the rounded rack-card treatment onto the curated `scene-scorer` device so the pair match (separate reviewed change, that one is live in Canvas).

## Last updated
2026-08-12 - Muted the scene's own audio (`muted: true`) so only the added music plays. Also on initial ship: new scene (L_Cb1OepkY8, 0:37 to 2:10), single paste-your-own music slot, level fader, locked share links, rack-card container on a transparent surround.
