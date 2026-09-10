# Audio Player [Spring Yard Zone from Sonic The Hedgehog]

Directory: `audio-player-spring-yard-zone/`

Audio-only player for a fixed YouTube track. Starts cold from the top, holds
at full, then fades out and stops. No video, no scrubbing. Sits at the top of
a page as a musical bed the student presses play and reads under.

## Live URL
https://numberdave-cloud.github.io/MPMPT1/audio-player-spring-yard-zone/

## Canvas embed
Height is 190, not the 600 default. This is a slim single-row player. Content
is about 169px on desktop and about 184px on narrow mobile, where the title
line wraps to two lines. 190 clears the tallest case without clipping the
volume fader.

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/audio-player-spring-yard-zone/"
  width="100%"
  height="190"
  title="Spring Yard Zone from Sonic The Hedgehog audio player"
  style="border: none;"
  allow="autoplay"
  loading="lazy"></iframe>
```

## Build state
v1.0. Copied from `audio-player-under-the-skin/` (canonical fade-out shape),
constants and title swapped. Shipped on build for live testing. Playback not
yet verified live or in Canvas.

## What it plays
Masato Nakamura, Spring Yard Zone, from Sonic The Hedgehog (1991).
YouTube ID `Owc5NNYSLwY`.

## Intake values
- Start: from the top, no fade-in
- End point: fade-out starts at 0:41, 10s fade-out

## Fade shape (resolved constants)
- Playback starts cold at 0:00 and holds at full to 0:41.
- `FADE_START` 41 (0:41): linear fade to silence begins.
- `FADE_DURATION` 10: silent at 0:51 (`SCALE` = 51), then pauses and offers
  replay (`STOP_AFTER_FADE` true).
- Progress bar and readout run 0:00 to 0:51 and fill to 100% at the moment it
  goes silent.

## Technical notes
- Audio comes from the YouTube IFrame API. The player lives in a 1px
  absolutely positioned `overflow:hidden` host, rendered rather than
  `display:none` (which would stop playback).
- The fade is automation, not an audio tap. An 80ms ticker polls
  `getCurrentTime` and calls `setVolume`; `fadeFactor(t)` multiplies the
  fader level and effective volume is only pushed when it changes.
- Fade-out is linear. This is a fixed-window shape: `SCALE` comes from the
  fade constants, not from `getDuration()`.
- iOS Safari needs the play tap as the audio gesture, so `playVideo` is called
  directly in the click handler.
- Fader defaults to 70% (`userVol`). Adjust by ear if the bed sits hot or
  quiet against the other players.

## Open decisions / TODOs
- Verify playback and level on the live URL, then inside a Canvas iframe.

## Last updated
2026-09-11. Initial build and ship.
