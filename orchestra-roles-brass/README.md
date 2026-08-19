# Instrument Roles [Brass]

**Directory:** `orchestra-roles-brass/`

Interactive matrix of the typical roles each brass instrument plays in an orchestral texture. Sibling to the strings matrix, same engine. Rows are roles, columns are the five brass instruments. A filled marker means that instrument typically fills that role; hovering or tapping it shows how. A quaver by each instrument name opens a character note and fires that instrument's one-shot sample. Built for the movie scoring unit (MMI3).

## Live URL

https://numberdave-cloud.github.io/MPMPT1/orchestra-roles-brass/

## Canvas embed

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/orchestra-roles-brass/"
  width="100%"
  height="620"
  title="Instrument Roles - Brass"
  style="border: none;"
  allow="autoplay"
  loading="lazy">
</iframe>
```

Height 620: the card measures ~596px at full width, a little taller than the strings matrix because of the extra Counterline and Bass rows. Re-measure if Canvas shows a scrollbar.

## Build state

v1.0, 2026-08-19. Category: Arranging. Copy final, five instruments complete, audio embedded.

## Content model

Roles (rows): Melody, Counterline, Accompaniment, Pad, Rhythm, Bass, Solo.
Instruments (columns): French Horn, Trumpet, Tenor Trombone, Bass Trombone, Tuba (score order).

Active roles per instrument:
- French Horn: melody, counterline, accompaniment, pad, rhythm, solo
- Trumpet: melody, counterline, accompaniment, pad, rhythm, solo
- Tenor Trombone: melody, counterline, accompaniment, pad, rhythm, solo
- Bass Trombone: pad, bass
- Tuba: melody, accompaniment, rhythm, bass

Each active cell carries a role tooltip; each instrument carries a character note behind its quaver.

## Sources and fact-check

Content drawn from two texts, both credited in-widget: Acoustic and MIDI Orchestration for the Contemporary Composer (Pejrolo & DeRosa) and The Guide to MIDI Orchestration (Gilreath). The role assignments were then cross-checked against general orchestration references. Adjustments made from that check:
- Added: Trumpet Rhythm, Tuba Rhythm, Tenor Trombone Counterline, Tenor Trombone Solo (all standard practice the two books did not state).
- Dropped: Bass Trombone Melody (bass trombone reads as harmonic and bass reinforcement, not a melodic voice).
- Reworded: the Tuba Melody note so the "awkward, use sparingly" caution attaches to the high register, since bass-register melody is idiomatic.
- Skipped as too soft: Tuba Pad, Tuba Solo, Bass Trombone Accompaniment.

The Tenor Trombone Solo tooltip anchors on Ravel's Bolero as the reference example.

## Interaction

- Role markers: hover (desktop), tap (touch, taps pin the tooltip open), keyboard (tab then enter). Tooltip clamps inside the card.
- Quaver notes: click only, never hover. Opening one also plays that instrument's one-shot once. Closing it again does not replay.
- Escape or click-away closes any open panel.

## Audio

- Five one-shot WAVs embedded as base64, decoded via `atob()` and played through Web Audio. Canvas blocks fetch on data URLs, so inline is the only route.
- Each sample: 10.80s, stereo, 44.1kHz. Slots keyed by instrument in the `AUDIO` object.
- Total page ~12.1MB with all five embedded. This is a deliberate call: kept at full stereo length rather than trimmed or downmixed to mono. Heavier first load, especially on phones. If it ever needs slimming, mono roughly halves it and cropping the tails shrinks it further.
- Sound fires on quaver-open only.

## Open TODOs

- Verify audio playback and layout live in Canvas.
- If load weight becomes an issue, downmix to mono or trim the samples.
- Companion families (woodwind, percussion) would be separate builds reusing this template.

## Last updated

2026-08-19. v1.0: initial build. Five-instrument brass matrix, per-cell role tooltips, per-instrument character notes, five embedded one-shot samples firing on quaver-open. Fact-checked against orchestration references. Shipped for the MMI3 movie scoring unit.
