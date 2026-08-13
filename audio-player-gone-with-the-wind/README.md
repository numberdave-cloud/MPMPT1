# Audio Player [Gone with the Wind: Main Title]

Directory: `audio-player-gone-with-the-wind/`

Audio-only player for a fixed YouTube track. Sits at the top of a reading page as a musical bed: the student presses play, reads, and the track fades itself to silence on a timer. No video, no scrubbing.

## Live URL
https://numberdave-cloud.github.io/MPMPT1/audio-player-gone-with-the-wind/

## Canvas embed
Height is 190, not the 600 default. This is a slim single-row player. Content is about 169px on desktop and about 184px on narrow mobile, where the transport row wraps onto a second line. 190 clears the tallest case without clipping the volume fader.

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/audio-player-gone-with-the-wind/"
  width="100%"
  height="190"
  title="Gone with the Wind main title audio player"
  style="border: none;"
  allow="autoplay"
  loading="lazy"></iframe>
```

## Build state
v1.0. Built on the corrected player template (clipped hidden player, body locked to iframe height, 70% default volume). Not yet verified playing inside a live Canvas iframe.

## What it plays
Main Title from Gone with the Wind (1939). Max Steiner. YouTube ID `EESHIpo4Lgk`.

## Technical notes
- Audio comes from the YouTube IFrame API, not embedded base64. The IFrame API builds a 640x360 player, so its wrapper is a 1px absolutely positioned box with `overflow:hidden` that clips the player out of sight. It is rendered rather than set to `display:none`, which would stop playback.
- `html` and `body` are locked to 100% height with `overflow:hidden`, so page content can never exceed the iframe and Canvas cannot scroll the card internally. The card is centred in whatever embed height is set. Keep the embed height at or above 185 so nothing clips on narrow mobile.
- The fade is automation, not a real audio tap. Web Audio cannot read a cross-origin YouTube stream, so the fade polls `getCurrentTime` and calls `setVolume` on an 80ms ticker.
- Fade config lives in three constants at the top of the script: `FADE_START` (110s = 1:50), `FADE_DURATION` (10s), `STOP_AFTER_FADE` (true, pauses the source once it reaches silence). Change these plus `VIDEO_ID` to reuse the player on another page or track.
- Progress bar scale is `FADE_START + FADE_DURATION` (120s = 2:00), not the real track length, so the bar fills to 100% at the exact moment the track goes silent. The time readout shows elapsed against that scale.
- Volume fader is a custom control: drag the handle, scroll over it, or use arrow keys (Home/End jump to 0/100). Clicking the track does not jump the value. It initialises at 70%. The fader multiplies with the fade, so pulling it down still fades from the lower level.
- Once the fade completes, the play button becomes a replay: it seeks to 0 and restores the fader level.
- iOS Safari needs the play tap as its audio gesture; the play button handler calls `playVideo` directly to satisfy that.

## Open decisions / TODOs
- Playback not yet verified in a live Canvas iframe.
- Metadata line uses a spaced hyphen as separator. Swap to a comma if preferred.

## Last updated
13 August 2026 (v1.0). Initial ship. One of a batch of fixed-track reading-bed players. Fade to silence over 10s starting at 1:50.
