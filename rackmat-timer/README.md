# RackMat Timer

Directory: `rackmat-timer/`
Category: Trainers

A drill stopwatch that runs while the student is away from Canvas. They read the drill on the Canvas page, press Start, switch to Ableton, complete the steps, and switch back. The clock runs only while they're out of the browser.

Live URL: https://numberdave-cloud.github.io/MPMPT1/rackmat-timer/

## Canvas embed

Height 480 (not the default 600). The card renders at 419px on desktop and 469px on narrow screens, so 600 leaves dead space.

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/rackmat-timer/" width="100%" height="480" title="RackMat Timer" style="border: none;" allow="autoplay" loading="lazy"></iframe>
```

With a preset target (target switches on at that time):

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/rackmat-timer/?target=60" width="100%" height="480" title="RackMat Timer" style="border: none;" allow="autoplay" loading="lazy"></iframe>
```

## Build state

v1.0, shipped 2026-10-22. Not yet verified in Canvas.

## Technical notes

- State machine: Ready, then Armed (after Start), then Running (window blur), then Stopped (window focus, or pointer movement over the frame). Again re-arms; Reset zeroes.
- Leaving is detected by `blur` on the frame's window. Returning is detected by `focus` (Alt-Tab / Cmd-Tab restores focus to the frame), with a backup stop on real pointer movement (6px or more, at least 400ms after the start) for students who return by clicking outside the frame.
- Timing comes from `performance.now()` timestamps, so background throttling while the student is in Ableton doesn't affect accuracy. The display catches up on return.
- Known limit: clicking the Canvas page outside the frame after Start counts as leaving and starts the clock early. It can't be told apart from an app switch inside a cross-origin iframe. The student sees it running and presses Reset.
- Target: off by default at 1:00, 5s steps, range 0:05 to 59:55. Typed input accepts seconds ("90") or M:SS ("1:30"). URL param `?target=` presets it and switches it on.
- Readout and progress bar go green under target, red over. BEST is a session best (lost on refresh), no localStorage.
- Audio: short synthesised sine cues via Web Audio. Tick on arm, blip when the clock starts, two-note chime on under-target, low tone on over-target, single tone with no target. The AudioContext is created on the Start click.
- Keys: Space or Enter starts / re-arms, Escape resets (not while running).
- No instruction text in the MOTE by design. Drill steps live on the Canvas page.

## Open decisions / TODOs

- Verify focus behaviour inside a real Canvas page on Windows and macOS.
- Decide whether the audio cues stay.

## Last updated

2026-10-22: initial ship (v1.0).
