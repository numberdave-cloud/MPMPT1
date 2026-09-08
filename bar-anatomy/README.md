# Bar Anatomy

**Directory:** `bar-anatomy/` · **Category:** Composition

Listening and identification device for the parts of a bar of 4/4. One fixed drum loop runs while the student switches between three overlays: how the bar divides (whole to sixteenth), how it is counted (1 / 1 & / 1 e & a, in DJ's voice), and what its beats are called (downbeat, backbeats, offbeats, upbeat). Nothing is editable in normal use. Built for the MPCT1 Week 1 Bars video.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/bar-anatomy/

## Canvas iframe embed

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/bar-anatomy/" width="100%" height="700" title="Bar Anatomy" style="border: none;" allow="autoplay" loading="lazy"></iframe>
```

Height 700, not the 600 default: the Grid divisions overlay stacks five division rows above the three-lane grid, and with a three-line info entry showing the card runs to about 690px. The other two overlays sit under 600.

## Build state

v1.0, 2026-09-08. Copy approved. Voice, drum and voice-kit samples all supplied by Dave and inlined. Not yet verified in Canvas.

## Interaction

- Play / Stop runs the loop at a fixed 90 BPM. Master fader (-36 to 0 dB, default -6) sits beside it.
- Grid divisions: click a row to select it. A 1500 Hz tick plays at that division, the block under the playhead lights, and the drums duck by 12 dB while a row is selected. Click again, change overlay, or press Escape to clear.
- Counting the bar: click a level (Quarters / Eighths / Sixteenths). Voice syllables fire as the playhead crosses each one. Each syllable is shaped to its slot with a short fade at the slot end rather than a hard stop.
- Elements of a bar: four buttons. Selecting one solos those step positions in the loop (Downbeat = step 1, Backbeats = 5 and 13, Offbeats = 3, 7, 11, 15, Upbeat = 13) and greys out the other hits on the grid.
- Info panel shows the selected entry with the British note name in brackets.

## Hidden mode

Clicking the Counting the bar tab 16 times unlocks voice sequencer mode. The kick, snare and hat lanes swap to Dave's vocal versions, every grid cell becomes clickable to toggle a hit, and the title changes to "Bar Anatomy: voice sequencer". Nothing persists; a refresh resets it. Overlays keep working on the programmed pattern because Elements solo is by step position. `SECRET_TAPS` in the config block sets the count.

## Audio

- All audio is base64 WAV decoded via `atob()` and Web Audio (Canvas blocks fetch on data URLs). No synthesis.
- Drums: `DRUMS` object. Kick 359 ms, snare 352 ms, hat 200 ms, stereo 44.1k 16-bit, trimmed at the tails only. Levels as bounced (hat sits ~17 dB under kick and snare by design).
- Voice syllables: `VOICE` object, seven mono 44.1k 16-bit one-shots (one, two, three, four, e, and, a), 117 to 251 ms, common +6 dB applied over Dave's bounce levels. Fit inside a sixteenth at 90 BPM except "and", which fades over its last ~80 ms at that level.
- Voice kit: `VOX` object, three mono one-shots (kick 179 ms, snare 277 ms, hat 234 ms), common gain so the loudest peaks at -1 dBFS.
- Scheduler: 25 ms timer, 120 ms lookahead, sources fired at exact multiples of the step duration. No looping buffers.
- Page ~444 KB total.

## Open TODOs

- Verify playback, layout and the 700px height live in Canvas.
- Recorded musical examples were scoped for a later stage; no slot built for them yet.
- Division tick stays a sine blip in hidden mode. Silence it if "voice only" is meant literally.

## Last updated

2026-09-08. v1.0: initial build and ship. Three overlays, sample-based loop, master fader, ducking on division select, hidden voice sequencer mode.
