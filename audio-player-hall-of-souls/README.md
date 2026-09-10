# Audio Player [The Hall of Souls from Quake 1]

Directory: `audio-player-hall-of-souls/`

Audio-only player for a fixed YouTube track. Enters silent, eases up to full,
holds, then fades out and stops. No video, no scrubbing. Sits at the top of a
page as a musical bed the student presses play and reads under.

## Live URL
https://numberdave-cloud.github.io/MPMPT1/audio-player-hall-of-souls/

## Canvas embed
Height is 190, not the 600 default. This is a slim single-row player. Content
is about 169px on desktop and about 184px on narrow mobile, where the title
line wraps to two lines. 190 clears the tallest case without clipping the
volume fader.

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/audio-player-hall-of-souls/"
  width="100%"
  height="190"
  title="The Hall of Souls from Quake 1 audio player"
  style="border: none;"
  allow="autoplay"
  loading="lazy"></iframe>
```

## Build state
v1.0. Copied from `audio-player-history-of-the-ring/` (canonical fade-in+out
shape), constants and title swapped. Shipped on build for live testing.
Playback not yet verified live or in Canvas.

## What it plays
Trent Reznor / Nine Inch Nails, The Hall of Souls, from Quake (1996).
YouTube ID `gkktyOA06NQ`.

## Intake values
- Start point: full at 2:10, 5s fade-in
- End point: fade-out starts at 3:00, 10s fade-out

## Fade shape (resolved constants)
- `START_AT` 125 (2:05): playback enters here, silent.
- `FADE_IN_END` 130 (2:10): eased raised-cosine fade-in reaches full.
- Holds at full from 2:10 to 3:00.
- `FADE_OUT_START` 180 (3:00): linear fade to silence begins.
- `FADE_OUT_DURATION` 10: silent at 3:10 (`SCALE` = 190), then pauses and
  offers replay.
- Progress bar and readout run from `START_AT`, so they read 0:00 at entry and
  fill to 100% at 3:10 (span 65s, 1:05).

## Technical notes
- Audio comes from the YouTube IFrame API. The player lives in a 1px
  absolutely positioned `overflow:hidden` host, rendered rather than
  `display:none` (which would stop playback).
- The fade is automation, not an audio tap. An 80ms ticker polls
  `getCurrentTime` and calls `setVolume`; `fadeFactor(t)` multiplies the
  fader level and effective volume is only pushed when it changes.
- Fade-in is eased (raised cosine), fade-out is linear.
- iOS Safari needs the play tap as the audio gesture, so `playVideo` is called
  directly in the click handler.
- Fader defaults to 70% (`userVol`). Adjust by ear if the bed sits hot or
  quiet against the other players.

## Open decisions / TODOs
- Verify playback and level on the live URL, then inside a Canvas iframe.

## Last updated
2026-09-11. Initial build and ship.
