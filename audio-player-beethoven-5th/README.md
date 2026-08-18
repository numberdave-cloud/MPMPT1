# Audio Player [Beethoven 5th]

Directory: `audio-player-beethoven-5th/`

Audio-only player for a fixed YouTube track. Enters partway in, fades in from
silence, holds at full, then fades out and stops. No video, no scrubbing. Sits
at the top of a page as a musical bed the student presses play and reads under.

## Live URL
https://numberdave-cloud.github.io/MPMPT1/audio-player-beethoven-5th/

## Canvas embed
Height is 190, not the 600 default. This is a slim single-row player. Content
is about 169px on desktop and about 184px on narrow mobile, where the title
line wraps to two lines. 190 clears the tallest case without clipping the
volume fader.

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/audio-player-beethoven-5th/"
  width="100%"
  height="190"
  title="Beethoven Symphony No. 5 audio player"
  style="border: none;"
  allow="autoplay"
  loading="lazy"></iframe>
```

## Build state
v1.0. Built on the fade-in-plus-fade-out audio-player template (copied from
`audio-player-history-of-the-ring/`, video, title and fade points swapped). Not
yet verified playing inside a live Canvas iframe.

## What it plays
Symphony No. 5 in C minor, Op. 67, first movement (I. Allegro con brio).
Beethoven. YouTube ID `QpYKVzErt-E`.

## Fade shape
- Enters silent at 0:09, eases up to full level by 0:10 (a 1s raised-cosine
  fade-in).
- Holds at full from 0:10 to 0:55.
- Fades out from 0:55 to silence at 1:05, then pauses and offers replay.
- Config constants at the top of the script: `START_AT` (9 = 0:09), `FADE_IN_END`
  (10), `FADE_OUT_START` (55 = 0:55), `FADE_OUT_DURATION` (10). `SCALE` is
  `FADE_OUT_START + FADE_OUT_DURATION` (65).
- Progress bar and time readout run from `START_AT`, so they read 0:00 when
  playback begins and fill to 100% at 1:05 (span 56s).
- The fade-in is eased (raised cosine), not linear. The fade-out is linear.
  Playback seeks to `START_AT` on first play and on replay.

## Technical notes
- Audio comes from the YouTube IFrame API, not embedded base64. The IFrame API
  builds a 640x360 player, so its wrapper is a 1px absolutely positioned box
  with `overflow:hidden` that clips the player out of sight. It is rendered
  rather than set to `display:none`, which would stop playback.
- The fade is automation, not a real audio tap. Web Audio cannot read a
  cross-origin YouTube stream, so the fade polls `getCurrentTime` and calls
  `setVolume` on an 80ms ticker. `fadeFactor` eases up across `START_AT` to
  `FADE_IN_END`, holds at 1, then ramps down linearly across `FADE_OUT_START`
  to `SCALE`.
- The `fading` glow on the progress bar is active during both fade windows.
- The ticker calls `finish` when currentTime passes `SCALE`, which pauses the
  source (`STOP_AFTER_FADE`) and sets the replay control.
- Volume fader is a custom control: drag the handle, scroll over it, or use
  arrow keys (Home/End jump to 0/100). Clicking the track does not jump the
  value. It initialises at 70%. The fade-in target is this fader level.
- `html` and `body` are locked to 100% height with `overflow:hidden`, so page
  content can never exceed the iframe. Keep the embed height at or above 185 so
  nothing clips on mobile.
- iOS Safari needs the play tap as its audio gesture; the play button handler
  calls `playVideo` directly to satisfy that.

## Open decisions / TODOs
- Playback and both fade curves not yet verified in a live Canvas iframe.
- Fade-in eased with a raised-cosine curve over 1s. Swap to linear in
  `fadeFactor` if a dead-linear ramp is wanted.
- Default fader level is 70%. Raise the default if a louder level is wanted.

## Last updated
17 August 2026 (v1.0). Initial ship. Enter at 0:09, 1s eased fade-in to 70% by
0:10, hold, fade out 0:55 to 1:05, stop.
