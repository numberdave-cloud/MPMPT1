# Arcade High Scores (Interval Trainer)

Standalone, view-only arcade attract-mode leaderboard for the Interval Trainer. Reads the same shared Google Sheet board as the trainer and shows Challenge (top 10) and Survival (top 3) in a synthwave cabinet: retro sun, perspective grid floor, CRT scanlines/bloom/vignette, reigning-champ photo, blinking INSERT COIN. No audio, no writes; it only reads.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/arcade-high-scores/

## Canvas iframe embed

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/arcade-high-scores/" width="100%" height="900" title="Interval Trainer High Scores" style="border: none;" allow="autoplay" loading="lazy"></iframe>
```

Height `900` (non-default). The two boards sit side by side, so on a wide Canvas column the page is ~886px tall and 900 fits cleanly. On a narrow column or the Canvas mobile app the boards stack vertically (~1367px) and the iframe inner-scrolls to reach the champ image and coin. If your shell tends to render narrow and scrolling bothers you, switch to a scale-to-fit lock (same trick the trainer uses) so a fixed height always fits.

## Build state

**v1.1 — shipped.** Ported from the Claude Design `.dc.html` source (the `x-dc` template runtime removed) into a single self-contained HTML file. Wired to the live board with the trainer's fetch-then-JSONP fallback, demo-row fallback, attract-mode auto-refresh, and the three source palettes.

## Technical notes

- Single self-contained HTML file, ~67 KB, no libraries. Web fonts (Orbitron, Press Start 2P) load from the Google Fonts CDN.
- Reads the same `LEADERBOARD_URL` (public Apps Script read endpoint) as the trainer. `GET ?board=challenge|survival` returns `{ scores: [...] }`; a JSONP fallback (`&callback=`) covers cross-origin reads that a plain fetch refuses.
- Row mapping: `initials -> NAME`, `score -> SCORE` (both boards; Survival shows the run score, not a wave count), timestamp -> `DATE` (date portion only). The date reader accepts `date` / `ts` / `timestamp` / `time` / `when`.
- If a board comes back empty or the request is CSP-blocked, it falls back to seeded demo rows so it never renders broken. For a real display this means demo scores would show if the call is blocked — see the CSP TODO.
- Attract-mode auto-refresh every 45s (`REFRESH_MS`).
- Champ image optimised from a 2.4 MB PNG to a ~37 KB WebP at display size (170px), inlined as base64 to keep it one file.
- Palettes: `classic` (default), `synthwave`, `outrun` via `?palette=`. Scanlines off via `?scanlines=0`.
- Page background is transparent: the rounded stage is the only edge, so on the embed it reads as a floating rounded panel and takes on the Canvas page colour behind it (no hard square dark buffer). The neon glow bleeds softly onto the page.
- INSERT COIN links to `interval-trainer/` and opens in a new tab. Works as long as the Canvas iframe is not sandboxed (the standard embed above is not).

## Open decisions / TODOs

- Verify the `script.google.com` call from inside a real Canvas page (CSP) on embed day, same open test as the trainer. If Canvas blocks it, the board falls back to demo rows.
- Confirm the endpoint actually returns a timestamp/date field and its exact key name. The DATE column depends on it; the reader tries several common keys, but if the real key differs it is a one-word change.
- Champ photo is a fixed decorative image, not dynamically the current #1.

## Last updated

2026-07-17 — v1.1. Made the page background transparent so the embed shows rounded corners instead of a hard square dark edge; panel now floats on the Canvas page colour.

2026-07-16 — v1.0 shipped. First deploy of the standalone arcade leaderboard: eyebrow reads INTERVAL TRAINER, Survival labelled SCORE, champ caption is the earplugs safety line, INSERT COIN links to the trainer.
