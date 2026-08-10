# Energy Dial

**Directory:** `energy-dial/`

One running scene (Terminator 2 truck chase), three music beds at different energy levels. The student flips between beds and hears how energy recontextualises the same footage. Extension of the Scene Scorer cue-audition family. Home: B1·W3 (energy and style page).

## Live URL

https://numberdave-cloud.github.io/MPMPT1/energy-dial/

## Canvas embed

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/energy-dial/"
  width="100%"
  height="545"
  title="Energy Dial"
  style="border: none;"
  allow="autoplay"
  loading="lazy">
</iframe>
```

Height 545: the v1.1 letterbox crop (2.526:1 window) puts the card at ~535px at full width. Was 660 pre-crop. Re-measure once live if Canvas shows a scrollbar.

## Build state

v1.1, 2026-08-06. Category: Miscellaneous (assumed, unconfirmed). Shipped for live testing at Dave's request (YouTube refuses file:// referrers, live origin is the only test bench). Scene confirmed loading and playing on live; levels and bed lengths unverified.

## Config

- Scene: `6z9qws7M8q8` (Terminator 2 truck chase, "Flashback FM" upload, 2.40:1 picture in a 16:9 frame), starts at 1:12 (72s), audio permanently muted
- ENERGY 1: `ZtbDetsudtI`, starts at 2:35
- ENERGY 2: `cLc37iEdMyg`, starts at 0:48
- ENERGY 3: `7cx3cOVnV0g`, starts at 0:36
- Default selection: ENERGY 1. Labels deliberately unranked (no GLACIAL/FRANTIC) so students judge energy by ear.
- All volumes 100, untrimmed.
- `fadeInMs: 1000`, `fadeOutMs: 150`, `fadeExp: 2` in CONFIG.

## Interaction model

Inherited from `scene-scorer-drive/` v1.1: selector is the primary control, transport demoted beneath it. FROM TOP (default) resets scene and beds to their start points on any selection; SEAMLESS hot-switches while the video rolls. PLAY/PAUSE, RESTART, master volume knob with segment readout.

## Differences from scene-scorer-drive

- No TEMP TRACK button; the scene's own audio is muted at all times.
- No first-trigger lockout.
- Fade engine: every bed entrance fades in over 1s on a power curve (`frac^fadeExp` applied to the per-bed volume, master knob still effective mid-fade); outgoing bed drops over 150ms on a seamless switch, then mutes. Single 30ms interval drives all fades and stops itself when idle.
- Letterbox crop (v1.1): the upload is 2.40:1 inside 16:9 with 98px baked bars (measured from a live screenshot at 1356px window width). Frame cut to 2.526:1, player at `top: -21.58%`. Top crop is one bar + 3% of picture (buries title/channel text); bottom crop is one bar + 2% of picture (this upload's More Videos pill pokes ~3% above the bottom bar, unlike Drive where one bar sufficed). Maths in the CSS comment.

## Technical notes

- Shared Scene Scorer machinery: four synced YT players, inert click-shield, caption kill, opaque `#videoCover` whenever the scene is not rolling (LOADING → READY → hidden → PAUSED / END).
- `applyAudioGate(fromSilence)` is the one place audibility is decided. `fromSilence` (used by play/restart/FROM TOP) forces the incoming bed's fade fraction to 0 so every entrance is a full 1s fade; seamless switches fade from wherever the bed's fraction sits.
- Beds keep rolling muted while another is audible, so seamless switching stays in sync.
- Per-bed `sceneStart` offset support retained from the Drive variant but unused here.

## Open TODOs

- Verify the v1.1 crop on live: no chrome at play start, no black slivers, nothing important lost at frame edges.
- Trim per-bed `volume` by ear (YouTube normalisation means they will not arrive matched).
- Check every bed outlasts the scene from its start point.
- Confirm bed order actually reads glacial → frantic, or reorder in CONFIG.
- Confirm category (Miscellaneous assumed).

## Last updated

2026-08-06. v1.1.2: bed 1 start moved to 2:35, bed 2 replaced. v1.1.1: all three beds replaced during live testing. v1.1: asymmetric letterbox crop from screenshot measurements; embed height 660 → 545. v1.0: initial build from scene-scorer-drive v1.6.3, shipped untested for live evaluation.
