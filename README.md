# MPMPT1

MOTEs (Mini Online Teaching Elements) for MPMPT1.

Each MOTE is a single self-contained HTML file. Web Audio API only, no external libraries. Hosted on GitHub Pages, embedded in Canvas LMS via iframe.

## Widgets

| Path | Description |
| --- | --- |
| [`hello/`](./hello) | Deployment pipeline test |
| [`mote-1/`](./mote-1) | MOTE-1 — What is a MOTE? (intro / self-referential CRT tour) |
| [`bpm-tap/`](./bpm-tap) | BPM Tap — tap-tempo counter with accuracy scoring and BPM references |

## Live URLs

- https://numberdave-cloud.github.io/MPMPT1/hello/
- https://numberdave-cloud.github.io/MPMPT1/mote-1/
- https://numberdave-cloud.github.io/MPMPT1/bpm-tap/

## Embedding in Canvas

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/mote-1/"
        width="100%" height="600"
        title="MOTE-1 — What is a MOTE?"
        style="border: none;"
        allow="autoplay"
        loading="lazy"></iframe>
```
