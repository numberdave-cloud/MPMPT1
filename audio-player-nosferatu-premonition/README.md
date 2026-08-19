# Audio Player [Premonition from Nosferatu - Robin Carolan]

Directory: `audio-player-nosferatu-premonition/`

## What it plays

A slim single-row audio-only player. Plays a quoted window of "Premonition"
from Robin Carolan's Nosferatu (2024) score as a musical bed. Fade-in+out
shape: enters silent, reaches full at the start point, holds, then fades to
silence and stops.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/audio-player-nosferatu-premonition/

## Canvas embed

Height 190, not the 600 default. This is a single slim transport row; content
runs about 169px desktop and about 184px on narrow mobile where the title wraps.
190 clears the tallest case without clipping the fader.

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/audio-player-nosferatu-premonition/"
  width="100%"
  height="190"
  title="Premonition from Nosferatu - Robin Carolan audio player"
  style="border: none;"
  allow="autoplay"
  loading="lazy"></iframe>
```

## Config

- Video ID: `tAnN8AgRkoQ`
- Shape: fade-in+out (source: `audio-player-history-of-the-ring/`)
- Intake: start point 0:10 with a 5s fade-in, end point 1:04 with an 8s fade-out

Resolved constants:

- `START_AT = 5` (0:05, enters silent)
- `FADE_IN_END = 10` (0:10, full level)
- `FADE_OUT_START = 64` (1:04, fade to silence begins)
- `FADE_OUT_DURATION = 8`
- `STOP_AFTER_FADE = true`

Window runs 0:05 to 1:12 (`FADE_OUT_START + FADE_OUT_DURATION`), then stops.

## Technical notes

- IFrame API player lives in a 1px `overflow:hidden` host, never `display:none`
  (which stops YouTube playback).
- Fade is automation, not a real audio tap: an 80ms ticker polls
  `getCurrentTime` and calls `setVolume`. Fade-in eased (raised cosine),
  fade-out linear.
- Fixed-window shape: progress runs `START_AT` to `SCALE` and calls `finish`.
- Fader default 70% (`userVol`). Level is only checkable live, so a default
  tweak may follow testing.

## Open items

- Playback and fade timing unverified in Canvas (ship-on-build; test live).
- Level unverified against the other beds.

## Last updated

2026-08-19. Built from intake. New player, fade-in+out shape.
