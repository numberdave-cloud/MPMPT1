# String Articulations

**Directory:** `string-articulations/`

A soundboard of the four core string articulations. The student hovers a tile for a short note plus a MIDI production tip, and taps it to hear the articulation played. Same engine as the Orchestra Soundboard, four tiles instead of twelve. Built for the movie scoring unit (MMI3).

## Live URL

https://numberdave-cloud.github.io/MPMPT1/string-articulations/

## Canvas embed

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/string-articulations/"
  width="100%"
  height="560"
  title="String Articulations"
  style="border: none;"
  allow="autoplay"
  loading="lazy">
</iframe>
```

Height 560: the card holds a constant ~542px at full width. The readout is fixed height (sized to the tallest note-plus-tip, pizzicato) so it does not jump between tiles.

## Build state

v1.0, 2026-08-20. Category: Arranging. Copy final, four clips embedded and decode-verified.

## Tiles (grid order)

Legato, Pizzicato, Spiccato, Tremolo. Single row of four; no family label (this is not a family board).

## Interaction

- Hover a tile: readout shows the articulation name, a short note, and a MIDI tip callout (accent left border, "MIDI tip" label) where one exists.
- Tap or click a tile: plays its clip once. Tile shows the glow ring and equaliser until the clip ends.
- Idle: readout shows the prompt and a two-source credit line.
- Keyboard: tiles focusable, trigger on Enter or Space, show the note on focus.

## Audio

- Four one-shot WAVs embedded as base64, decoded via `atob()` and played through Web Audio (`AUDIO` map keyed by articulation name).
- Durations: Legato 8.0s, Pizzicato 6.75s, Spiccato 4.0s, Tremolo 10.0s. Stereo, 44.1kHz.
- Total page ~6.5MB, lighter than the twelve-tile soundboard.
- Playback fires on tap only.

## Copy and sources

- Notes were trimmed and synthesised by Claude from the user's dictated dump of the two orchestration texts, then approved by the user. MIDI production tips are kept as accent callouts on legato (upbow velocity), pizzicato (realistic sample banks) and spiccato (alternating-bow simulation). Tremolo has no tip.
- Idle source line credits the two books only: Acoustic and MIDI Orchestration for the Contemporary Composer (Pejrolo & DeRosa) and The Guide to MIDI Orchestration (Gilreath). No Karl Haas on this board.
- House-style note: no colons in the note or tip copy, by request. The "Sources" line keeps its colon by exception.

## Open TODOs

- Verify audio playback and layout live in Canvas.
- The dictated detache material was set aside (no tile). A fifth tile or a legato contrast line could use it later.
- Optional: downmix to mono to slim the page if needed.

## Last updated

2026-08-20. v1.0: initial build. Four-tile string articulations board, hover notes with MIDI tip callouts, four embedded one-shot clips on Web Audio, glow and equaliser playing state. Engine from the Orchestra Soundboard. Shipped for the MMI3 movie scoring unit.
