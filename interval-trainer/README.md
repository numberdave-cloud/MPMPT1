# Interval Trainer

Ear-training MOTE. Students hear a musical interval (two notes, harmonic or melodic) and identify it from a live list of interval buttons. Difficulty ramps through six tempo-named tiers, with Practice and scored Challenge modes plus a hidden Survival mode. Answer input is the on-screen interval list; a hidden QWERTY layout mirrors the Ableton computer-MIDI keyboard for power users.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/interval-trainer/

## Canvas iframe embed

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/interval-trainer/" width="100%" height="720" title="Interval Trainer" style="border: none;" allow="autoplay" loading="lazy"></iframe>
```

Height `720`. The device is tall because the options are anchored to the bottom, the busy tiers list all twelve intervals (two-column grid), and the frame scales up ~14% on desktop for readability. On phone widths (<600px) the scale drops to 100% and the content is a little shorter. If Canvas gives trouble, `720` is a safe fixed height.

## Build state

**v0.5 — shipped. Piano + strings + three synth voices, Practice + Challenge + Survival, leaderboard stubbed.**

Working: full audio engine, six difficulty tiers, harmonic / ascending / descending, root transposition on the top tiers, octave-reduced compound intervals, speed-bonus scoring, Practice mode, 20-question Challenge run, hidden Survival mode.

Stubbed / pending:
- **Leaderboard**: Google Sheet Apps Script endpoint not yet wired. Challenge ends on a local summary; Survival ends on a local game-over. Arcade high-score entry and the shared boards switch on once the `/exec` URL is added.
- **Survival voice**: entry currently plays a placeholder synth sting. Drops in a digitised voice sample when recorded.
- **Strings loudness**: matched by trim length, not loudness-matched to piano. May want a per-instrument gain trim after listening in context.

## Modes and controls

- **Practice**: pick difficulty (slider) and sound, unlimited-ish replays, auto-advances. Third transport button is RESET (clears score / streak).
- **Challenge**: fixed 20-question run, speed bonus, replay caps tighten with tier. Third button is END (ends the run early to the summary).
- **Survival** (hidden): easter-egg trigger — click the DIFFICULTY label 16 times within 8 seconds. Hot red palette, fastest content, single listen, reflex-speed scoring ladder, three lives, one miss costs a life, zero lives ends it. Third button is EXIT.

Keyboard (undocumented in-widget, for a separate instructions sheet): number keys 1–5 select sound; `[` / `]` move difficulty; Space replays; Enter advances; the Ableton QWERTY row (A W S E D F T G Y H U J K) answers intervals relative to A = root.

## Technical notes

- Single self-contained HTML file, ~5.1 MB, Web Audio API only, no libraries.
- Two sampled instruments (piano, strings), each nine WAVs (C and G per octave, C1–C5), mono, trimmed, base64-embedded, decoded via `atob()` + `decodeAudioData()`. Pitch by `playbackRate` from the nearest sample.
- Three synth voices (sine, saw, triangle) generated live. Sine and saw are −10 dB relative to their raw oscillator level so they sit under the piano.
- Active-voice tracker fades and cuts ringing notes (~45 ms) on every advance, replay, or sound change, so nothing bleeds across questions or instruments.
- Speed clock starts on the **second** note onset (both notes for harmonic), so melodic intervals aren't penalised for the inter-note gap. Standard tiers: under 5s = ×1.5. Survival reflex ladder: ×10 / ×8 / ×6 / ×4 / ×2 at 200 / 400 / 800 / 1600 / 3200 ms. All tier bases even so every product is a whole number.
- Auto-advance: correct answers move on after ~0.65s, wrong after ~1.9s (time to read the highlighted correct row). Next / Enter skips instantly.
- Difficulty tiers (no unison anywhere; melodic mixed in from tier 1; roots on C3 for early tiers, roaming C2–G3 on the top two): Adagio (P4 P5 P8), Andante (+M2 M3 M6), Moderato (+m3 m6 M7), Allegro (all 12), Vivace (all 12, roaming), Presto (all 12, roaming, compounds). Prestissimo is the hidden Survival tier.

## ~5 MB file size

Two sampled instruments sit near the practical base64 ceiling. A third sampled instrument (cello, or proper multisampling) should move audio to separate files fetched same-origin from GitHub Pages, which sidesteps the size limit and is a different mechanism to the data-URL `fetch()` that Canvas blocks.

## Open TODOs

- Wire the Google Sheet leaderboard endpoint (Challenge top 10, Survival top 3).
- Record and embed the digitised Survival voice sample.
- Loudness-match strings against piano.
- Decide remaining Survival easter-egg entry points (20/20 on the hardest Challenge tier was discussed as a second route).
- Optional: student instruction sheet documenting the QWERTY answer layout.

## Last updated

2026-07-14 — Initial ship. v0.5: two-column answer grid to fit a laptop screen, bottom-anchored sound/difficulty options, difficulty slider, retimed auto-advance, note-cutoff on advance/replay/sound-change, strings instrument, −10 dB on sine/saw, Survival easter egg.
