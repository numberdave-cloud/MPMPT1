# BPM Tap v2

**Directory:** `bpm-tap-v2/` · **Category:** Composition

Tap-tempo counter with accuracy scoring, tap-count readout, milestone awards and reference points (a song, a genre, a real-world rhythm) near the tapped tempo. Same logic as `bpm-tap/`, reskinned to the suite's rack-card and Nixie-readout design language.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/bpm-tap-v2/

## Canvas iframe embed

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/bpm-tap-v2/" width="100%" height="470" title="BPM Tap" style="border: none;" allow="autoplay" loading="lazy"></iframe>
```

Height 470 (non-default). The card measures ~443px at 700 to 1100px wide and ~514px at 480px. Raise to 540 if the page is expected to be viewed on narrow phones.

## Build state

v2.2, 2026-09-08. Shipped as a new folder so the original `bpm-tap/` embed stays live untouched. v2.1 and v2.2 overwrote earlier v2 builds in place (git history is the undo).

## Technical notes

- Single self-contained HTML, ~18 KB. No audio, no embedded assets. Interaction is timing and visual only.
- Data pools (song brackets, genres, physical references, award tiers, joke awards) and the config constants (idle reset 2500 ms, 8-tap BPM window, 40 to 600 BPM range, accuracy thresholds 65 / 85 / 95) are unchanged from v1 and sit at the top of the script.
- Readouts use the Interval Trainer pattern: ghost "888" segment layer in flow, live digits absolutely positioned and right-aligned over it.
- TAP is a wide spacebar-shaped button in the footer row beside RESET. Rests transparent, flashes solid accent with a glow for 90 ms on hit. Spacebar also taps (repeat blocked); the button shape hints at this but it is not spelled out.
- Card max-width is 960px, wider than the 760px used by Instrument Roles, so it fills a Canvas content column rather than floating in it.
- Musical example renders title with the artist on a dimmed second line; the v1 em-dash separator is gone.

## Changes from v1

- Rack card frame, palette background, Inter 600/700 uppercase chrome. Title at ~29px top left, no subtitle.
- Tempo, accuracy and tap count on a Nixie-style readout plate. No BPM unit label.
- Added TAPS readout (new) so the 16-tap award milestones are visible.
- Award text sits under the accuracy readout on the plate (accent mono, blank until the first 16-tap milestone). No separate award panel, no footer hint.
- v2.1: all borders 2px (frame 3px) at roughly double the v2.0 opacity (panels 0.32, controls 0.6); all font sizes scaled by 1.3.
- v2.2: TAP/AWARD row removed; TAP moved to the footer row and widened; card widened to 960px.
- Example values remain uppercase monospace because the data pool is stored uppercase.

## Open TODOs

- Verify layout and readout glow live in Canvas.

## Last updated

2026-09-08. v2.2: award folded under accuracy readout, TAP moved to the footer as a wide spacebar-style button beside RESET, card widened to 960px. Embed height lowered to 470.
