# Expression and Dynamics

**Directory:** `expression-dynamics/`

A two-tile A/B listening comparison. The student taps to hear the same passage first without any dynamics automation, then with dynamic automation applied to the string parts. Same engine as the soundboard family, stripped back to two wide tiles and no readout. Built for the movie scoring unit (MMI3).

## Live URL

https://numberdave-cloud.github.io/MPMPT1/expression-dynamics/

## Canvas embed

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/expression-dynamics/"
  width="100%"
  height="300"
  title="Expression and Dynamics"
  style="border: none;"
  allow="autoplay"
  loading="lazy">
</iframe>
```

Height 300: the card hugs its content at ~276px (no info panel). The rack has no fixed aspect ratio here, so it scales with width.

## Build state

v1.0, 2026-08-20. Category: Arranging. Two clips embedded and decode-verified.

## Tiles

Two double-wide tiles in one row: "Without Dynamics" (left, the first piece) and "With Dynamics" (right, the second). Order matches the lede's first-then-second framing.

## Interaction

- Tap or click a tile: plays its clip once, with the glow ring and equaliser until it ends.
- Only one plays at a time: tapping the other tile stops the first and starts the second, which is the intended A/B behaviour.
- Keyboard: tiles focusable, trigger on Enter or Space.
- No readout panel and no source line on this board, by request.

## Audio

- Two one-shot WAVs embedded as base64, decoded via `atob()` and played through Web Audio (`AUDIO` map keyed by tile name).
- Each clip: 24.0s, stereo, 44.1kHz (full musical excerpts, not short one-shots).
- Total page ~10.8MB.
- Playback fires on tap only.

## Copy

- Title and the explainer lede are the user's, used as written. Tile labels are plain ("Without Dynamics" / "With Dynamics").

## Provenance

- Built from the String Articulations / Orchestra Soundboard engine, with the readout, sources, hover notes and MIDI tips removed. Grid dropped to two columns; tiles widened (aspect ratio 2 / 0.9); rack aspect ratio removed so the card hugs its content.

## Open TODOs

- Verify audio playback and layout live in Canvas.
- Optional: downmix to mono to roughly halve the page weight.

## Last updated

2026-08-20. v1.0: initial build. Two-tile A/B dynamics comparison, tap to play with glow and equaliser, no readout. Engine from the soundboard family. Shipped for the MMI3 movie scoring unit.
