# Drum Circle — live collaborative drum grid

Directory: `drum-circle/`

A live, multiplayer 16-step by 8-lane drum grid for in-class step sequencing and
drum programming. Students open a link on their own devices and tap notes into a
shared grid, a budgeted number of notes each. The host screen plays the grid out
through Web MIDI into Ableton in real time, can drive Ableton's tempo and transport
over MIDI clock, and can capture the pattern as a `.mid` clip.

This is not a Canvas-embedded MOTE. It runs as a live tool opened directly in the
browser during a synchronous class. It needs external services (Firebase Realtime
Database, plus Firebase and QR scripts from CDNs) that Canvas CSP would block, so
it is not iframed into Canvas.

## URLs
- Host (control screen, your Mac, Chrome): https://numberdave-cloud.github.io/MPMPT1/drum-circle/?host=1
- Player (hand to students): https://numberdave-cloud.github.io/MPMPT1/drum-circle/

## Roles
Two roles from one file, split by the `?host=1` query flag.
- Host gets transport, MIDI out, swing, a MIDI clock-out toggle, the note-budget
  stepper, the delete and move strips, clear-all, `.mid` download, plus the player
  link and a QR code.
- Players get the grid, a 2-character initials box, the room list, and their own
  `.mid` download. Their download uses the host's tempo.

## Player interaction
- Tap an empty square to place a note at velocity 100, tap again for 65, a third
  tap clears it. Capped at the host's per-player allowance; remaining count shown.
- Each player's initials sit on their notes and in the room list, on both screens.
  Unset reads as "––".
- One note per cell. Players only touch other players' notes when the host enables
  it (below).

## Host: delete and move
- Deletes: an Off / 1 / 2 / 3 / 4 strip. Pressing a number tops every player
  (including later joiners) up to that many delete tokens; each delete spends one.
  Off = zero. Stored as `config.deleteGrant = {n, id}`; a new id refills everyone.
- Move: an Off / 1 / 2 / 3 / 4 strip read as distance, not tokens. The number is the
  max squares (Manhattan, so lane changes count) a single move can shift a note.
  Moves are unlimited while on; Off stops all moving. Lifting a note highlights the
  legal drop squares. Big shifts need teamwork across players.

## Sync / backend
- Firebase Realtime Database, Spark (free) tier. Project `drum-circle-database`,
  region asia-southeast1.
- Web config embedded in `index.html` in the `FIREBASE` block. Public client config,
  not a secret. DB rules are currently open (`.read` / `.write` true); fine for
  throwaway grid data. Anonymous-auth lockdown is the upgrade path if reused often.
- Room id defaults to `main`. Add `?room=xxx` to both host and player links for a
  separate room.
- Config keys: `allowance`, `bpm` (synced so player exports match), `moveDist`,
  `deleteGrant {n,id}`.
- If the config is blanked, the page falls back to solo mode (grid + MIDI on one
  machine, no students).

## MIDI / audio (host, Chrome only)
- Sends note-ons to the chosen output; auto-selects an IAC bus if it finds one.
- 8 rows map to notes C1 to G1 (36 to 43), the bottom eight Drum Rack pads.
  Channel selectable, default 1.
- Clock out toggle: when on, sends MIDI Start (0xFA) on play, Stop (0xFC) on stop,
  and 24-PPQ clock (0xF8), scheduled with Web MIDI timestamps. Page is master. In
  Ableton: Preferences > Link Tempo MIDI > enable Sync on the IAC input. Left off,
  behaviour is unchanged (notes only, no transport). Browser clock is tight enough
  to play against but not hardware-steady; test before leaning on it live.
- BPM and 16th swing are host-side live feel and are not baked into the `.mid`
  export, which stays quantised. Export keeps each note's velocity.

## Ableton setup
IAC Driver on (Audio MIDI Setup), MIDI out set to the IAC bus, Ableton MIDI track
input set to IAC, Monitor set to In, a Drum Rack loaded. For tempo sync, also enable
Sync on the IAC input under Link Tempo MIDI.

## Open / TODO
- `databaseURL` was completed from a screenshot that cut off. Verify against the
  console Data tab.
- Not yet load-tested with a full class.
- Clock-out jitter unverified against a live Ableton set.
- Move distance is Manhattan (lane changes allowed). Switch to horizontal-only if
  wanted.

Last updated: 2026-09-21 — v1.1. Added player initials + note labels, delete-token
and move-distance strips, player-side room list and `.mid` download, and MIDI
clock/start/stop out (page as master).
