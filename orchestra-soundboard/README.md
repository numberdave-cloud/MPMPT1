# Orchestra Soundboard

**Directory:** `orchestra-soundboard/`

A clickable soundboard of the remaining orchestral instruments (woodwind, harp, keys and tuned percussion). The student hovers a tile for a short note about the instrument, and taps it to hear a one-shot clip. The playing tile lights with a glow ring and an animated equaliser. Third widget in the orchestra group, alongside the strings and brass role matrices. Built for the movie scoring unit (MMI3).

## Live URL

https://numberdave-cloud.github.io/MPMPT1/orchestra-soundboard/

## Canvas embed

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/orchestra-soundboard/"
  width="100%"
  height="740"
  title="Orchestra Soundboard"
  style="border: none;"
  allow="autoplay"
  loading="lazy">
</iframe>
```

Height 740: the card holds a constant ~718px at full width. The readout is fixed height so it does not jump between short and long notes.

## Build state

v1.2, 2026-08-20. Category: Arranging. Copy final, twelve clips embedded and decode-verified.

## Instruments (12, grid order)

Piccolo, Flute, Oboe, Clarinet, Bassoon, Harp, Celesta, Glockenspiel, Xylophone, Marimba, Tubular Bells, Timpani.

Grouped Woodwind / Harp & keys / Percussion; family is shown in the readout, not as on-grid labels. Fixed 4-across grid so it never reflows, only scales.

## Interaction

- Hover a tile: readout shows the instrument name, its family, and a short note.
- Tap or click a tile: plays its clip once. Tile shows a glow ring and equaliser until the clip ends. Play triangle at rest.
- Keyboard: tiles are focusable, trigger on Enter or Space, and show the note on focus.

## Audio

- Twelve one-shot WAVs embedded as base64, decoded via `atob()` and played through Web Audio (`AUDIO` map keyed by instrument name).
- Each clip: 4.80s, stereo, 44.1kHz.
- Total page ~12.9MB. In the same weight bracket as the brass board, kept at full stereo by choice.
- Playback fires on tap only (browsers block sound without a gesture).

## Provenance and notes

- Visual design (tiles, readout, glow ring, equaliser) came from Claude Design. The original delivery played audio with `new Audio(src)`; that was rewired to the base64 plus Web Audio path so it survives the Canvas sandbox, with the visuals unchanged.
- Instrument copy is the user's, drawn from three texts credited in the idle readout panel: Acoustic and MIDI Orchestration for the Contemporary Composer (Pejrolo & DeRosa), The Guide to MIDI Orchestration (Gilreath), and Inside Music (Karl Haas). The source line shows when no tile is hovered and hides while a note is up. Note the roles boards credit only the first two, not Haas.
- Readout height is fixed (170px) so the card stays a constant height across all twelve notes.

## Open TODOs

- Verify audio playback and layout live in Canvas.
- Optional: add Karl Haas (Inside Music) to the strings and brass boards if the group should be fully consistent.
- Optional: downmix to mono to roughly halve the page weight if load becomes an issue.

## Last updated

2026-08-20. v1.2: three-source credit line added to the idle readout panel (Pejrolo & DeRosa, Gilreath, Karl Haas), hidden while a note shows. v1.1: body background set to transparent so the card floats on the Canvas page instead of sitting in a dark block. v1.0: initial build. Twelve-tile soundboard, hover notes, twelve embedded one-shot clips on Web Audio, glow and equaliser playing state. Design by Claude Design, playback rewired for Canvas. Shipped for the MMI3 movie scoring unit.
