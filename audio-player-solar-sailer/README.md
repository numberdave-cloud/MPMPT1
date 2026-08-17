# Audio Player [Solar Sailer]

Directory: `audio-player-solar-sailer/`

Audio-only player for a fixed YouTube track. Plays from the top at the fader
level, no volume automation, no fade. No video, no scrubbing. Sits at the top
of a page as a musical bed the student presses play and reads under.

## Live URL
https://numberdave-cloud.github.io/MPMPT1/audio-player-solar-sailer/

## Canvas embed
Height is 190, not the 600 default. This is a slim single-row player. Content
is about 169px on desktop and about 165px on narrow mobile. 190 clears it
without clipping the volume fader.

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/audio-player-solar-sailer/"
  width="100%"
  height="190"
  title="Solar Sailer audio player"
  style="border: none;"
  allow="autoplay"
  loading="lazy"></iframe>
```

## Build state
v1.0. Built on the no-fade audio-player template (copied from
`audio-player-order-in-chaos/`, video and title swapped). Not yet verified
playing inside a live Canvas iframe.

## What it plays
Solar Sailer from TRON: Legacy (2010). Daft Punk. YouTube ID `f9cKyVJuV2Y`.

## Technical notes
- No fade in, no fade out, no entry offset. Volume is the fader level throughout.
- Audio comes from the YouTube IFrame API, not embedded base64. The IFrame API
  builds a 640x360 player, so its wrapper is a 1px absolutely positioned box
  with `overflow:hidden` that clips the player out of sight. It is rendered
  rather than set to `display:none`, which would stop playback.
- Config is two constants at the top of the script: `VIDEO_ID` and `START_AT`
  (0 = top of the track). There is no fade constant because there is no fade.
- Progress bar and time readout run against the full track length, discovered
  at runtime via `getDuration`, polled until the source reports it. The 80ms
  ticker updates the readout only; it does not touch volume.
- End of track is caught by the YouTube ENDED event, which flips the play
  button to a replay control.
- Volume fader is a custom control: drag the handle, scroll over it, or use
  arrow keys (Home/End jump to 0/100). Clicking the track does not jump the
  value. It initialises at 70%.
- `html` and `body` are locked to 100% height with `overflow:hidden`, so page
  content can never exceed the iframe. Keep the embed height at or above 185 so
  nothing clips on mobile.
- iOS Safari needs the play tap as its audio gesture; the play button handler
  calls `playVideo` directly to satisfy that.
- The `.rack.fading` CSS rule is inherited from the fade-capable siblings and
  is inert here, since the fading class is never applied.

## Open decisions / TODOs
- Playback not yet verified in a live Canvas iframe.
- Default fader level is 70%. Raise the default if a louder level is wanted.
- Metadata line uses a spaced hyphen as separator. Swap to a comma if preferred.

## Last updated
17 August 2026 (v1.0). Initial ship. No-fade player, plays from the top.
