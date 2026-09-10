# Timbre Comparison

**Directory:** `timbre-comparison/`

A three-tile listening comparison. The student taps to hear the same passage played on piano, brass and synth, one at a time, to hear how timbre changes the character of identical material. Same engine as Expression and Dynamics, widened to three tiles, no lede.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/timbre-comparison/

## Canvas embed

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/timbre-comparison/"
  width="100%"
  height="300"
  title="Timbre Comparison"
  style="border: none;"
  allow="autoplay"
  loading="lazy">
</iframe>
```

Height 300: the card hugs its content at roughly 230 to 260px at desktop widths (no lede, no readout). Under 520px the tiles stack to one column and the card grows to around 530px. Height was estimated from the CSS, not measured in a browser (Playwright download was blocked on the build session). Confirm in Canvas.

## Build state

v1.0, 2026-09-10. Category: Composition. Three clips embedded and decode-verified.

## Tiles

Three tiles in one row: Piano, Brass, Synth. Source files were labelled Upright Piano, Brass Quartet and Wavetable.

## Interaction

- Tap or click a tile: plays its clip once from the top, with the glow ring and equaliser until it ends. No loop.
- Only one plays at a time: tapping another tile stops the first and starts the second.
- Keyboard: tiles focusable, trigger on Enter or Space.
- No lede, readout or source line, by request.

## Audio

- Three OGG Vorbis clips embedded as base64, decoded via `atob()` and `decodeAudioData`, played through Web Audio (`AUDIO` map keyed by tile name).
- Each clip: 27.0s, stereo, 44.1kHz. About 830KB each; page ~3.4MB.
- Playback fires on tap only.
- A tile whose `AUDIO` entry is null flashes for two seconds and stops (safety net for future clip swaps).
- Caveat: Safari's `decodeAudioData` has historically not accepted Vorbis. If iPad students report silence, re-encode the clips as AAC (.m4a) or MP3; the clips don't loop, so encoder delay is not a concern. The decode path is unchanged.

## Copy

- Title is the user's. Tile labels are plain instrument names.

## Provenance

- Built from `expression-dynamics/`. Grid widened to three columns, tile aspect adjusted (2 / 1.1), frame updated to the current rack-card language (2px dark frame with inset stroke), lede removed.

## Open TODOs

- Verify audio playback (especially Safari/iPad) and rendered height live in Canvas.

## Last updated

2026-09-10. v1.0: initial build. Three-tile timbre comparison, tap to play with glow and equaliser, no lede.
