# Groove Maker

Interactive MOTE for building an Ableton Live groove template by ear. Students drag the 16 dots of a fixed one-bar linear hip-hop pattern earlier or later in time, hear the pocket change, then export a real `.agr` file that drops straight into Live's User Library / Grooves.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/groove-maker/

## Canvas iframe embed

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/groove-maker/?v=1"
        width="100%" height="440"
        title="Groove Maker"
        style="border: none;"
        allow="autoplay"
        loading="lazy"></iframe>
```

`440` height leaves a little breathing room above and below the widget because the design pass vertically centers content in the viewport. Bump lower (down to about 380) if you want it snugger; bump higher for more headroom.

## What it teaches

Groove and humanisation. Students have learned to program beats already; this MOTE lets them add microtiming without the piano roll's noise floor. One fixed pattern, one interaction (drag a dot), immediate audible feedback. Press play, drag the snare late, hear the pocket shift.

## Build state

v0.1, first ship. Design pass by Claude Design, audio + export engine wired in this chat. All controls functional, sample playback verified locally, `.agr` structurally verified.

Currently unconfirmed: the audible round-trip into Live. A generated `.agr` needs to be dropped into Live's User Library / Grooves and applied to a target clip to confirm it swings the notes the same way the MOTE previewed. Once that passes, mark this build audibly verified.

## The pattern

One bar of 4/4, 16 steps at 16th resolution, strictly linear:

```
Step:  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
Lane:  K Cb  H  K  S  H Cb  K Cb  S  K  K  S  K  H Cb
```

Pattern is fixed; only the timing of each hit is editable. Sourced from `NEW_HIP_HOP_MIDI.mid` (96 PPQ, format 0). One-hit-per-step is what lets the `.agr` export be unambiguous (every position holds exactly one groove point).

## The swing model

Swing is on a 25–50–75 scale where 50 is on-grid, 75 is maximally late, 25 is maximally early. This maps linearly to time offset in beats:

```
offset_beats = (swing − 50) / 25 × 0.125
```

So the extremes are ±0.125 beats, which is half a 16th-note step. Because the max offset is half a step, dots can slide up to the neighbour's gridline but never past. Do not widen the 25–75 range without adding stacking rules.

Step 0 with a negative offset (swing below 50) wraps in the exported `.agr` to `Time = time + 4`, i.e. shows up at the end of the bar. This matches how Live stores extracted grooves that push the downbeat early.

## Interactions

- **Click a dot** to select it (white ring). Click empty grid to deselect.
- **Drag** a dot horizontally to move it. Pointer capture keeps the drag alive off-dot.
- **Double-click** a dot to snap it back to swing 50.
- **Swing stepper** (− / +) adjusts the selected dot by the current Resolution step.
- **Arrow keys** ← / → do the same as the stepper.
- **Resolution** buttons (`×.1`, `×1`, `×5`) set how much each nudge moves the swing value. `×1` is default.
- **Play toggle** starts / stops the loop. Single button, glyph swaps.
- **Tempo** field: type or click ▲/▼. Clamps to 40–220 BPM.
- **Reset** zeroes all offsets back to swing 50.
- **Export Template** downloads a `.agr` named `MOTE_Groove_<timestamp>.agr`.

## Technical notes

**Audio.** Four base64-inlined WAV samples (kick, snare, hat, cowbell) decoded via `atob()` + `decodeAudioData` on first play. Loaded lazily so page paint is fast; only the play button waits on decode. Kick and Hat are 16-bit PCM (from Dave's re-uploads), Snare and Cowbell are 32-bit float (pulled from the live Quantise MOTE on GitHub because the current session only had Kick and Hat uploaded). Both formats decode identically in Web Audio; no audible difference at output.

**Scheduler.** 25 ms `setInterval` with 100 ms lookahead, per-hit swing offset applied at scheduling time (`nextTime + swingToOff(swing[s]) * (60/bpm)`). Firing queue drives the visual illumination via `requestAnimationFrame`. No manual loop-wrap catch-up (unlike the Quantise MOTE) because there's no gap in the pattern where a delayed RAF tick could miss a hit — every step has a scheduled note.

**Export pipeline.** The `NO_SWING.agr` template Dave supplied is inlined as XML in `TEMPLATE_XML`. On export, the 16 `Time` attributes on `MidiNoteEvent` elements get rewritten as `i × 0.25 + offset`, the two `<Name>` fields get set to "MOTE Groove", the XML is re-gzipped via `CompressionStream('gzip')`, and the download triggers via `data:application/octet-stream;base64,...` so it survives sandboxed Canvas iframes. `URL.createObjectURL` is deliberately avoided.

**Format.** Live 12.4 `.agr` schema. `QuantizationAmount=0`, `TimingAmount=100`, `RandomAmount=0`, `VelocityAmount=0` pass through unchanged. All 16 notes remain on a single KeyTrack at `MidiKey=36` because groove application uses only the timing offsets, not the pitch of the reference clip.

**No postMessage auto-resize.** The design pass didn't include it. Iframe height is fixed at 440. Add a `mote-resize` message and Canvas-side listener if snug fitting becomes worth the extra code.

## Open items

- **Audible round-trip verification.** Highest priority. Drop the generated `.agr` into Live, apply to a clip, confirm the offsets play as previewed.
- **Real samples for Snare / Cowbell.** Currently the samples from the Quantise MOTE. If Dave intended different samples for this MOTE, they can be swapped in (base64 replace).
- **Optional postMessage auto-resize.** Would let the iframe snap to content height instead of the fixed 440.
- **Volume control.** Original brief specified a −36 to 0 dB fader init −6. Design pass dropped it. Not in v0.1.
- **Zoom controls.** Original brief specified 1× / 2× / 4× zoom. Design pass dropped it in favour of a single fixed-width matrix. Not in v0.1.

## Files

Single self-contained `index.html` (~758 KB). All CSS, JS, four WAV samples, and the `.agr` template are inlined. No external assets beyond the Inter font from Google Fonts.

## Last updated

2026-07-29. Initial ship: design pass build with real drum samples and `.agr` export wired.
