# Audio Player [Force Shoots Robo from Robocop - Basil Poledouris]

Directory: `audio-player-robocop-force-shoots-robo/`

## What it plays

A slim single-row audio-only player. Plays a quoted window of "Force Shoots
Robo" from Basil Poledouris's Robocop (1987) score as a musical bed.
Fade-in+out shape: enters silent, reaches full at the start point, holds, then
fades to silence and stops.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/audio-player-robocop-force-shoots-robo/

## Canvas embed

Height 190, not the 600 default. This is a single slim transport row; content
runs about 169px desktop and about 184px on narrow mobile where the title wraps.
190 clears the tallest case without clipping the fader.

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/audio-player-robocop-force-shoots-robo/"
  width="100%"
  height="190"
  title="Force Shoots Robo from Robocop - Basil Poledouris audio player"
  style="border: none;"
  allow="autoplay"
  loading="lazy"></iframe>
```

## Config

- Video ID: `22da-7-q1D8`
- Shape: fade-in+out (source: `audio-player-history-of-the-ring/`)
- Intake: start point 1:10 with a 6s fade-in, end point 1:48 with a 10s fade-out

Resolved constants:

- `START_AT = 64` (1:04, enters silent)
- `FADE_IN_END = 70` (1:10, full level)
- `FADE_OUT_START = 108` (1:48, fade to silence begins)
- `FADE_OUT_DURATION = 10`
- `STOP_AFTER_FADE = true`

Window runs 1:04 to 1:58 (`FADE_OUT_START + FADE_OUT_DURATION`), then stops.

## Technical notes

- IFrame API player lives in a 1px `overflow:hidden` host, never `display:none`
  (which stops YouTube playback).
- Fade is automation, not a real audio tap: an 80ms ticker polls
  `getCurrentTime` and calls `setVolume`. Fade-in eased (raised cosine),
  fade-out linear.
- Fixed-window shape: progress runs `START_AT` to `SCALE` and calls `finish`.
- Fade envelope runs on `smoothTime()`: getCurrentTime interpolated with a local
  clock (30ms ticker) so the fade is smooth, not stepped by YouTube's coarse
  clock. This is a shared-machinery change that currently lives only in this
  folder, pending live confirmation before propagating to the family.
- Fader default 70% (`userVol`). Level is only checkable live, so a default
  tweak may follow testing.

## Open items

- Playback and fade timing unverified in Canvas (ship-on-build; test live).
- Level unverified against the other beds.
- Fade-smoothing (smoothTime + 30ms ticker) not yet propagated to the other 11
  players. Roll out across the family once confirmed smooth here.

## Last updated

2026-08-19. Built from intake, then added smoothTime() fade interpolation and a
30ms ticker to fix a ragged fade-in. Family propagation pending confirmation.
