# Scene Scorer: The Matrix

**Directory:** `custom-scene-scorer-matrix/`

## What it does
A student-driven film-scoring tool built on the Custom Scene Scorer template. A fixed Matrix clip is preloaded and plays with its own audio (sound effects, no music). The student pastes any YouTube link as a music bed, balances scene audio against music with two faders, and can copy a locked share link that reproduces their exact version as a watch-only example.

## Live URL
https://numberdave-cloud.github.io/MPMPT1/custom-scene-scorer-matrix/

## Canvas embed
```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/custom-scene-scorer-matrix/"
  width="100%"
  height="860"
  style="border: none;"
  title="Scene Scorer: The Matrix"
  allow="autoplay; clipboard-write"
  loading="lazy">
</iframe>
```
Height is 860 (up from the original Custom Scene Scorer's 820) because a second fader row was added: Scene Level sits above Music Level. `clipboard-write` is required in `allow` for the Copy Link button to write to the clipboard cleanly inside the Canvas iframe. Confirm the height against the live Canvas column and adjust if it clips or leaves slack.

## Build / version state
v1.0. Initial ship, pending live verification of: the Matrix clip embedding at all, the crop framing, whole-clip end detection, dual-volume balance, and the share-link round-trip carrying both volumes.

## How it differs from the base Custom Scene Scorer
- **Scene plays its own audio.** `muted: false`. The scene's sound effects play alongside the added music, so both YouTube players sound at once. The music player still sits full-size behind the opaque scene (kept over 200px and viewport-intersecting) so YouTube does not halt it.
- **Two faders.** SCENE LEVEL (picture audio, default 80) and MUSIC LEVEL (added track, default 70). Both are live volume controls; both are dimmed and non-editable in locked EXAMPLE mode.
- **Whole clip, computed end.** `start: 0`, `end: null`. The out-point is read from the clip's own `getDuration()` on ready (`computeSceneEnd`) and set to `duration - 0.4s`, so playback pauses just before YouTube's natural end and the "More videos" end-screen never lands in frame. `getDuration()` can return 0 before the video buffers, so the end-poll retries the duration read until a real value appears; the `ENDED` state handler is a fallback.
- **Share link carries both volumes.** `?m=ID&t=START&vol=MUSIC&svol=SCENE`. Opening a link with `m` present is locked EXAMPLE mode as before.
- **No audio blip on load.** The scene is muted for the load-time seek to its first frame, then `play()` unmutes and applies the scene level. A paused player is silent, so pause/stop need no re-mute.

## How it works (shared with the template)
- **Scene:** fixed in the CONFIG block at the top of the script. Currently video `m8J7vtr2qIM`, whole clip, own audio. Travels with the device; the student cannot change it.
- **Music:** one slot. Student pastes a link, the parser pulls the video ID plus any start timestamp (`?t=`, `&start=`, seconds or `1m23s` form; handles `youtu.be`, `watch?v=`, `embed`, `shorts`, bare IDs). The pasted timestamp is the music's in-point, aligned to the scene's first frame.
- **Share:** COPY LINK is held disabled until a pasted track is verified (see the error-150 grace window). Locked example mode shows scene plus the student's bed at their two levels, dimmed non-editable faders, an EXAMPLE badge, no editing controls. State rides entirely in the URL, no backend. The copied link is the github.io URL even when embedded in Canvas, so shared examples open standalone.

## Technical notes
- Crop knobs at the top of the `.video-wrap` rule: `--frame-aspect` (window shape, 1.778 = full 16:9, higher = wider) and `--scene-zoom` (enlarge to push YouTube's top/bottom bars out and pull the sides in, 1.0 = none). Currently 2.15 / 1.18, carried over from the previous scene and NOT yet tuned to the Matrix clip. Retune by eye against the live embed; a letterboxed scope upload may need different values to avoid black bands or clipped heads. `--scene-shift` is an optional vertical nudge.
- Music player is built once and reused via `cueVideoById`, never destroyed and recreated (rebuilding made YouTube throw a false error 150 on embeddable videos).
- Phantom error 150 on video swaps is absorbed by an 1800 ms grace window: a 150/101 shows a neutral "Loading track..." and only surfaces the real "embedding switched off" message if the player is still dead at the deadline. Codes 100 (private) and 2 (bad link) fail instantly. Copy Link stays disabled during the window.
- All players pass `origin: window.location.origin` in playerVars to give YouTube a stable embedder identity (the 2025 identity check otherwise falls back to a flaky Referer and throws false 150s). The `<meta name="referrer">` is a second layer.
- Scene controls hidden (`controls: 0`); the device transport is the only way to drive playback. A transparent click-shield over the scene routes clicks to the device's own play/pause so the bed is never orphaned. Captions unloaded on first PLAY.
- Page background transparent so the rounded rack card floats on the Canvas page.
- Embeddability is not guaranteed for pasted or shared tracks. Audio-only, lyric, and "Artist - Topic" uploads embed most reliably; official/Vevo videos often refuse.

## Open decisions / TODOs
- **Verify the Matrix clip `m8J7vtr2qIM` embeds.** If the owner has embedding off, swap to a different upload of the same scene.
- **Tune the crop** (`--frame-aspect` / `--scene-zoom`) against the live embed.
- Confirm embed height 860 in the real Canvas column.
- Live-verify: whole-clip end detection pauses cleanly before the end-screen, dual-volume balance behaves, and a copied link opened fresh rebuilds both volumes exactly.

## Last updated
2026-09-22 - v1.0 initial ship. Built from the Custom Scene Scorer template with an unmuted scene, a second SCENE LEVEL fader, whole-clip end computed from the clip's own duration, and both volumes encoded in the share link. Fader qualifier text removed before ship at Dave's request.
