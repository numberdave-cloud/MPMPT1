# Beat Recreate

Directory: `beat-recreate/`

A listen-and-recreate drum game. Students hear a one-bar drum pattern, rebuild it by ear on a six-channel sixteen-step sequencer, then check their accuracy and take a quick peek at the answer.

## Live
https://numberdave-cloud.github.io/MPMPT1/beat-recreate/

## Canvas embed
```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/beat-recreate/" width="100%" height="600" style="border: none;" allow="autoplay" loading="lazy" title="Beat Recreate"></iframe>
```
Height 600 is the default and clears the widget (about 550px tall) with room to spare.

## Build state
Trial build on placeholder assets. Kit is Kit Test (the KT_ WAVs). Four test answers (ANSWER_1 to 4). Flat Beat 1 to 4 picker, no difficulty gating yet.

## How it works
- Six channels: kick, snare, clap, closed hat, open hat, tom. All rows stay open on every beat, so wrong hits on channels that are empty in the answer count against the score as extras.
- Original and Yours both play through the same kit, so a perfect recreation sounds identical to the source. Pressing either restarts from the top of the bar.
- Check Score grades a snapshot and pulses once. Formula is correct / (correct + missed + extra). It does not update live as notes are added.
- Reveal Answer flashes the answer for four seconds then clears itself. Green is correct, amber is missed, red is should-not-be-there.
- Gold Flawless skin fires on any 100% Check. This becomes Hard-only once difficulty gating is added.
- Keyboard: 1 plays Original from the top, 2 plays Yours from the top, space stops.
- Count / Steps toggle switches the column labels between 1 to 16 and 1 e and a counting.

## Technical notes
- Single self-contained HTML. Six WAV one-shots are base64-embedded and decoded via atob() then decodeAudioData, since Canvas blocks fetch on data URLs.
- Kit WAVs are 16-bit stereo PCM, 44.1kHz, roughly half-second one-shots.
- Answer MIDIs are parsed into 16-step grids at build time by an external Python builder. Nothing MIDI runs in the browser. Source MIDIs are PPQ 96, quantised to 16ths.
- BPM is read from the MIDI filename, not from a tempo meta event (the test MIDIs carry none).
- Note map: 36 kick, 38 snare, 39 clap, 42 closed hat, 46 open hat, 47 tom. Fixed across kits.
- Playback uses a precision scheduler firing sources at exact 16th intervals, not loop=true, to avoid drift.

## Open decisions / TODO
- Filename convention proposed, not yet locked. Samples as `kit_drum.wav`, answers as `beat_difficulty_kit_bpm.mid`. The builder still reads the old `ANSWER_n_TEST_bpm` test names until real assets arrive in the agreed format.
- Difficulty gating (Easy / Medium / Hard) and the Hard-only gold egg are deferred. Flat picker for now.
- Real kits and beats to replace the Kit Test placeholders.
- Final name and directory. "Beat Recreate" is provisional.
- Kits with fewer than six sounds: widget shows a row per sound present, but this path is untested until a real short kit exists.

## Last updated
2026-07-14. Initial ship: trial build with Kit Test assets and four test beats. Momentary four-second reveal, keyboard transport (1/2/space), snapshot scoring with single pulse, all channels open for scored mistakes, challenge and info bars removed, brighter borders.
