# Basic Piano Roll

Directory: `basic-piano-roll/`
Category: Composition

A fixed, playable example of a one-bar monophonic bass part in a MIDI editor. Students press play, hear the loop, and click around to learn what each part of the piano roll is called. Nothing in the clip can be moved or edited. The companion piece to Basic DAW Interface (`first-daw/`): where that one shows the DAW workspace, this one shows the inside of a MIDI clip. Editing the notes comes in a later device.

Live URL: https://numberdave-cloud.github.io/MPMPT1/basic-piano-roll/

## Canvas embed

Height 820 (non-default). The page measures about 810 px at desktop widths and about 825 px on a phone, so 600 would crop the velocity lane and info panel.

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/basic-piano-roll/" title="Basic Piano Roll" width="100%" height="820" style="border: none;" allow="autoplay" loading="lazy"></iframe>
```

## Build state

v1.0, shipped 2026-10-26. Not yet verified in Canvas.

## What it does

- One-bar clip, 4/4, 72 BPM, 1/16 grid. Plays Dave's supplied bass loop (OGG).
- Transport: play, stop (returns to bar 1), loop (always on here). Spacebar toggles play/stop.
- Playhead sweeps the bar; position counter reads bar.beat.sixteenth with per-DAW separators.
- Keyboard down the side, C3 and C2 marked. Click a key to audition that pitch (synthesised triangle + low-pass, not the loop).
- Click a note block to audition its pitch and show its pitch / length / velocity in the info panel.
- Read-only velocity lane under the grid: stalks + heads, one per note, matching the MIDI.
- Logic / Pro Tools / Ableton toggle swaps all terminology, the ruler format (1 2 3 4 / 1|1|1 / 1.1.1) and the position separators.
- Hover or tap any element for its info-panel entry.
- Nothing is editable. No draw, delete, move, resize. Swing/Groove is a named chip with an info entry only, no control (students apply it in a later device).

## Technical notes

- Notes traced verbatim from Dave's `BASS_LOOP_MIDI_FILE.mid` (type 0, 96 PPQ, 8 notes, monophonic). Stored in `src/notes.json` as `[midiPitch, startBeat, lengthBeats, velocity]`.
- The 8 notes: C2 dotted-1/8 v100, C2 1/8 v75, C2 1/16 v65, D#2 1/8 v100, C2 dotted-1/8 v100, C2 1/8 v50, C2 1/16 v75, B1 1/8 v100.
- Audio: Dave's `BASS_LOOP_AUDIO.wav` (48 kHz, 24-bit stereo, 3.3333 s = one bar at 72 BPM) converted to OGG Vorbis q6 (`src/bass_loop.ogg`, ~31 KB). Embedded as base64, decoded with atob() + decodeAudioData.
- Loop period 3.3333 s. Precision scheduler fires the source at exact multiples of the loop length (no loop=true).
- Pitch rows span A1 (MIDI 45) to C3 (MIDI 60), 16 rows. Note name convention is C3 = middle C (MIDI 60), matching the Ableton source screenshot.
- Octave convention is display-only words in the info panel; the keyboard labels do not flip between C3/C4 across DAWs (open decision below).
- Key auditioning uses a synthesised triangle through a low-pass, not the bass stem, so single notes are audible on their own.
- Colour scheme matches Basic DAW Interface: black background (#0B0B0C), accent orange.
- Source in `src/`: edit template.html, then run `python3 build.py` to regenerate index.html.

## Open decisions / TODOs

- Info-panel copy is Claude's draft, not yet approved by Dave. Entries to review: Note, Velocity, Note Length, Octave, Grid, Editor. Shipped on Dave's call before copy sign-off.
- Octave readout: currently explained in words only. Open question whether the keyboard labels should flip to the C4 convention when Logic/Pro Tools is selected.
- "Note Length" and "Time Signature" info entries were added beyond the named scope; confirm they stay.
- Verify playback and embed height in Canvas.
- Safari/iOS OGG decoding untested.

Last updated 2026-10-26: v1.0, first ship.
