# MPMPT1

MOTEs (Mini Online Teaching Elements) for MPMPT1.

Each MOTE is a single self-contained HTML file. Web Audio API only, no external libraries. Hosted on GitHub Pages, embedded in Canvas LMS via iframe.

## Widgets

| Path | Description |
| --- | --- |
| [`hello/`](./hello) | Deployment pipeline test |
| [`mote-1/`](./mote-1) | MOTE-1 — What is a MOTE? (intro / self-referential CRT tour) |
| [`bpm-tap/`](./bpm-tap) | BPM Tap — tap-tempo counter with accuracy scoring and BPM references |
| [`step-sequencer/`](./step-sequencer) | Step Sequencer — 16-step grid with kick/snare/hat/side-stick, preset patterns (disco / rock / garage), step/count label toggle, and hover-driven theory info |
| [`mix-balance-industrial/`](./mix-balance-industrial) | Mix Balance [Industrial] — multi-channel fader mix balance exercise on an industrial stem set |
| [`mix-balance-reggae/`](./mix-balance-reggae) | Mix Balance [Reggae] — multi-channel fader mix balance exercise on a reggae stem set |

## Live URLs

- https://numberdave-cloud.github.io/MPMPT1/hello/
- https://numberdave-cloud.github.io/MPMPT1/mote-1/
- https://numberdave-cloud.github.io/MPMPT1/bpm-tap/
- https://numberdave-cloud.github.io/MPMPT1/step-sequencer/
- https://numberdave-cloud.github.io/MPMPT1/mix-balance-industrial/
- https://numberdave-cloud.github.io/MPMPT1/mix-balance-reggae/

## Embedding in Canvas

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/mote-1/"
        width="100%" height="600"
        title="MOTE-1 — What is a MOTE?"
        style="border: none;"
        allow="autoplay"
        loading="lazy"></iframe>
```
