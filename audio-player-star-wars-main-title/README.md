# Audio Player [Star Wars: Main Title]

Directory: `audio-player-star-wars-main-title/`

Audio-only player for a fixed YouTube track. Sits at the top of a reading page as a musical bed: the student presses play, reads, and the track fades itself to silence on a timer. No video, no scrubbing.

## Live URL
https://numberdave-cloud.github.io/MPMPT1/audio-player-star-wars-main-title/

## Canvas embed
Height is 190, not the 600 default. This is a slim single-row player. Measured content is about 169px on desktop and about 184px on narrow mobile, where the transport row wraps onto a second line. 190 clears the tallest case without clipping the volume fader, and floats on a little transparent slack at wider widths.

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/audio-player-star-wars-main-title/"
  width="100%"
  height="190"
  title="Star Wars Main Title audio player"
  style="border: none;"
  allow="autoplay"
  loading="lazy"></iframe>
```

## Build state
v1.0. Not yet verified playing inside a live Canvas iframe.

## What it plays
Main Title from Star Wars: A New Hope. John Williams and the Wiener Philharmoniker, from "John Williams in Vienna" (Deutsche Grammophon, 2020). YouTube ID `54hoKbTWon4`.

## Technical notes
- Audio comes from the YouTube IFrame API, not embedded base64. The video iframe is rendered but parked off-screen (1px, positioned off-canvas) so only sound reaches the student. `display:none` would stop playback, so it stays positioned instead.
- The fade is automation, not a real audio tap. Web Audio cannot read a cross-origin YouTube stream, so the fade polls `getCurrentTime` and calls `setVolume` on an 80ms ticker.
- Three config constants at the top of the script control the fade: `FADE_START` (210s = 3:30), `FADE_DURATION` (30s), `STOP_AFTER_FADE` (true, pauses the source once it reaches silence). Change these plus `VIDEO_ID` to reuse the player on another page or track.
- Progress bar scale is `FADE_START + FADE_DURATION` (240s = 4:00), not the real track length, so the bar fills to 100% at the exact moment the track goes silent. The time readout shows elapsed against that 4:00 scale.
- Volume fader is a custom control, not a native range input: drag the handle, scroll over it, or use arrow keys (Home/End jump to 0/100). Clicking the track does not jump the value. The fader is a master level that multiplies with the fade, so pulling it down still fades from the lower level and never rides back up.
- Once the fade completes, the play button becomes a replay: it seeks to 0 and restores the fader level.
- iOS Safari needs the play tap as its audio gesture; the play button handler calls `playVideo` directly to satisfy that.

## Open decisions / TODOs
- Folder name was proposed by Claude. Confirm before the embed goes live in Canvas, since renaming later means re-embedding.
- Playback and exact iframe fit not yet verified in live Canvas.
- Metadata line uses a spaced hyphen as separator ("...A New Hope - John Williams"). Swap to a comma if preferred.
- EQ animation beside the transport is a cosmetic "playing" tell, not real spectrum data. Remove if it reads as too decorative for the design system.

## Last updated
13 August 2026. Initial ship. Audio-only YouTube player with a single metadata line, custom volume fader, and a 3:30 to 4:00 fade to silence.
