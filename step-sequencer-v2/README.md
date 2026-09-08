# Step Sequencer v2 (Drums)

**Directory:** `step-sequencer-v2/` · **Category:** Composition

16-step drum grid (kick / snare / hi-hat) with Disco / Rock / Garage presets, a Steps / Count label toggle, hover-driven theory info, and Standard MIDI File export. Same interaction as `step-sequencer/`, reskinned to the suite's rack-card design language and moved from synthesised voices to sampled one-shots.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/step-sequencer-v2/

## Canvas iframe embed

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/step-sequencer-v2/" width="100%" height="600" title="Step Sequencer" style="border: none;" allow="autoplay" loading="lazy"></iframe>
```

Height 600 (default). The card measures ~562px at 900 wide, ~580 at 1100, ~697 at 480. Below ~640px viewport the grid scrolls sideways inside its panel rather than squashing. Raise to 720 if the page is expected on narrow phones.

## Build state

v2.0, 2026-09-08. Shipped as a new folder so the original `step-sequencer/` embed stays live untouched.

## Technical notes

- Single self-contained HTML, ~487 KB, almost all of it the three samples.
- Audio: three one-shot WAVs (KICK, SNARE, HAT) embedded as base64, 16-bit stereo 44.1 kHz, 0.667 s each. Decoded via `atob()` into an ArrayBuffer then `decodeAudioData`; no fetch(), because Canvas CSP blocks it on data URLs. Samples live in the `SAMPLES_B64` object at the top of the sample engine block.
- Decode is kicked off on the first pointerdown anywhere in the page and awaited before the scheduler starts, so the first bar is never silent.
- Playback: one `AudioBufferSourceNode` per hit through a per-track gain (kick 0.9, snare 0.8, hat 0.65) into a master gain. Master fader is in dB, -60 to 0, default -10.
- Scheduler: 100 ms lookahead, 25 ms interval, 16th-note steps derived from the tempo input (40 to 300 BPM). Unchanged from v1.
- MIDI export: format 0, 480 TPQ, channel 10, GM notes kick 36 / snare 38 / hat 42. Download via data URL, not createObjectURL.
- Steps / Count toggle is a two-segment group in the header (was a single relabelling button in the grid corner in v1).

## Changes from v1

- Rack card frame (960px max), accent title, 2px borders at the brighter opacities, all type scaled 1.3x, 6 to 8px corners throughout.
- Side stick track removed. Presets and MIDI export updated to three tracks.
- Synthesised drum voices replaced by the embedded samples.
- Tempo input and dB readout styled as glowing Nixie readouts; play button glows while running; fader handle is the rack-style rounded rectangle with a centre line.
- Garage hover text trimmed to drop the side-stick clause.
- Title reads STEP SEQUENCER (the " - Drums" suffix was dropped for width at the larger type size).

## Open TODOs

- Verify sample playback and layout live in Canvas.
- Confirm the trimmed Garage hover text and the title without "Drums".

## Last updated

2026-09-08. Initial v2 ship: rack-card reskin, sampled kick / snare / hat, side stick removed.
