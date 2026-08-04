# Compression

Folder: `compression-explorer/` · Category: Mixing

All-controls-live compressor sandbox. A student plays a loop through a real, in-browser compressor and hears what attack, release, ratio and threshold each do, with a live VU-style gain-reduction meter, an A/B bypass, and automatic level matching so they hear character rather than a change in volume.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/compression-explorer/

## Canvas iframe embed

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/compression-explorer/?v=2"
        width="100%" height="620"
        title="Compression"
        style="border: none;"
        allow="autoplay"
        loading="lazy"></iframe>
```

Height is 620 rather than the usual 600 because the enlarged gain-reduction meter makes the device roughly 600px tall at full size. The device has a fixed design width (about 604px) and scales down as a single unit below that, so on a narrower Canvas column it shrinks and leaves some blank space beneath, which you can reclaim by lowering the iframe height. Give it at least ~600px of width to show at full size.

## What it teaches

The sound of dynamic range compression, one parameter at a time, on real material. Students have watched a lecture covering the controls; this lets them move each one and hear the result immediately, no DAW launch required. It is the all-live version. The four single-parameter MOTEs (attack, release, threshold, ratio) are intended to be built from this same faceplate with the other three knobs locked.

## Build state

v1.1. Custom DSP engine, four switchable sources, reversed threshold knob, grouped source selector, enlarged meter, small output volume fader. Page background is transparent (floats on the Canvas white) and the device now sits in a near-black rounded bezel frame with a 2px screen border, matching the Tuning Practice treatment. All controls functional, level matching and no-clip behaviour verified in headless Chromium. Classroom testing not yet done.

## The engine

Hand-written per-sample compressor in a `ScriptProcessorNode` (buffer 512), not the browser's `DynamicsCompressorNode`. The built-in node carries about 6ms of fixed look-ahead that swallows any attack faster than roughly 5ms, so 0.1ms and 1ms sound identical on transients and the attack control cannot teach attack. There is no property to disable that look-ahead (the node exposes only threshold, knee, ratio, attack, release).

The custom engine is a feed-forward peak design: linked-stereo peak detection, a log-domain gain computer with soft-knee interpolation (Giannoulis, Massberg and Reiss, JAES 2012), and real attack/release one-pole coefficients (`exp(-1/(tau*sr))`). No look-ahead, so a slow attack genuinely lets the transient through. Verified: one millisecond after a hit, 0.1ms attack has pulled 22.8dB of reduction while 1ms has pulled 14.4 and 10ms only 2.2, a monotonic, audible spread the built-in node could not produce.

## Controls (detented)

- Attack: 0.1 / 1 / 10 / 100 ms
- Release: 0.1 / 0.3 / 0.6 / 1 s
- Ratio: 2 / 4 / 10 / 20 :1
- Threshold: 0 / -6 / -12 / -18 / -24 / -30 dB. Knob is reversed to mirror Ableton's Glue: 0dB fully clockwise, -30 fully anticlockwise. Opens at 0dB (no compression).
- Knee: ratio-dependent, SSL-style. Soft at 2:1 (about 10dB wide), hardening to near-hard at 20:1.

Knob interaction: click selects (no jump), arrow keys step, click-drag steps, scroll is accumulated so a light flick moves one detent.

## Level handling

- Auto makeup by calibration: for the current source and settings the engine runs the same DSP over the whole buffer in plain JS, measures the output loudness, and sets a single fixed makeup that lands it on the dry level. Cached per setting. This is deterministic, preserves the loop's own dynamics, and is immune to any hidden makeup the node might have applied (which is why threshold-distance and formula-based makeup were abandoned).
- Output volume fader: post-everything, independent of the compressor. Small fader in the right margin. Mute at the bottom, 0dB at the top, default -6 which reproduces the calibrated output level. Custom pointer fader (the browser's vertical `<input range>` was jumpy and misaligned).
- Safety ceiling: a WaveShaper soft-clip at -1 dBFS after the fader, oversample off, so output can never exceed -1 dBFS regardless of settings. At the default and normal use it never engages.

## Audio

Four OGG loops: drums, bass, guitars, vox. About 8.8s each, stereo 44.1k, peaks around -5 dBFS. base64-embedded and decoded via `atob()` (Canvas CSP blocks `fetch()` on data URLs). Single self-contained file, roughly 2MB.

## Technical notes and quirks

- `ScriptProcessorNode` is deprecated but works everywhere and needs nothing external. AudioWorklet would be the modern choice but needs a separate module file loaded by URL, which fights Canvas CSP and the `createObjectURL` block, so it is not worth it for one compressor on a loop.
- The meter reads the engine's own reduction value, so the needle is exactly what the DSP is doing, with no inherited look-ahead artefact. Needle rises fast and falls slow like a real GR meter.
- Bypass crossfades dry and processed inside the engine over about 20ms, so it is click-free and jump-free, and both states share the engine's latency (an earlier version routed dry around the engine and the latency mismatch caused an audible hiccup).
- The whole device scales as one unit via a CSS transform on a `#scaler` wrapper driven by a ResizeObserver, so narrowing the width shrinks everything proportionally instead of reflowing.

## Open decisions and TODO

- Build the four single-parameter MOTEs from this faceplate (a `LIVE` flag already exists to lock the fixed knobs).
- SSL character is approximated. The feedback detection topology, the program-dependent Auto release, and VCA colour are not modelled. A dedicated research pass on the SSL bus compressor is planned for a later character-comparison MOTE (1176 vs LA-2A vs SSL), where measured literature will matter.
- Confirm behaviour and levels on real classroom monitoring.

## Last updated

2026-08-04. v1.1: transparent page background so it presents on Canvas white, and a near-black rounded bezel frame around the screen (copied from Tuning Practice). Embed bumped to ?v=2.
