# Melodic Step Sequencer v2

**Directory:** `melodic-sequencer-v2/` · **Category:** Composition

16-step monophonic melody grid over one diatonic octave (A2 to A3, white keys), played by a saw-plus-sub synth bass with a hall reverb, an optional DR-110 house beat that ducks the synth, octave shift, a randomise button, and Standard MIDI File export. Same interaction as `melodic-sequencer/`, reskinned to the suite's rack-card design language with a master fader and a hidden filter panel added.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/melodic-sequencer-v2/

## Canvas iframe embed

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/melodic-sequencer-v2/" width="100%" height="740" title="Melodic Step Sequencer" style="border: none;" allow="autoplay" loading="lazy"></iframe>
```

Height 740 (non-default). The card measures ~629px at 900 to 1100 wide in its normal state and ~725px with the hidden synth panel open; 740 covers both without a scrollbar. ~748px at 480 wide.

## Build state

v2.0, 2026-09-08. Shipped as a new folder so the original `melodic-sequencer/` embed stays live untouched.

## Controls

- Transport: PLAY / STOP and BEAT (toggles the DR-110 house pattern: kick on every beat, snare on 2 and 4, hat on the offbeat 8ths). Kick ducks the synth bus about 18 dB with an 80 ms release.
- Octave: OCT − / OCT + shift the whole grid by 12 semitones, range −1 to +2. No readout.
- Tempo: 60 to 180 BPM, default 100 (v1 defaulted to 120).
- Volume: master fader in dB, −60 to 0, default −6. 0 dB is unity. v1 had a fixed master of 0.32 (about −10 dB), so the default is roughly 4 dB louder than v1.
- Footer: CLEAR, dice (randomise: about 60% of columns get a note on a random row, one note per column), EXPORT MIDI (primary).
- Row labels audition the note on click.

## Hidden synth panel (easter egg)

Click the title letters R, E, S, O in that order: the final R of SEQUENCER, the E just before it, the S at the start of SEQUENCER, then the O in MELODIC. Any other letters clicked in between are ignored; the trail only has to end in that sequence. Two rotary dials then appear under the Volume fader and stay for the session (no persistence).

- CUTOFF: base filter cutoff, 100 Hz to 4 kHz, log scale, default 350 Hz. The filter envelope peak tracks at 18.6x base, capped at 12 kHz, matching v1's 350 to 6500 ratio.
- RESONANCE: filter Q, 0.5 to 8, default 3.
- Dials respond to vertical drag (150 px for full travel), mouse wheel, and arrow keys when focused.
- Until unlocked the synth is at the v1 values, so it sounds identical.

## Technical notes

- Single self-contained HTML, ~215 KB. Three DR-110 one-shots (24-bit mono WAV) embedded as base64 and decoded via `atob()` plus `decodeAudioData`; no fetch(). Synth fallbacks remain in code for the case where a sample fails to decode.
- Reverb: synthesised hall impulse, 2.0 s, 15 ms pre-delay. Wet send 0.28 (v1 was 0.35; backed off 20% at review).
- Scheduler: 100 ms lookahead, 25 ms interval; playhead driven by requestAnimationFrame against the AudioContext clock.
- MIDI export: format 0, 480 PPQ, one track, 4/4 meta, notes at 90% gate. Built as a data URL on mousedown / touchstart / keydown. v1 used `createObjectURL`, which fails inside the Canvas sandboxed iframe, so v1's export was likely broken live.
- Grid rows are 24px (piano-roll proportion) on a lighter #2D2722 bed with darker cells; beat columns carry a brighter left edge.

## Changes from v1

- Rack card frame (960px max), accent title, 2px borders at the brighter opacities, type scaled 1.3x, 4 to 8px corners.
- Controls laid out on a label-column grid so PLAY / BEAT and OCT − / OCT + align as one block; tempo and volume stacked on the right.
- Master volume fader added. Randomise button added. Hidden cutoff / resonance panel added.
- Default tempo 120 to 100. Reverb send 0.35 to 0.28.
- PLAY / STOP lost their ▶ / ■ glyphs; the solid-accent active state carries that.
- MIDI export switched from blob URL to data URL.

## Open TODOs

- Verify playback, export download and layout live in Canvas.
- Confirm the −6 dB default level against v1 by ear.
- No limiter on the synth bus: high resonance at low cutoff is loud by design.

## Last updated

2026-09-08. Initial v2 ship: rack-card reskin, master fader, randomise, RESO easter egg, tempo default 100.
