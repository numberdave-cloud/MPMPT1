# Audio Player [Phat Planet - Leftfield]

Directory: `audio-player-phat-planet/`

Audio-only player for a fixed YouTube track. Enters silent, eases up to full,
holds, then fades out and stops. No video, no scrubbing. Sits at the top of a
page as a musical bed the student presses play and reads under.

## Live URL
https://numberdave-cloud.github.io/MPMPT1/audio-player-phat-planet/

## Canvas embed
Height is 190, not the 600 default. This is a slim single-row player.

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/audio-player-phat-planet/"
  width="100%"
  height="190"
  title="Phat Planet - Leftfield audio player"
  style="border: none;"
  allow="autoplay"
  loading="lazy"></iframe>
```

## Build state
v1.0. Built from the fade-in+out template (`audio-player-history-of-the-ring/`),
video, title and timings swapped. First player built through the `audio-player`
skill intake panel.

## What it plays
Phat Planet by Leftfield. YouTube ID `5GC_X_tI5kA`.

## Fade shape (fade-in + fade-out)
Intake values: full at 0:45 with a 5s fade-in, fade-out from 1:10 over 5s.

Resolved constants at the top of the script:
- `START_AT` 40 (0:40), silent entry.
- `FADE_IN_END` 45 (0:45), full level, on a raised-cosine S-curve up from silence.
- `FADE_OUT_START` 70 (1:10), linear fade to silence begins.
- `FADE_OUT_DURATION` 5, so it lands silent and stops at 1:15.
- `SCALE` is `FADE_OUT_START + FADE_OUT_DURATION` (75).

Clean quote sits at full volume from 0:45 to 1:10 (25s). Progress bar and time
readout run from `START_AT`, so they read 0:00 at first play and fill to 100% at
1:15 (span 35s).

## Technical notes
- Audio comes from the YouTube IFrame API, not embedded base64. The player is
  built in a 1px absolutely positioned box with `overflow:hidden` that clips it
  out of sight, rendered rather than `display:none`, which would stop playback.
- The fade is automation, not a real audio tap. Web Audio cannot read a
  cross-origin YouTube stream, so the fade polls `getCurrentTime` and calls
  `setVolume` on an 80ms ticker. Fade-in eased (raised cosine), fade-out linear.
- Volume fader initialises at 70%. Drag the handle, scroll over it, or use arrow
  keys (Home/End jump to 0/100). Clicking the track does not jump the value.
- iOS Safari needs the play tap as its audio gesture; the play handler calls
  `playVideo` directly.

## Open decisions / TODOs
- Level not yet checked live. Adjust the default fader level if the bed is too
  hot or too quiet against other players.
- Timings and both fade curves to be confirmed on the live URL.

## Last updated
18 August 2026 (v1.0). Built via the audio-player skill intake. Quote 0:45 to
1:10, 5s fades either side, stops at 1:15.
