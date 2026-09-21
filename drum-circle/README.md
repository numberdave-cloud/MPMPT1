# Drum Circle — live collaborative drum grid

Directory: `drum-circle/`

A live, multiplayer 16-step by 8-lane drum grid for in-class step sequencing and
drum programming. Students open a link on their own devices and tap notes into a
shared grid, a budgeted number of notes each. The host screen plays the grid out
through Web MIDI into Ableton in real time and can capture it as a `.mid` clip.

This is not a Canvas-embedded MOTE. It runs as a live tool opened directly in the
browser during a synchronous class. It needs external services (Firebase Realtime
Database, plus Firebase and QR scripts from CDNs) that Canvas CSP would block, so
it is not iframed into Canvas.

## URLs
- Host (control screen, your Mac, Chrome): https://numberdave-cloud.github.io/MPMPT1/drum-circle/?host=1
- Player (hand to students): https://numberdave-cloud.github.io/MPMPT1/drum-circle/

## How it runs
- Two roles from one file, split by the `?host=1` query flag. Host gets transport,
  MIDI, swing, the note-budget stepper, the two unlock toggles, clear-all, `.mid`
  download, plus the player link and a QR code.
- Players get just the grid. Tap places a note at velocity 100, tap again drops it
  to 65, a third tap clears it. Each player is capped at the host's per-player
  allowance and sees how many notes they have left.
- One note per cell. Players can only touch another player's note when the host
  turns on "delete others" or "move others". Move is lift-then-drop onto a
  neighbouring cell. Notes carry each player's colour on both screens.

## Sync / backend
- Firebase Realtime Database, Spark (free) tier. Project `drum-circle-database`,
  region asia-southeast1.
- The web config is embedded in `index.html` in the `FIREBASE` block. This is the
  public client config, not a secret.
- DB rules are currently open (`.read` / `.write` true). Fine for throwaway grid
  data. If reused often, switch on Anonymous auth and gate the rules behind it.
- Room id defaults to `main`. Add `?room=xxx` to both host and player links for a
  separate room.
- If the config is ever blanked, the page falls back to solo mode: grid and MIDI
  on one machine, no students.

## MIDI / audio
- Host only, Chrome only (Web MIDI). Sends note-ons to the chosen output and
  auto-selects an IAC bus if it finds one.
- 8 rows map to notes C1 to G1 (36 to 43), the bottom eight Drum Rack pads.
  Channel selectable, default 1.
- BPM and 16th swing are host-side live feel and are not baked into the `.mid`
  export, which stays quantised. The export does keep each note's velocity.

## Ableton setup
IAC Driver on (Audio MIDI Setup), MIDI out set to the IAC bus, Ableton MIDI track
input set to IAC, Monitor set to In, a Drum Rack loaded.

## Open / TODO
- `databaseURL` was completed from a screenshot that cut off. Verify it against the
  console Data tab.
- Not yet load-tested with a full class.
- Timing free-runs, not MIDI-clock-synced to Ableton. Clock-out is a possible later
  addition.
- Anonymous-auth lockdown of DB rules pending if this gets regular reuse.

Last updated: 2026-09-21 — first ship, v1.0.
