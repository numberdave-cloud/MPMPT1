# Audio Player Registry

Every audio-only player in the repo. Read this before touching any player.

An audio player is a slim single-row transport that plays a fixed YouTube track
as a musical bed. No video, no scrubbing. It sits at the top of a page and the
student presses play and reads under it.

All instances share one machinery. Only a few things differ per instance: the
config constants at the top of the script, the card `<title>` and the on-card
title line, and the folder name. **A fix to the shared machinery must be applied
to every folder listed below, not just the one being worked on.**

Category for all players: **Miscellaneous**.

## Fade shapes

Four shapes, and the shape decides which folder to copy when making a new one.
The split runs deeper than the fade: the two "plays to natural end" shapes read
progress off the real video duration, the two "fixed window" shapes compute it
from the fade constants and stop themselves. Copy the canonical source for the
shape rather than reworking a different one.

| Shape | Canonical source | Ends how | Config surface |
| --- | --- | --- | --- |
| Plain | `audio-player-order-in-chaos/` | plays to the track's natural end | `VIDEO_ID`, `START_AT` |
| Fade-out | `audio-player-under-the-skin/` | fades to silence and stops | `VIDEO_ID`, `FADE_START`, `FADE_DURATION`, `STOP_AFTER_FADE` |
| Fade-in | `audio-player-mausam-escape/` | plays to the track's natural end | `VIDEO_ID`, `START_AT`, `FADE_DURATION` |
| Fade-in + out | `audio-player-history-of-the-ring/` | fades to silence and stops | `VIDEO_ID`, `START_AT`, `FADE_IN_END`, `FADE_OUT_START`, `FADE_OUT_DURATION`, `STOP_AFTER_FADE` |

## Instances

| Folder | Card title | Video ID | Shape | Entry | Fade | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `audio-player-order-in-chaos/` | Order in the Chaos | `mQOOToUY6fw` | plain | 0:00 | none | live, confirmed working |
| `audio-player-solar-sailer/` | Solar Sailer | `f9cKyVJuV2Y` | plain | 0:00 | none | live, confirmed working |
| `audio-player-jaws-main-title/` | Main Title from Jaws (1975), John Williams | `pwiqKSfnPp8` | plain | 0:00 | none | live, playback unverified |
| `audio-player-vampire-hunters/` | Vampire Hunters from Bram Stoker's Dracula by Wojciech Kilar | `k_53LEwnGXU` | plain | 0:00 | none | live, playback unverified |
| `audio-player-solange/` | Solange from Casino Royale - David Arnold | `f_NpqG0E1Tk` | plain | 0:00 | none | live, playback unverified |
| `audio-player-under-the-skin/` | Under the Skin: Lonely Void | `7NIz94ILjxI` | fade-out | 0:00 | out at 1:30, 10s | live, confirmed working |
| `audio-player-forbidden-planet/` | Forbidden Planet: Graveyard | `WR-MkDKWWW0` | fade-out | 0:00 | out at 1:00, 10s | live, confirmed working |
| `audio-player-gone-with-the-wind/` | Gone with the Wind: Main Title | `EESHIpo4Lgk` | fade-out | 0:00 | out at 1:50, 10s | live, confirmed working |
| `audio-player-midnight-express/` | Midnight Express: The Chase | `mpW3C_k0WMY` | fade-out | 0:00 | out at 1:56, 10s | live, confirmed working |
| `audio-player-star-wars-main-title/` | Star Wars: Main Title | `54hoKbTWon4` | fade-out | 0:00 | out at 3:30, 30s | live, confirmed working |
| `audio-player-terminator-2/` | Terminator 2: Main Theme | `lqcHjUJadp8` | fade-out | 0:00 | out at 1:35, 10s | live, confirmed working |
| `audio-player-mausam-escape/` | Mausam & Escape | `_WOWIH41W4c` | fade-in | 0:36 | in over 4s | live, confirmed working |
| `audio-player-history-of-the-ring/` | History of the Ring | `GuiROE85RMQ` | fade-in+out | 0:23 | in to 0:28, out at 1:34 over 8s | live, confirmed working |
| `audio-player-phat-planet/` | Phat Planet - Leftfield | `5GC_X_tI5kA` | fade-in+out | 0:40 | in to 0:45, out at 1:10 over 5s | live, confirmed working |
| `audio-player-nosferatu-premonition/` | Premonition from Nosferatu - Robin Carolan | `tAnN8AgRkoQ` | fade-in+out | 0:05 | in to 0:10, out at 1:04 over 8s | live, playback unverified |
| `audio-player-robocop-force-shoots-robo/` | Force Shoots Robo from Robocop - Basil Poledouris | `22da-7-q1D8` | fade-in+out | 1:04 | in to 1:10, out at 1:48 over 10s | live, playback unverified |

