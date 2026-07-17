# Interval Trainer

Ear-training MOTE. Students hear a musical interval (two notes, harmonic or melodic) and identify it from a live list of interval buttons. Difficulty ramps through six tempo-named tiers, with Practice and scored Challenge modes plus a hidden Survival mode and a shared arcade leaderboard. Answer input is the on-screen interval list; a hidden QWERTY layout mirrors the Ableton computer-MIDI keyboard for power users.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/interval-trainer/

## Canvas iframe embed

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/interval-trainer/" width="100%" height="800" title="Interval Trainer" style="border: none;" allow="autoplay" loading="lazy"></iframe>
```

Height `800`. The trainer sits in a rounded black bumper on a transparent surround, so it floats as a contained card on the Canvas page rather than filling the column width. The tallest state (Practice on the hardest tier, ~788px) drives the height. The device scales ~14% on desktop and drops to 100% below 600px so it still fits a phone. If you previously embedded at `760` or `720`, bump it to `800`.

## Build state

**v0.8 — shipped. Piano + strings + two synth voices, Practice + Challenge + Survival, shared leaderboard live, floating bumper frame.**

Working: full audio engine, six difficulty tiers, harmonic / ascending / descending, root transposition on the top tiers, octave-reduced compounds, speed-bonus scoring, Practice mode with direction toggles, 20-question Challenge run, hidden Survival mode, arcade high-score entry, shared Challenge (top 10) and Survival (top 3) leaderboards backed by a Google Sheet.

Pending:
- **Guitar**: chip is present but disabled, awaiting guitar samples (same format as piano/strings).
- **Survival voice**: entry plays a placeholder synth sting; a digitised voice sample drops in when recorded.
- **Strings loudness**: matched by trim length, not loudness-matched to piano.
- **Standalone leaderboard**: shipped as a separate arcade-styled view-only scoreboard reading the same sheet. Live at `../arcade-high-scores/` (https://numberdave-cloud.github.io/MPMPT1/arcade-high-scores/).

## Modes and controls

- **Practice**: pick difficulty (slider), sound, and direction (Ascending / Descending / Harmonic toggles, at least one on — these override the tier's built-in direction). Auto-advances. Third transport button is RESET.
- **Challenge**: fixed 20-question run, speed bonus, replay caps tighten with tier. Third button is END. Cracking the top 10 opens the initials entry.
- **Survival** (hidden): easter-egg trigger — click the DIFFICULTY label 16 times within 8 seconds. Hot red palette, fastest content, single listen, reflex-speed scoring ladder, three lives, one miss costs a life, zero lives ends it. Top 3 board. Third button is EXIT.

Difficulty tiers (no unison anywhere; melodic mixed in from tier 1; C3 root on tiers 1-4, roaming C2-G3 on tiers 5-6; compounds on tier 6):

| # | Name | Intervals | Directions | Root | Replays | Base |
|---|------|-----------|-----------|------|---------|------|
| 1 | Adagio | P4 P5 P8 | harm, asc | C3 | inf | 10 |
| 2 | Andante | +M2 M3 M6 | +desc | C3 | inf | 20 |
| 3 | Moderato | +m3 m6 M7 | all | C3 | 3 | 30 |
| 4 | Allegro | all 12 | all | C3 | 2 | 50 |
| 5 | Vivace | all 12 | all | roams | 2 | 70 |
| 6 | Presto | all 12 +compounds | all | roams | 1 | 100 |

Keyboard (undocumented in-widget, for a separate instructions sheet): number keys 1-5 select sound; `[` / `]` move difficulty; Space replays; Enter advances; the Ableton QWERTY row (A W S E D F T G Y H U J K) answers intervals relative to A = root. During initials entry: type directly, or the arrows to spin a letter, Enter to confirm.

## Leaderboard

Backed by a Google Apps Script Web App bound to a Sheet (owner-managed). The endpoint URL lives in the `LEADERBOARD_URL` constant near the top of the script in `index.html` — it is a public read/append endpoint by design, not a secret. GET returns the top N per board (JSONP fallback for cross-origin reads); POST appends one sanitised row. If `LEADERBOARD_URL` is blanked, the board falls back to seeded local demo scores.

**Known test:** the outbound call must still be verified from inside a real Canvas page — Canvas CSP is stricter than a plain browser tab and could block the request to `script.google.com`. The widget degrades gracefully if blocked (board runs empty, entry still works, nothing breaks), but writes/reads would not persist. Test on the day it's embedded.

## Technical notes

- Single self-contained HTML file, ~5.1 MB, Web Audio API only, no libraries.
- Two sampled instruments (piano, strings), each nine WAVs (C and G per octave, C1-C5), mono, trimmed, base64-embedded, decoded via `atob()` + `decodeAudioData()`. Pitch by `playbackRate` from the nearest sample.
- Two synth voices (sine, saw) generated live; sine and saw are -10 dB relative to raw oscillator level to sit under the piano.
- Active-voice tracker fades and cuts ringing notes (~45 ms) on every advance, replay, or sound change.
- Speed clock starts on the second note onset. Standard tiers: under 5s = x1.5. Survival reflex ladder: x10/x8/x6/x4/x2 at 200/400/800/1600/3200 ms. Even bases give whole-number scores.
- Auto-advance: correct ~0.65s, wrong ~1.9s. Next / Enter skips.

## ~5 MB file size

Two sampled instruments sit near the practical base64 ceiling. Adding a third (guitar) should move audio to separate files fetched same-origin from GitHub Pages, sidestepping the size limit — a different mechanism to the data-URL `fetch()` Canvas blocks.

## Open TODOs

- Verify the leaderboard call from inside real Canvas (CSP).
- Add guitar samples and wire the Guitar instrument.
- Record and embed the Survival voice sample.
- Loudness-match strings against piano.
- Second Survival easter-egg entry point (20/20 on the hardest Challenge tier was discussed).
- Student instruction sheet documenting the QWERTY answer layout.

## Last updated

2026-07-17 — v0.8.1 shipped. Removed the outer drop shadow behind the bumper (it was casting onto the Canvas page); the bumper now sits flat with only its own inset edge. No other changes.
