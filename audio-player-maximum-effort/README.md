# Audio Player [Maximum Effort from Deadpool]

Directory: `audio-player-maximum-effort/`

Audio-only player for a fixed YouTube track. Enters silent, eases up to full,
then plays through to the track's natural end. No video, no scrubbing. Sits at
the top of a page as a musical bed the student presses play and reads under.

## Live URL
https://numberdave-cloud.github.io/MPMPT1/audio-player-maximum-effort/

## Canvas embed
Height is 190, not the 600 default. This is a slim single-row player. Content
is about 169px on desktop and about 184px on narrow mobile, where the title
line wraps to two lines. 190 clears the tallest case without clipping the
volume fader.

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/audio-player-maximum-effort/"
  width="100%"
  height="190"
  title="Maximum Effort from Deadpool audio player"
  style="border: none;"
  allow="autoplay"
  loading="lazy"></iframe>
```

## Build state
v1.0. Copied from `audio-player-mausam-escape/` (canonical fade-in shape),
constants and title swapped. Shipped on build for live testing. Playback not
yet verified live or in Canvas.

## What it plays
Tom Holkenborg (Junkie XL), Maximum Effort, from Deadpool (2016).
YouTube ID `4wD5tamhwXo`.

## Intake values
- Start point: full at 0:40, 5s fade-in
- End: plays to the natural end, no fade-out

## Fade shape (resolved constants)
- `START_AT` 35 (0:35): playback enters here, silent.
- `FADE_DURATION` 5: eased raised-cosine fade-in reaches full at 0:40.
- Plays at full through to the track's natural end and stops on the YouTube
  `ENDED` event.
- Progress bar and readout run from `START_AT`, so they read 0:00 at entry;
  the span is `getDuration()` minus 35, discovered once the source is ready.

## Technical notes
- Audio comes from the YouTube IFrame API. The player lives in a 1px
  absolutely positioned `overflow:hidden` host, rendered rather than
  `display:none` (which would stop playback).
- The fade is automation, not an audio tap. An 80ms ticker polls
  `getCurrentTime` and calls `setVolume`; `fadeFactor(t)` multiplies the
  fader level and effective volume is only pushed when it changes.
- Fade-in is eased (raised cosine). This is a play-to-end shape: `scale`
  comes from `getDuration()`, not from fade constants.
- iOS Safari needs the play tap as the audio gesture, so `playVideo` is called
  directly in the click handler.
- Fader defaults to 70% (`userVol`). Adjust by ear if the bed sits hot or
  quiet against the other players.

## Open decisions / TODOs
- Verify playback and level on the live URL, then inside a Canvas iframe.

## Last updated
2026-09-10. Initial build and ship.
