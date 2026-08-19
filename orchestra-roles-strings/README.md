# Instrument Roles [Strings]

**Directory:** `orchestra-roles-strings/`

Interactive matrix of the typical roles each string instrument plays in an orchestral texture. Rows are roles, columns are the four string instruments. A filled marker means that instrument typically fills that role; hovering or tapping it shows how. A quaver by each instrument name opens a character note and fires that instrument's one-shot sample. Built for the movie scoring unit (MMI3).

## Live URL

https://numberdave-cloud.github.io/MPMPT1/orchestra-roles-strings/

## Canvas embed

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/orchestra-roles-strings/"
  width="100%"
  height="600"
  title="Instrument Roles - Strings"
  style="border: none;"
  allow="autoplay"
  loading="lazy">
</iframe>
```

Height 600: the card measures ~590px at full width. Re-measure if Canvas shows a scrollbar.

## Build state

v1.1, 2026-08-19. Category: Arranging. Content sourced from Acoustic and MIDI Orchestration for the Contemporary Composer (Pejrolo & DeRosa), credited in-widget. Copy final, four instruments complete.

## Content model

Roles (rows): Melody, Counterline, Accompaniment, Pad, Rhythm, Pizzicato, Solo.
Instruments (columns): Violin, Viola, Cello, Double Bass.

Active roles per instrument:
- Violin: melody, counterline, pad, rhythm, solo (no accompaniment, no pizzicato)
- Viola: all seven
- Cello: all seven
- Double Bass: accompaniment, rhythm, melody, counterline, pad, pizzicato (no solo)

Each active cell carries a role tooltip; each instrument carries a character note. All four pad tooltips read "harmonic texture" (source dictation gave homophonic on cello and bass; unified to harmonic at build, one-line revert if wanted).

## Interaction

- Role markers: hover (desktop), tap (touch, taps pin the tooltip open), keyboard (tab then enter). Tooltip clamps inside the card so it does not clip in the iframe.
- Quaver notes: click only, never hover. Opening one also plays that instrument's one-shot once. Closing it again does not replay.
- Escape or click-away closes any open panel.

## Audio

- Four one-shot WAVs embedded as base64, decoded via `atob()` and played through Web Audio. Canvas blocks fetch on data URLs, so inline is the only route.
- Each sample: 4.80s, stereo, 44.1kHz. Slots keyed by instrument in the `AUDIO` object at the top of the script.
- Total page ~4.33MB with all four embedded. Heavier than a typical MOTE. If Canvas load feels slow the lever is shorter trims or mono, not external hosting.
- Sound fires on quaver-open only.

## Open TODOs

- Confirm harmonic vs homophonic on the pad tooltips (currently harmonic across all four).
- Verify audio playback and layout live in Canvas.
- Companion families (brass, woodwind, percussion) would be separate builds reusing this template.

## Last updated

2026-08-19. v1.1: instrument icons changed from eye to quaver; lede reworded to match. v1.0: initial build. Four-instrument strings matrix, per-cell role tooltips, per-instrument character notes, four embedded one-shot samples firing on note-open. Shipped for the MMI3 movie scoring unit.
