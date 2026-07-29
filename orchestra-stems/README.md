# Orchestra Stems

**Directory:** `orchestra-stems/`
**Category:** Miscellaneous

## What it does
A three-stem listening tool for the instrument families of the orchestra: strings, brass, woodwinds. Students click an image to solo that family in isolation and read a short note about its colour and how to program it. Faders (behind a Mixer toggle) let them blend the three families.

## Live URL
https://numberdave-cloud.github.io/MPMPT1/orchestra-stems/

## Canvas embed
```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/orchestra-stems/?v=1"
  width="100%" height="700" style="border: none;"
  allow="autoplay" loading="lazy"
  title="Orchestra Stems"></iframe>
```
Height is 700 (non-default). The Mixer panel expands the layout when open; 700 fits the tallest state at full Canvas width without an internal scrollbar. Bump `?v=N` on each update to bust the cache.

## Build state
Shipped, v1. Fully working and verified (syntax + Playwright functional pass).

## How it works
- Silent on load. Play and Stop drive all three stems together (master transport). Solo only sets what is audible.
- Click an image (the whole framed tile) to exclusive-solo that family: its info text overlays the image (barely translucent, photo ghosts through), the other two dim. Click again to clear.
- Mixer button toggles the three per-family volume faders (0 to 100%). Hidden by default.
- Corner label chip on each image names the family and stays visible on top of the text overlay.
- Layout is locked to three across at every width (no vertical fold-down). Soloing grows that column (info panel appears) by design.

## Easter egg
Open Mixer, drag all three faders to 0, then press Stop, Play, Stop, Play, Stop. On the final Stop the faders fade themselves up, the images ripple left to right into negative (CSS `invert(1)`), and reverse mode arms. The next Play runs all three stems backwards. Persists until the widget reloads.

## Technical notes
- Audio: three OGG Vorbis stems, base64-embedded, decoded via `atob()` then `decodeAudioData` (no `fetch()` / no `createObjectURL`, so Canvas CSP safe).
- Loop period ~19.2s. Strings and woodwinds are exactly 19.200s; brass is 19.196s (about 4ms shorter), so over very long unbroken runs brass will phase slightly against the others. Inaudible for classroom use on sustained beds. All three are started at a single common start time with `loop=true`.
- Reverse buffers are built once at init by flipping each channel's sample data. A reversed copy of a gapless loop stays gapless.
- Vertical faders use `writing-mode: vertical-lr` (the old `-webkit-appearance: slider-vertical` was removed in Chrome 121 and is not used).
- Images: three PNGs, base64-embedded. Each sits in a matte frame (5% padding) with its own inner border.
- Total file ~7.2MB (all audio and images inline). Single self-contained HTML.

## Open TODOs
- None outstanding. Optional future tweak: reserve the info-panel space so the soloed column does not grow (currently spec-accurate: it grows).

## Last updated
2026-07-29: Initial ship.