Live URL pattern: `https://numberdave-cloud.github.io/MPMPT1/<folder>/`

## Naming

`audio-player-<subject>`. Keep the subject short and greppable.

## Making a new one

Full workflow lives in the `audio-player` skill (`skills/audio-player/SKILL.md`).
In short:

1. Pick the fade shape, copy its canonical source folder to `audio-player-<subject>/`.
2. Remove the copied `README.md`.
3. Set `VIDEO_ID`, the timing constants for the shape, the card `<title>` and the on-card title line.
4. `node --check` the script, screenshot with Playwright, present for review.
5. On ship: write the folder `README.md`, add a row here and to `INDEX.md`, one commit, verify the raw URL.

## Config fields

| Field | Notes |
| --- | --- |
| `VIDEO_ID` | YouTube ID only, not the full URL |
| `START_AT` | seconds, where playback enters. `0` is the top of the track |
| `FADE_START` | fade-out shape. seconds, where the fade to silence begins |
| `FADE_DURATION` | fade-out and fade-in shapes. seconds, length of the fade |
| `FADE_IN_END` | fade-in+out shape. seconds, where the eased fade-in reaches full |
| `FADE_OUT_START` | fade-in+out shape. seconds, where the fade to silence begins |
| `FADE_OUT_DURATION` | fade-in+out shape. seconds, length of the fade to silence |
| `STOP_AFTER_FADE` | fixed-window shapes. pause the source once it has faded to nothing |

## Levels

Same wall as the quoters. The IFrame API exposes no loudness data and the audio
sits in a cross-origin iframe, so it cannot be measured from outside and there
is no automatic normalisation. The fader default is 70%. If a bed is too hot or
too quiet against the others, adjust the default fader level (`userVol`) by ear.

## Shared machinery, known behaviours

- **The fade is automation, not a real audio tap.** Web Audio cannot read a
  cross-origin YouTube stream, so an 80ms ticker polls `getCurrentTime` and
  calls `setVolume`. `fadeFactor(t)` multiplies the fader level. Effective
  volume is only pushed when it changes.
- **Fade-in curve is eased (raised cosine), fade-out is linear.** A linear ramp
  out of silence sounds abrupt, so the fade-in uses `0.5 - 0.5*cos(pi*p)`. The
  fade-out is a straight ramp and reads fine going into silence.
- **The IFrame API player lives in a 1px `overflow:hidden` host,** absolutely
  positioned and clipped out of sight. It is rendered, never `display:none`,
  which would stop playback.
- **Progress model forks by shape.** Fixed-window shapes run the bar and readout
  from `START_AT` to `SCALE` (`FADE_OUT_START + FADE_OUT_DURATION`, or
  `FADE_START + FADE_DURATION`), a known span, and call `finish` at the end.
  Play-to-end shapes set `scale` from `getDuration()` once it is known and end on
  the YouTube `ENDED` event.
- **The volume fader ignores click-to-jump.** Drag starts on the handle only, so
  clicking the track never moves the value. Scroll wheel and arrow keys also
  work (Home/End jump to 0/100). It initialises at 70%.
- **iOS Safari needs the play tap as its audio gesture.** The play handler calls
  `playVideo` directly to satisfy that.
- **`html` and `body` are locked to 100% height with `overflow:hidden`,** so page
  content can never exceed the iframe.

## Embed

Height 190, not the 600 default. This is a slim single-row player. Content is
about 169px on desktop and about 184px on narrow mobile where a long title line
wraps to two lines. 190 clears the tallest case without clipping the fader. Keep
the embed at or above 185.

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/<folder>/"
  width="100%"
  height="190"
  title="<card title> audio player"
  style="border: none;"
  allow="autoplay"
  loading="lazy"></iframe>
```

## Source durability

Each bed depends on its source video staying up. An unofficial upload of
commercial music is more likely to be removed than an official channel. Prefer
official uploads where one exists, and check any player that has been sitting
unused for a while.

## Last updated

2026-08-20. Added `audio-player-solange/` (plain shape, video `f_NpqG0E1Tk`).
Registry now catalogues fourteen players and the four fade shapes with their
canonical source folders.
