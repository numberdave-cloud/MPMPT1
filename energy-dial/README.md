# Energy Dial

**Directory:** `energy-dial/`

One running scene, three music beds at different energy levels. The student flips between beds and hears how energy recontextualises the same footage. Extension of the Scene Scorer cue-audition family. Home: B1·W3 (energy and style page).

## Live URL

https://numberdave-cloud.github.io/MPMPT1/energy-dial/

## Canvas embed

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/energy-dial/"
  width="100%"
  height="660"
  title="Energy Dial"
  style="border: none;"
  allow="autoplay"
  loading="lazy">
</iframe>
```

Height 660, not the default 600: the plain 16:9 video window makes the card ~648px tall at full width (the Drive variant's 600 relies on its letterbox crop). Re-measure if a crop is applied later.

## Build state

v1.0, 2026-08-06. Category: Miscellaneous (assumed, unconfirmed). Shipped for live testing at Dave's request (YouTube refuses file:// referrers, live origin is the only test bench). Levels, bed lengths, and the scene upload's aspect ratio all unverified.

## Config

- Scene: `6z9qws7M8q8`, starts at 1:12 (72s), audio permanently muted
- ENERGY 1: `AIRX176j2CA`, starts at 0:24
- ENERGY 2: `oRSijEW_cDM`, starts at 0:00
- ENERGY 3: `6kN4zRfnHm8`, starts at 0:09
- Default selection: ENERGY 1. Labels deliberately unranked (no GLACIAL/FRANTIC) so students judge energy by ear.
- All volumes 100, untrimmed.
- `fadeInMs: 1000`, `fadeOutMs: 150`, `fadeExp: 2` in CONFIG.

## Interaction model

Inherited from `scene-scorer-drive/` v1.1: selector is the primary control, transport demoted beneath it. FROM TOP (default) resets scene and beds to their start points on any selection; SEAMLESS hot-switches while the video rolls. PLAY/PAUSE, RESTART, master volume knob with segment readout.

## Differences from scene-scorer-drive

- No TEMP TRACK button; the scene's own audio is muted at all times.
- No first-trigger lockout.
- Fade engine: every bed entrance fades in over 1s on a power curve (`frac^fadeExp` applied to the per-bed volume, master knob still effective mid-fade); outgoing bed drops over 150ms on a seamless switch, then mutes. Single 30ms interval drives all fades and stops itself when idle.
- Plain 16:9 video window, no letterbox crop. If the upload is letterboxed and YouTube paints chrome in the baked bars, port the asymmetric crop from scene-scorer-drive v1.6.1 and re-measure the embed height.

## Technical notes

- Shared Scene Scorer machinery: four synced YT players, inert click-shield, caption kill, opaque `#videoCover` whenever the scene is not rolling (LOADING → READY → hidden → PAUSED / END).
- `applyAudioGate(fromSilence)` is the one place audibility is decided. `fromSilence` (used by play/restart/FROM TOP) forces the incoming bed's fade fraction to 0 so every entrance is a full 1s fade; seamless switches fade from wherever the bed's fraction sits.
- Beds keep rolling muted while another is audible, so seamless switching stays in sync.
- Per-bed `sceneStart` offset support retained from the Drive variant but unused here.

## Open TODOs

- Verify all four videos load and stay in sync on live.
- Trim per-bed `volume` by ear (YouTube normalisation means they will not arrive matched).
- Check every bed outlasts the scene from its start point.
- Confirm the scene upload's aspect; apply crop if chrome intrudes.
- Confirm bed order actually reads glacial → frantic, or reorder in CONFIG.
- Confirm category (Miscellaneous assumed).

## Last updated

2026-08-06. v1.0: initial build from scene-scorer-drive v1.6.3. Shipped untested for live evaluation.
