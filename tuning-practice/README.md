# Tuning Practice

Ear-training MOTE. Two notes play in sequence and the student judges whether the **second** note is sharp, flat or in tune relative to where it should sit. Detune shrinks across ten tiers from 40-50 cents down to 2-3 cents. Practice, scored Challenge and a hidden Survival mode. Design and audio engine are cannibalised from Interval Trainer.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/tuning-practice/

## Canvas iframe embed

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/tuning-practice/" width="100%" height="800" title="Tuning Practice" style="border: none;" allow="autoplay" loading="lazy"></iframe>
```

Height `800`, matching Interval Trainer. Same rounded black bumper on a transparent surround, so it floats as a contained card rather than filling the column. Tallest measured state is 685px; the device scales ~14% on desktop and drops to 100% below 600px for phones.

## Build state

**v1.0 — shipped.** Ten tiers, four instruments, four intervals, Practice + Challenge + Survival, shuffle-bag randomiser. No leaderboard.

## Learning outcome

Student identifies a second note as sharp, flat or in tune against a reference note played immediately before it, at progressively finer resolution.

## Audio

| Element | Value |
| --- | --- |
| Note 1 | 1000 ms, 100 ms fade at the tail |
| Gap | 150 ms silence |
| Note 2 | 1000 ms, 100 ms fade at the tail |
| Total | 2250 ms |

Melodic only. Note 1 is hard-stopped before note 2 begins: verified at RMS 0.0000000 through the gap on all four voices. No overlap means no beating, so the task is pitch memory rather than roughness detection.

Detune is applied to note 2 only, as a fractional MIDI offset (`midi + cents/100`). Sampled voices resolve that to `playbackRate = 2^((midiFrac - sampleMidi)/12)`; synth voices to `midiToFreq(midiFrac)`. Measured output accuracy is within 0.001 cents at every tier including the 2-cent floor.

Instruments: piano and strings (9 WAVs each, C1-C5, base64 + `atob()`), sine and saw oscillators. Same banks as Interval Trainer.

## Tiers

| Tier | Cents | Tier | Cents |
| --- | --- | --- | --- |
| 1 | 40-50 | 6 | 9-12 |
| 2 | 30-40 | 7 | 6-9 |
| 3 | 22-30 | 8 | 4-6 |
| 4 | 16-22 | 9 | 3-4.5 |
| 5 | 12-16 | 10 | 2-3 |

Magnitude is drawn continuously within the band.

- **Root:** fixed C3 on tiers 1-7, roams C3-G3 (MIDI 48-55) on tiers 8-10.
- **Direction:** ascending only on tiers 1-6, ascending and descending on tiers 7-10. Unison ignores direction.
- **Intervals:** unison, octave, perfect 4th, perfect 5th. Available at every tier.

`ROAM_LO` was originally 36 (C2) and was raised to 48. Two cents at C2 is 0.076 Hz against 0.227 Hz at G3, so the bottom of the old range was asking students to resolve less than a tenth of a Hz and made fine tiers feel broken rather than hard.

## Randomiser

Independent uniform draws clump badly: with two answers and two intervals, five identical answers in a row turns up roughly once every 32 questions. Each axis instead deals from a shuffled bag holding two of every value, refilled when empty, with a hard run cap of 2 blocking any value that just appeared twice.

Separate bags for answer, interval and melodic direction. Because answer and interval are capped independently, an identical question cannot appear three times running, and a doubled question forces both axes to switch so it cannot immediately bounce back. Roaming roots never repeat consecutively.

Answer bag is `[sharp, sharp, flat, flat, intune]` when In Tune is offered (40/40/20) and `[sharp, flat]` when it is not. Bags reset on mode change, tier change, interval toggle and In Tune toggle.

Verified over 4000 questions per configuration: longest run 2 on every axis, distributions balanced to within 1%.

## Modes

**Practice.** Difficulty slider 1-10. Instrument, interval and In Tune all changeable at any time. Unlimited replays, auto-advance, no scoring. Third transport button is RESET.

**Challenge.** Setup screen locks instrument, interval and In Tune for the whole run. Starts at tier 1. Two correct in a row climbs a tier; a wrong answer resets progress toward the next tier but does not end the run; three wrong answers total ends it; clearing tier 10 completes it.

Replay caps by tier: unlimited on 1-3, three on 4-6, two on 7-8, one on 9-10. A replay re-fires the identical pair, it does not generate a new one.

Score per correct answer is `tier x 10 x streak multiplier`. Streak counts correct answers in a row across the whole run and survives promotion; a wrong answer resets it to zero.

| Streak | Multiplier | Streak | Multiplier |
| --- | --- | --- | --- |
| 1-4 | x1 | 15-19 | x2.5 |
| 5-9 | x1.5 | 20+ | x3 |
| 10-14 | x2 | | |

A perfect 20-question run scores **2365**. End screen shows final score, highest tier reached and per-tier accuracy, which gives a rough read on where the student's threshold sits.

**Survival.** Hidden. Pinned to tier 10, sine, unison, In Tune off, single listen. Three lives, a wave is five correct in a row. Uses the reflex speed ladder (x10 at under 200 ms down to x1 over 3200 ms) rather than the streak multiplier. Entered by clicking the DIFFICULTY label 16 times within 8 seconds. Exits via EXIT or the end screen.

No speed scoring in Practice or Challenge. Fine intonation discrimination is a careful-listening task, and a speed bonus pays students to guess at exactly the tiers where guessing is most tempting.

## Controls

| Key | Action |
| --- | --- |
| `1` / `←` | Flat |
| `5` / `↓` | In Tune |
| `0` / `→` | Sharp |
| `Space` | Replay |
| `Enter` | Start / Next |
| `[` `]` | Step tier (Practice) |
| `Q W E R` | Piano / Strings / Sine / Saw (Practice) |

Key hints are deliberately not printed on the pads. Answer keys are handled before everything else in the keydown handler, so a stray keystroke cannot select an instrument mid-question.

## Technical notes

- Single self-contained HTML, ~5.8 MB. Samples spliced in at build time from `interval-trainer/index.html`; the two payload lines are `SAMPLES` and `SURVIVAL_VOICE`.
- No `fetch()`. All audio is base64 decoded via `atob()` into `Uint8Array` then `decodeAudioData()`.
- `AudioContext` is created on first user gesture (`ensureAudioThen`) for iOS Safari.
- Survival voice sample is shared with Interval Trainer. If it fails to decode there is an oscillator sting fallback.
- Highest note reachable is G4 (MIDI 67), descending an octave from a G3 root, well inside the sampled range, so no extreme playbackRate stretching.
- Sample tuning is assumed correct. Not FFT-verified. If any source WAV sits a few cents off nominal, that bias is larger than the detune being tested at tiers 9 and 10. Worth checking before leaning on the fine tiers for assessment.

## Open decisions / TODO

- Leaderboard deferred. Would need its own sheet or a mode column added to the shared Interval Trainer endpoint.
- Tier names are plain numbers. Ten tempo markings exist (Larghissimo through Prestissimo) and would match Interval Trainer, but tempo names on a precision ladder are misleading.
- Default instrument is piano, which is the hardest timbre here because of the attack transient and decaying amplitude. Sine is easiest by a distance. One-word change if a gentler first contact is wanted.
- ET versus just intonation is not addressed anywhere in the MOTE. An ET fifth sits about 2 cents narrow of a just fifth; in a melodic context with no beating this does not corrupt the task, but it is a teaching moment sitting unused.
- Chance rate is 50% on two answers and 33% on three. Neither tells a student whether they heard it or guessed. An adaptive staircase mode reporting a single cent threshold would give a measurable outcome across a semester; scoped and declined for v1.0.

## Last updated

2026-08-04 — v1.0 initial ship.
