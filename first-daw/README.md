# Basic DAW Interface

Formerly titled Baby's First DAW (renamed in v1.3).

Directory: `first-daw/`
Category: Composition

A safe, simplified DAW interface for a student's first look at a digital audio workstation. Four looping tracks (two MIDI, two audio) with working transport, mute, solo, pan and volume, plus dummy controls. Every part shows an explanation when hovered or tapped, and a DAW terms toggle swaps labels between Logic, Pro Tools and Ableton.

Live URL: https://numberdave-cloud.github.io/MPMPT1/first-daw/

## Canvas embed

Height 800 (non-default). The page measures 728 px at full width, about 780 px at typical Canvas content widths and about 825 px on a phone, so 600 would crop the info panel.

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/first-daw/" title="Basic DAW Interface" width="100%" height="800" style="border: none;" allow="autoplay" loading="lazy"></iframe>
```

## Build state

v1.3, shipped 2026-10-26. Not yet verified in Canvas.

## What works and what doesn't

Working: play, stop (returns to bar 1), position counter, playhead, metronome (accent on beat 1), mute, solo, pan knobs, track faders with level meters, master fader, browser panel open/close, save dialog, DAW terms toggle, loop marker show/hide.

Dummy: record (flashes red), record arm (toggles red), loop toggle (playback always loops), instrument slot (shows info), browser folders (display only, apart from the four easter egg folders below), tempo (fixed display).

## Technical notes

- Four OGG Vorbis stems, 44.1 kHz stereo, each 7.3846 s. Rendered as 8 bars at 260 BPM; the MOTE displays them as 4 bars at 130 BPM (same audio, same speed). Embedded as base64, decoded with atob() and decodeAudioData.
- Bass and drums are labelled MIDI but play audio stems. Vocal clip is drawn at bar 3, beats 1 to 2; its reverb tail plays through the following bars as rendered.
- Loop period 7.3846 s. Precision scheduler fires all four sources at exact multiples of the loop length (no loop=true).
- Signal chain per track: source, mute/solo gain, fader gain, StereoPanner, Analyser, master gain.
- Meters: -48 to +6 dB scale, green below -6, amber to 0, red at clipping. Stems peak between -10 and -19 dBFS.
- MIDI clip note blocks in `src/notes.json` were traced from Dave's Ableton screenshot and halved to fit 4 bars. Audio clip waveforms are drawn from the decoded buffers.
- Terminology table lives in the TERMS object; info copy (Dave's, approved) in the INFO object.
- Tempo display and metronome run at 130 BPM, accent on each downbeat.
- Easter egg: clicking 1980s Anime Sound Effects, Jungle Jungle Sample Pack, 803 Kick Drums or Nicolas Cage quotes plays a one-shot through the master fader. The folder lights while it plays; clicking it again stops it, and clicking another folder swaps. Sources are Dave's 32-bit float WAVs, converted to OGG Vorbis q6 (`src/egg_*.ogg`) to keep the page around 1.9 MB. Decoded lazily on first click.
- Spacebar toggles play/stop. Double-click a fader or knob to reset.
- Source in `src/`: edit template.html, then run `python3 build.py` to regenerate index.html.
- Colour scheme departs from the suite: black background (#0B0B0C) at Dave's request, accent orange kept.

## Open decisions / TODOs

- Verify playback and embed height in Canvas.
- Info panel placeholder "Hover over or tap anything" is Claude's wording, not yet confirmed by Dave.
- Safari/iOS OGG decoding untested.

Last updated 2026-10-26: v1.3, renamed from Baby's First DAW to Basic DAW Interface (folder unchanged).
