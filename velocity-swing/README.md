# Velocity + Swing

Directory: `velocity-swing/`
Category: Composition

A four-lane drum sequencer (kick, snare, hat, cowbell) for teaching how velocity and 16th-note swing shape a groove. Simple mode locks the beat and lets students change only the velocities; Advanced mode opens the beat up for reprogramming along with continuous swing and a free tempo. A Bypass button plays the beat flat (every note medium, no swing) for an A/B against the full groove, and the pattern can be exported as a MIDI file with swing and velocity baked in.

Live URL: https://numberdave-cloud.github.io/MPMPT1/velocity-swing/

## Canvas embed

Height 580 (non-default). The rack is laid out at a fixed 900 px and then scaled with a CSS transform to fit the width it is given, so the 16-step grid keeps its proportions instead of cramping or cropping on a narrow column. At full size it is about 539 px tall, so 580 clears it with margin; on a narrower column it scales down and sits shorter, leaving a little space below. The embed width stays 100%.

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/velocity-swing/" title="Velocity + Swing" width="100%" height="580" style="border: none;" allow="autoplay" loading="lazy"></iframe>
```

## Build state

v1.1, shipped 2026-10-27. Not yet verified in Canvas.

## How it works

- One bar, 16 steps, four lanes. Linear in both modes: one drum per step, so a new note replaces whatever shared that step.
- Velocity has three levels (weak / medium / strong) shown by note height and brightness, and mapped to playback gain (0.3 / 0.62 / 1.0, times a per-lane trim).
- Simple mode: velocity-only. Clicking an existing note cycles medium, strong, weak. Empty steps are inert and Clear is disabled. Swing is detented to 5% steps (50 to 70) and tempo is locked.
- Advanced mode: full edit. Clicking cycles medium, strong, off, weak, and empty steps accept new notes. Swing is continuous (50 to 75) and tempo is free (70 to 160).
- Default tempo 90. Mode switches retain the tempo.
- Bypass forces medium velocity and 50% swing on playback and audition, dims the swing knob and velocity key, and runs the playhead straight. It does not alter the stored pattern.

## Technical notes

- Four drum one-shots are 16-bit WAV, base64-embedded and decoded with `atob()` (not `fetch()`, which Canvas CSP blocks). Samples lifted from `quantise/`.
- Playback uses a lookahead scheduler (100 ms window, 25 ms tick) firing one-shots at computed times, not `loop=true`. Swing delays the second 16th of each pair: the step's offset is `pair*eighth + swingFrac*eighth` for the second of the pair, with `swingFrac` 0.50 to 0.75.
- MIDI export writes a Type 0 SMF at 480 PPQ, channel 10, GM drum map (kick 36, snare 38, hat 42, cowbell 56). Swing is written into the note tick positions and velocity into MIDI velocity (weak 50, medium 85, strong 118). Notes are a 16th long, trimmed only where a swung note would overlap the next hit of the same drum. Export always writes the full groove and ignores Bypass. Delivered as a `data:audio/midi;base64` download via an `<a download>` click (not `createObjectURL`, which Canvas blocks). At swing 50 the notes sit straight on the 16th grid by design.

## Open decisions / TODOs

- Info-panel copy: there is no explanatory panel; the device teaches by ear and hand. The grey hint line is Claude's draft and is awaiting DJ's sign-off or rewrite.
- Velocity cycle order (medium, strong, off, weak) puts "off" inside the loop, so an off step goes to weak on the next click rather than clearing for good. Confirmed as intended.
- Not yet verified in Canvas.

## Last updated

2026-10-27 — v1.1: rack now scales with a transform to fit the page width while holding its ratio (the fixed 900 px layout was cropping narrow Canvas columns).
2026-10-27 — initial ship (v1.0).
