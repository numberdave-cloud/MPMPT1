# Mix Balance [Industrial]

**Directory:** `mix-balance-industrial/` · **Category:** Mixing

Multi-channel fader balance exercise on a industrial stem set, for gain staging and level relationships.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/mix-balance-industrial/

## Canvas iframe embed

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/mix-balance-industrial/" width="100%" height="600" title="Mix Balance [Industrial]" style="border: none;" allow="autoplay" loading="lazy"></iframe>
```

Height 600 (default). Measured at 584px rendered for Canvas columns 700px wide and up. Near 480px wide the transport row wraps and the content reaches about 628px, so use height 640 if the column is narrow.

## Build state

v1.1, live. Not yet verified in Canvas.

- Assist starts OFF.
- Master volume knob beside the Assist button (see technical notes).
- Reskinned to match the Interval Trainer frame: rounded bumper (26px) around a 12px-radius screen, transparent page behind it.
- Ableton session palette sampled from a Live screenshot, with heavier lines (2px borders, 4px fader tracks).

## Technical notes

Single self-contained HTML, ~2.6 MB. Base64-embedded OGG stems (drums, vocal, bass, guitars, lead) decoded via `atob()`. All stems stereo, 44.1 kHz (read from the Vorbis headers). Master loop period 10.675374 s (guitars.ogg duration, shortest in the set). Gapless looping via precision scheduler (no `loop=true`), pako present. File size is heavy; watch the base64 payload if adding stems.

Audio graph: stem source, pre-fader gain, fader gain, `masterGain` (play and stop fades), analyser (OUT meter and clip latch), `monitorGain` (volume knob), destination.

Volume knob: sits after the analyser, so it changes only how loud the student hears the mix. The OUT meter and clip latch keep reading the mix itself. Range is -40 dB to 0 dB with silence at the bottom of travel. Default is 75% of travel, which is -10 dB (`VOL_DEFAULT = 0.75`). Drag, scroll wheel, arrow keys, Home and End all work, and double-click resets to the default. No focus outline (keyboard focus brightens the knob's inner circle instead).

Palette tokens in `:root`: bg `#2B374D`, well `#0F1A22`, ink `#161F35`, text `#DAD7D2`, accent `#F6C86B`, glow `#FFDA8C`, dim `#B8B8B7`, faint (lines) `#8D94B1`, seg `#6B7596`, green (balanced) `#BFDFD3`. Clip red stays `#C04838` because the source screenshot had no red.

## Open TODOs

- Verify the frame, knob and narrow-column wrap in a real Canvas page.
- Confirm -10 dB feels right as the default listening level in a classroom.

## Last updated

2026-10-01: assist off by default, master volume knob (default -10 dB), Interval Trainer frame, Ableton palette.
