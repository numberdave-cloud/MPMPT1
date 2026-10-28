# Bass Step Sequencer

**Directory:** `bass-sequencer/` · **Category:** Composition

A one-bar bass programming sandbox for the basslines unit. 16 steps, one octave of the A minor scale (white keys, A2 up to A3), monophonic synth bass. Built from `melodic-sequencer-v2/` and reskinned to the black Basic DAW card. Sits under the "Rhythm Section" bass-programming page.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/bass-sequencer/

## Canvas iframe embed

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/bass-sequencer/" title="Bass Step Sequencer" width="100%" height="920" style="border: none;" allow="autoplay" loading="lazy"></iframe>
```

Height 920 (non-default). The card measures ~871px at desktop widths (~907px body incl. padding, ~913px with a long info blurb showing); 920 covers it with headroom. At phone width (~480px) the card is ~1052–1123px, so phones may show a small inner scrollbar.

## Build state

v1.1, updated 2026-10-29 (final preset copy, placeholder note removed). v1.0 shipped 2026-10-28. Not yet verified in Canvas.

## Controls

- Transport: PLAY / STOP, and BEAT (toggles a house drum pattern that ducks the bass).
- Octave: OCT − / OCT + shift the whole grid ±1 octave (range −1 to +2).
- Tempo: 60–180 BPM, default 100.
- Volume: master fader, −60 to 0 dB, default −6.
- Rhythm Presets: load a ready-made bassline onto the grid. Seven presets (see below).
- Footer: CLEAR, randomise (dice), EXPORT MIDI (format 0 SMF, data URL).
- Row labels audition the note on click. Grid is monophonic (one note per column).
- Info panel: hover or tap any control for a plain-language explanation.

## Rhythm presets

| Name | Pattern (16-step grid, row A2 = low root unless noted) |
| --- | --- |
| Steady 8ths | root on every 8th: steps 0,2,4,6,8,10,12,14 |
| Octave Jumps | root on beats, A3 (octave) on offbeats |
| Tresillo | 3-3-2 cross-rhythm: steps 0,3,6,8,11,14 |
| Son Clave (3-2) | steps 0,3,6,10,12 |
| Offbeat | low A on the offbeats only: steps 2,6,10,14 |
| Psytrance | every 16th except the beats: all steps bar 0,4,8,12 |
| Giorgio | D D D D, A(low) A, C C, repeated ×2 across the bar |

All seven patterns are final (Dave confirmed 2026-10-29); the "placeholder patterns" header note has been removed. The info-panel copy for each preset is Dave's own words, locked 2026-10-29. To change a pattern, edit the `notes` arrays in the `PRESETS` array (each entry is `{step, row}`; rows are 0=A3 top … 7=A2 bottom); the preset's `info` string holds its copy.

## Synth engine (hidden easter egg)

Click the title letters **B-A-S-S** in order to reveal the full synth voice panel. All controls are live; there is no copy/readout (removed at Dave's request). Controls: oscillator waveform (Saw/Square/Tri), Sub level, Cutoff, Resonance, Env Amt (filter envelope depth), Flt Atk, Flt Rel, Amp Atk, Amp Rel, Reverb.

**Default patch (dialled in by Dave, baked in as the boot sound):**

- wave: Square
- sub level: 0.92
- cutoff: 213 Hz
- resonance Q: 6.0
- env amount: 3.7× (peak ~781 Hz)
- filter attack: 8 ms
- filter release: 117 ms
- amp attack: 15 ms
- amp release: 742 ms
- reverb: 0.18

The defaults live in the `let synth*` declarations near the top of the script; each dial's start position is derived from those variables, and `wetGain.gain.value` is initialised to the reverb default, so there is one source of truth.

## Technical notes

- Single self-contained HTML, ~236 KB. Three DR-110 one-shots (24-bit mono WAV) embedded as base64, decoded via `atob()` + `decodeAudioData`; no fetch() (Canvas CSP). Synth-drum fallbacks remain in code.
- Voice: main osc (waveform selectable) + sine sub an octave below → lowpass with filter envelope → amp envelope → synth bus → dry + hall reverb send → sidechain duck → master.
- Reverb: synthesised hall impulse, 2.0 s, 15 ms pre-delay.
- Scheduler: 100 ms lookahead, 25 ms interval; playhead on requestAnimationFrame against the AudioContext clock.
- MIDI export: format 0, 480 PPQ, 4/4, notes at 90% gate, built as a data URL on mousedown/touchstart/keydown (blob URLs fail in the Canvas sandbox).
- Spacebar is not bound here (base had no binding); PLAY/STOP via the button.
- Removed from the melodic-sequencer-v2 base: the RESO easter egg's old secret (now B-A-S-S), and there is no DAW term toggle (removed at Dave's request).

## Open decisions / TODOs

- Verify playback, MIDI export download and embed height live in Canvas.
- Preset patterns and preset copy are final. Control info-panel copy (Play, Beat, Tempo, etc.) is still Claude's draft, pending Dave's approval.
- Button labels still read "Steady 8ths", "Octave Jumps", "Son Clave (3-2)"; Dave's copy calls these "8th note", "octave", "Son clave". Rename not yet requested.
- Safari/iOS OGG/WAV decoding untested.

## Last updated

2026-10-29 — v1.1. Preset info-panel copy replaced with Dave's final words for all seven presets; all patterns confirmed final; "placeholder patterns — final MIDI pending" note removed from the preset row.

2026-10-28 — v1.0 initial ship. Reskin of melodic-sequencer-v2 to the black Basic DAW card; added rhythm presets (incl. Offbeat, Psytrance, Giorgio to spec), full synth-engine easter egg with Dave's baked-in default patch; DAW toggle and copy/readout removed.
