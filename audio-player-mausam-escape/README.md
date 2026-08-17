# Audio Player [Mausam & Escape]

Directory: `audio-player-mausam-escape/`

Audio-only player for a fixed YouTube track. Playback enters partway into the
track and fades in from silence, then plays through to the natural end. No
video, no scrubbing. Sits at the top of a page as a musical bed the student
presses play and reads under.

## Live URL
https://numberdave-cloud.github.io/MPMPT1/audio-player-mausam-escape/

## Canvas embed
Height is 190, not the 600 default. This is a slim single-row player. Content
is about 169px on desktop and about 184px on narrow mobile, where the transport
row wraps onto a second line. 190 clears the tallest case without clipping the
volume fader.

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/audio-player-mausam-escape/"
  width="100%"
  height="190"
  title="Mausam and Escape audio player"
  style="border: none;"
  allow="autoplay"
  loading="lazy"></iframe>
```

## Build state
v1.0. Built on the audio-player template, adapted from a fade-out player into a
fade-in player with an entry offset. Not yet verified playing inside a live
Canvas iframe.

## What it plays
Mausam & Escape from Slumdog Millionaire (2008). A.R. Rahman. YouTube ID
`_WOWIH41W4c`. Playback enters at 0:36.

## Technical notes
- This is the mirror image of the Under the Skin player: instead of fading out
  to silence at a set point, it enters silent and fades in.
- Audio comes from the YouTube IFrame API, not embedded base64. The IFrame API
  builds a 640x360 player, so its wrapper is a 1px absolutely positioned box
  with `overflow:hidden` that clips the player out of sight. It is rendered
  rather than set to `display:none`, which would stop playback.
- Fade config lives in three constants at the top of the script: `START_AT`
  (36s = 0:36, the entry point), `FADE_DURATION` (4s), and `VIDEO_ID`. Silent
  at 0:36, full level at 0:40, then plays through. Change these to reuse the
  player on another page or track.
- The fade is automation, not a real audio tap. Web Audio cannot read a
  cross-origin YouTube stream, so the fade polls `getCurrentTime` and calls
  `setVolume` on an 80ms ticker. `fadeFactor` ramps 0 to 1 across the window
  from `START_AT` to `START_AT + FADE_DURATION`.
- The fade-in target is the fader level, which defaults to 70%. So the ramp
  runs 0 to 70, not 0 to 100. Pulling the fader down mid-play scales the target.
- Progress bar and time readout are measured from `START_AT`, not from 0:00 of
  the source. They read 0:00 at the moment playback begins and fill to 100% at
  the track's natural end.
- Full track length is discovered at runtime via `getDuration`, polled until
  the source reports it (it is often 0 for a beat after `onReady`). The readout
  scale is `duration - START_AT`.
- End of track is caught by the YouTube ENDED event, which flips the play
  button to a replay control. Replay re-enters at 0:36 silent and fades in again.
- Volume fader is a custom control: drag the handle, scroll over it, or use
  arrow keys (Home/End jump to 0/100). Clicking the track does not jump the
  value. It initialises at 70%.
- `html` and `body` are locked to 100% height with `overflow:hidden`, so page
  content can never exceed the iframe and Canvas cannot scroll the card
  internally. Keep the embed height at or above 185 so nothing clips on mobile.
- iOS Safari needs the play tap as its audio gesture; the play button handler
  calls `playVideo` directly to satisfy that.

## Open decisions / TODOs
- Playback and the fade curve not yet verified in a live Canvas iframe.
- End behaviour is play-through-then-replay. Loop or a fade-out at the end were
  offered and not taken; either is a small change if wanted later.
- Fade-in target sits at the 70% fader default. Raise the default if a louder
  landing level is wanted.
- Metadata line uses a spaced hyphen as separator. Swap to a comma if preferred.

## Last updated
17 August 2026 (v1.0). Initial ship. Enters at 0:36, 4s fade in to 0:40, plays
through to end.
