# Audio Player [Jaws: Main Title]

Directory: `audio-player-jaws-main-title/`
Category: Miscellaneous
Family: audio player (see `PLAYERS.md` at repo root)

## What it does

Slim single-row transport that plays the Main Title from *Jaws* (1975) by John
Williams as an audio-only bed at the top of a Canvas page. No video, no
scrubbing. Plain fade shape: enters at the top of the track and plays through to
the natural end.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/audio-player-jaws-main-title/

## Canvas embed

Height 190, not the 600 default. This is a single slim row: measured content is
about 169px on desktop and about 184px on narrow mobile where a long title line
wraps. 190 clears the tallest case without clipping the volume fader. Keep it at
or above 185.

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/audio-player-jaws-main-title/"
  width="100%"
  height="190"
  title="Main Title from Jaws (1975), John Williams audio player"
  style="border: none;"
  allow="autoplay"
  loading="lazy"></iframe>
```

## Build state

v1.0. Built from the canonical plain-shape source `audio-player-order-in-chaos/`.
Shared machinery untouched. Script validated with `node --check`. Layout verified
with Playwright at 900px and 380px viewport widths, title holds one line at both.
Playback not verifiable locally: the YouTube IFrame API does not load from
`file://` (error 153), so playback is confirmed on the live URL only.

## Config

| Field | Value |
| --- | --- |
| `VIDEO_ID` | `pwiqKSfnPp8` |
| `START_AT` | `0` (top of the track) |
| Shape | plain |
| Ends | on the YouTube `ENDED` event, at the track's natural end |
| Fader default | 70% (`userVol`) |

## Technical notes

- The IFrame API player sits in a 1px `overflow:hidden` host, absolutely
  positioned and clipped out of sight. It is rendered, never `display:none`,
  which would stop playback.
- Plain is a play-to-end shape: `scale` is set from `getDuration()` once known
  and the player ends on the `ENDED` event. Do not graft fixed-window progress
  logic (`SCALE` from fade constants, `finish`) onto it.
- The volume fader ignores click-to-jump. Drag on the handle, scroll wheel, or
  arrow keys (Home/End jump to 0/100).
- iOS Safari needs the play tap as its audio gesture, so the play handler calls
  `playVideo` directly. Keep it in the click handler.
- `html` and `body` are locked to 100% height with `overflow:hidden`, so page
  content can never exceed the iframe.
- Levels cannot be measured from outside a cross-origin iframe and there is no
  automatic normalisation. If this bed sits hot or quiet against the others,
  adjust the `userVol` default by ear.

## Open decisions / TODOs

- Level unset by ear. Fader default is the family standard 70% and may need a
  nudge once heard against the other beds.
- Source durability: `pwiqKSfnPp8` is not an official label channel upload, so
  it carries a higher takedown risk than the official-channel players in the
  family. Worth re-checking before a teaching block that depends on it, and
  worth swapping to an official upload if one appears.
- Not yet verified inside Canvas.

## Last updated

2026-08-18. Created. Plain-shape player built from `audio-player-order-in-chaos/`,
video ID and titles swapped, nothing else changed.
