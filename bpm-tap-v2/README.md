# BPM Tap v2

**Directory:** `bpm-tap-v2/` · **Category:** Composition

Tap-tempo counter with accuracy scoring, tap-count readout, milestone awards and reference points (a song, a genre, a real-world rhythm) near the tapped tempo. Same logic as `bpm-tap/`, reskinned to the suite's rack-card and Nixie-readout design language.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/bpm-tap-v2/

## Canvas iframe embed

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/bpm-tap-v2/" width="100%" height="520" title="BPM Tap" style="border: none;" allow="autoplay" loading="lazy"></iframe>
```

Height 520 (non-default). The card measures ~482px at 700 to 900px wide and ~649px at 480px. Raise to 680 if the page is expected to be viewed on narrow phones.

## Build state

v2.0, 2026-09-08. Shipped as a new folder so the original `bpm-tap/` embed stays live untouched.

## Technical notes

- Single self-contained HTML, ~19 KB. No audio, no embedded assets. Interaction is timing and visual only.
- Data pools (song brackets, genres, physical references, award tiers, joke awards) and the config constants (idle reset 2500 ms, 8-tap BPM window, 40 to 600 BPM range, accuracy thresholds 65 / 85 / 95) are unchanged from v1 and sit at the top of the script.
- Readouts use the Interval Trainer pattern: ghost "888" segment layer in flow, live digits absolutely positioned and right-aligned over it.
- TAP button rests transparent and flashes solid accent with a glow for 90 ms on hit. Spacebar also taps (repeat blocked).
- Musical example renders title with the artist on a dimmed second line; the v1 em-dash separator is gone.

## Changes from v1

- Rack card frame, palette background, Inter 600/700 uppercase chrome.
- Tempo, accuracy and tap count on a Nixie-style readout plate.
- Added TAPS readout (new) so the 16-tap award milestones are visible.
- Award panel with empty-state copy; footer hint for spacebar and idle reset.
- Example values remain uppercase monospace because the data pool is stored uppercase.

## Open TODOs

- Verify layout and readout glow live in Canvas.
- Student-facing copy (award empty state, footer hint, subtitle) was drafted at build; confirm or rewrite.

## Last updated

2026-09-08. Initial v2 ship: design-consistency reskin of BPM Tap.
