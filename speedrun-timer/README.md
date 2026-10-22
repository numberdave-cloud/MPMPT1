# Speedrun Timer

Directory: `speedrun-timer/`
Category: Trainers

A drill stopwatch that runs while the student is away from Canvas. They read the drill on the Canvas page, press Start, switch to their DAW, complete the steps, and switch back. The clock runs only while they're out of the browser. It has an optional alarm that sounds when the target time is reached.

Supersedes RackMat Timer (`rackmat-timer/`), which stays live until Canvas pages point here.

Live URL: https://numberdave-cloud.github.io/MPMPT1/speedrun-timer/

## Canvas embed

Height 520 (not the default 600). The card renders at 419px on desktop. Below about 760px wide the header wraps to two rows and the card grows to 497px at 700 wide and 517px at 480 wide.

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/speedrun-timer/" width="100%" height="520" title="Speedrun Timer" style="border: none;" allow="autoplay" loading="lazy"></iframe>
```

With a preset target (target switches on at that time):

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/speedrun-timer/?target=60" width="100%" height="520" title="Speedrun Timer" style="border: none;" allow="autoplay" loading="lazy"></iframe>
```

## Build state

v1.0, shipped 2026-10-23. Not yet verified in Canvas.

## Technical notes

- State machine: Ready, then Armed (after Start), then Running (window blur), then Stopped (window focus, or pointer movement over the frame). Again re-arms; Reset zeroes.
- Leaving is detected by `blur` on the frame's window. Returning is detected by `focus` (Alt-Tab / Cmd-Tab restores focus to the frame), with a backup stop on real pointer movement (6px or more, at least 400ms after the start) for students who return by clicking outside the frame.
- Timing comes from `performance.now()` timestamps, so background throttling doesn't affect accuracy. The display catches up on return.
- Known limit: clicking the Canvas page outside the frame after Start counts as leaving and starts the clock early. The student sees it running and presses Reset.
- Target: off by default at 1:00, 5s steps, range 0:05 to 59:55. Typed input accepts seconds ("90") or M:SS ("1:30"). URL param `?target=` presets it and switches it on.
- Readout and progress bar go green under target, red over. BEST is a session best (lost on refresh), no localStorage.
- Sound: speaker button (off by default) plus an always-visible mode dropdown (fixed 168px width so nothing shifts). Speaker off means silent. Turning the speaker on also switches the target on.
  - Arm beep (Slava Pogorelsky UI beep, -10 dB baked in) plays on Start when the speaker is on.
  - Calm: Dave's calm.wav at the target time.
  - Obnoxious: Dave's obnoxious.wav (-12 dB baked in) at the target time.
- Alarms are scheduled on the AudioContext clock at the moment the student leaves, so tab throttling can't delay them. Returning before the target cancels the pending alarm.
- Audio: WAV 16-bit 44.1kHz stereo, base64 inline in `SOUND_DATA`, decoded with atob(). Beep and calm tails trimmed (0.75s, 1.15s). Master DynamicsCompressor as a safety limiter. Page is about 800KB.
- Zimmer Inspo Mode is parked: `ZIMMER_ENABLED = false`. When true, three over-target runs in a session add the option to the dropdown (and `?zimmer=1` unlocks it for testing). Design: boom on clock start, strings loop while running, BRAAAM at target, resolution on return inside target. Slots `zimmerStart`, `zimmerRun` (OGG loop), `zimmerOver`, `zimmerWin` are empty and fall back to synthesised stand-ins. Widen the dropdown back to 214px if it returns.
- Keys: Space or Enter starts / re-arms, Escape resets (not while running).
- No instruction text in the MOTE by design. Drill steps live on the Canvas page.

## Open decisions / TODOs

- Verify focus behaviour and background alarm playback in a real Canvas page on Windows and macOS (Safari in particular).
- Zimmer Inspo Mode sounds (Dave to supply), then set `ZIMMER_ENABLED = true`.
- Point Canvas pages at this folder, then archive `rackmat-timer/`.

## Last updated

2026-10-23: initial ship (v1.0), renamed from RackMat Timer, alarm sounds added.
