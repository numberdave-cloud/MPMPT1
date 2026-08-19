# Audio Player [Vampire Hunters]

Directory: `audio-player-vampire-hunters/`

Slim single-row audio-only YouTube player. Plays "Vampire Hunters" from Bram
Stoker's Dracula (Wojciech Kilar) as a musical bed. Plain shape: enters at the
top, plays to the track's natural end. No video, no scrubbing.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/audio-player-vampire-hunters/

## Canvas embed

Height 190, not the 600 default. This is a single slim transport row: content
runs about 169px on desktop and about 184px on narrow mobile where a long title
wraps. 190 clears the tallest case without clipping the fader.

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/audio-player-vampire-hunters/"
  width="100%"
  height="190"
  title="Vampire Hunters audio player"
  style="border: none;"
  allow="autoplay"
  loading="lazy"></iframe>
```

## Config

- Video ID: `k_53LEwnGXU`
- Shape: plain (`audio-player-order-in-chaos/` lineage)
- `START_AT = 0` (top of the track)
- No fades. Ends on the YouTube `ENDED` event; progress scale is read from
  `getDuration()` once known.

## Technical notes

- Standard shared player machinery, unchanged from the family. The IFrame API
  player lives in a 1px `overflow:hidden` host (never `display:none`, which
  stops playback).
- Plain shape is a play-to-end shape, so the bar and readout scale off the real
  video duration rather than a fixed window.
- Fader defaults to 70% (`userVol`). Level is only checkable live, so a default
  tweak may follow once heard in Canvas.

## Open decisions / TODOs

- Playback and level unverified in Canvas as of ship. Confirm live.

## Last updated

2026-08-20. Created from the plain source. Whole-track bed of Kilar's Vampire
Hunters, video `k_53LEwnGXU`.
