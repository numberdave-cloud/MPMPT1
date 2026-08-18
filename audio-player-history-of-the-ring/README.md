# Audio Player [History of the Ring]

Directory: `audio-player-history-of-the-ring/`

Audio-only player for a fixed YouTube track. Fades in from silence at the top,
holds at full, then fades out and stops. No video, no scrubbing. Sits at the
top of a page as a musical bed the student presses play and reads under.

## Live URL
https://numberdave-cloud.github.io/MPMPT1/audio-player-history-of-the-ring/

## Canvas embed
Height is 190, not the 600 default. This is a slim single-row player. Content
is about 169px on desktop and about 184px on narrow mobile, where the longer
title line wraps to two lines. 190 clears the tallest case without clipping the
volume fader.

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/audio-player-history-of-the-ring/"
  width="100%"
  height="190"
  title="History of the Ring audio player"
  style="border: none;"
  allow="autoplay"
  loading="lazy"></iframe>
```

## Build state
v1.0. Built on the original fade-out audio-player template (Under the Skin)
with a fade-in added on the front. Not yet verified playing inside a live
Canvas iframe.

## What it plays
The History of the Ring leitmotif from The Lord of the Rings. Howard Shore.
YouTube ID `GuiROE85RMQ`.

## Fade shape
- Enters silent at 0:23, eases up to full level by 0:28 on a raised-cosine
  S-curve (gentle out of silence, no bump onto full).
- Holds at full from 0:28 to 1:34.
- Fades out from 1:34 to silence at 1:42, then pauses and offers replay.
- Config constants at the top of the script: `START_AT` (23 = 0:23),
  `FADE_IN_END` (28), `FADE_OUT_START` (94 = 1:34), `FADE_OUT_DURATION` (8).
  `SCALE` is `FADE_OUT_START + FADE_OUT_DURATION` (102).
- Progress bar and time readout run from `START_AT`, so they read 0:00 when
  playback begins and fill to 100% at 1:42 (span 79s).
- The fade-in is eased (raised cosine), not linear, so it does not sound abrupt
  leaving silence. The fade-out is still linear. Playback seeks to `START_AT` on
  first play and on replay.

## Technical notes
- Audio comes from the YouTube IFrame API, not embedded base64. The IFrame API
  builds a 640x360 player, so its wrapper is a 1px absolutely positioned box
  with `overflow:hidden` that clips the player out of sight. It is rendered
  rather than set to `display:none`, which would stop playback.
- The fade is automation, not a real audio tap. Web Audio cannot read a
  cross-origin YouTube stream, so the fade polls `getCurrentTime` and calls
  `setVolume` on an 80ms ticker. `fadeFactor` eases up across `START_AT` to
  `FADE_IN_END` on a raised-cosine curve, holds at 1, then ramps down linearly
  across `FADE_OUT_START` to `SCALE`.
- The `fading` glow on the progress bar is active during both fade windows.
- Progress bar and time readout run 0 to `SCALE` (102s). At `SCALE` the ENDED
  path is not needed; the ticker calls `finish` when currentTime passes `SCALE`,
  which pauses the source (`STOP_AFTER_FADE`) and sets the replay control.
- Volume fader is a custom control: drag the handle, scroll over it, or use
  arrow keys (Home/End jump to 0/100). Clicking the track does not jump the
  value. It initialises at 70%. The fade-in target is this fader level, so a
  ramp runs 0 to 70 by default.
- `html` and `body` are locked to 100% height with `overflow:hidden`, so page
  content can never exceed the iframe. Keep the embed height at or above 185 so
  nothing clips on mobile.
- iOS Safari needs the play tap as its audio gesture; the play button handler
  calls `playVideo` directly to satisfy that.

## Open decisions / TODOs
- Playback and both fade curves not yet verified in a live Canvas iframe.
- Fade-in eased with a raised-cosine curve. If a faster arrival or a slower
  onset is wanted, change the curve in `fadeFactor`.
- Fade-out duration set to 8s (1:34 to 1:42) and still linear. Adjust or ease it
  if wanted.
- Default fader level is 70%. Raise the default if a louder level is wanted.

## Last updated
17 August 2026 (v1.1). Corrected entry point to 0:23 with an eased 5s fade-in to
70% by 0:28. Fade-out unchanged (1:34 to 1:42, stop).
