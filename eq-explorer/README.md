# EQ Explorer

Channel-strip EQ MOTE. Students boost and cut three fixed bands on a looping audio source and learn to associate subjective descriptive language (warm, muddy, honky, airy, scooped) with what EQ moves actually do.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/eq-explorer/

## Canvas iframe embed

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/eq-explorer/" width="100%" height="600" title="EQ Explorer" style="border: none;" allow="autoplay" loading="lazy"></iframe>
```

Default height `600`. May want to drop to `540` once tested in Canvas — widget is compact.

## Build state

**v0.1 — first prototype, single audio source (`dry.ogg`) only.**

Working: EQ chain, knobs, solo per band, bypass, descriptive readout, loop scheduler.
Not yet built: source selector (Drums / Guitars / Synths / Full Mix).

## Technical notes

- Single self-contained HTML file, ~286 KB, Web Audio API only, no libraries
- Audio: OGG (stereo 44.1 kHz Vorbis), base64-embedded, decoded via `atob()` then `decodeAudioData()`
- Precision scheduler fires new `AudioBufferSourceNode`s at exact multiples of buffer duration — no `loop=true` (drifts)
- Five parallel gain-gated routing paths (EQ / bypass / soloLo / soloMid / soloHi) with 12 ms crossfade time constant to prevent switching clicks

### EQ topology

| Band | Type | Freq | Q |
|---|---|---|---|
| Low shelf | `lowshelf` | 100 Hz | — |
| Mid peak | `peaking` | 750 Hz | 0.7 |
| High shelf | `highshelf` | 4 kHz | — |

Range ±9 dB, 1 dB discrete steps (19 positions per knob). Knobs: 270° total rotation, 15° per step. Interaction: vertical drag (~7 px/step), scroll wheel, double-click to reset.

### Solo band routing

| Solo | Filter | Freq | Q |
|---|---|---|---|
| Low | `lowpass` | 220 Hz | 0.7 |
| Mid | `bandpass` | 750 Hz | 0.9 |
| High | `highpass` | 3.5 kHz | 0.7 |

Solo isolates the range the band acts on, not the band's boost/cut amount.

### Descriptive readout

Rule cascade over the three band values:

1. Named curves (Smiley/Hyped, Telephone, Big/Excited)
2. Tilt curves (Muddy/Dark, Warm/Dark, Thin/Bright, Light/Open)
3. Mid-driven (Honky, Boxy/Forward, Scooped, Hollow)
4. Single-band strong (Boomy, Airy/Bright, Thin, Dull)
5. Single-band mild (Warm, Bright, Light, Dark)
6. Fallback: Coloured
7. All bands within ±1 dB: Flat

Overridden by `Solo · High/Mid/Low` when a solo is active, and by `Bypass` when bypassed.

## Open TODOs

- **Source selector** — add Drums / Guitars / Synths / Full Mix buttons. Only one source plays at a time. Remaining three OGGs pending from Dave.
- **Readout threshold tuning** — labels are best-guess. Play with the widget and nudge by ear (e.g. is "Boxy / Forward" right at +3 mid, or should that read just "Forward"?).
- **Solo Q tuning** — mid solo at Q 0.9 is a first pass. May want wider or narrower depending on what feels most revealing.
- Deliberately **not** included (may reconsider later): level matching between EQ and bypass, momentary-hold bypass, frequency response display, spectrum analyser, numerical hertz on the front panel.

## Last updated

2026-07-14 — v0.1 shipped with single dry source. Awaiting remaining source OGGs.
