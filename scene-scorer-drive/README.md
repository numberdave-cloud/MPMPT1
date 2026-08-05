# Scene Scorer — Drive [Temp Track]

**Directory:** `scene-scorer-drive/`

A Scene Scorer variant built for the temp-track lesson: the Drive (2011) opening credits arrive with a temp track everyone is already in love with (Kavinsky's "Nightcall", baked into the scene upload), and the student flips between it and three beds that are nothing like it, or each other. Demonstrates how hard it is to hear past a beloved temp.

Built from the `scene-scorer/` template. One structural change: the scene's own audio is a selectable option. Index -1 is the TEMP TRACK button (scene unmuted, beds muted); selecting any bed mutes the scene audio entirely.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/scene-scorer-drive/

## Canvas embed

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/scene-scorer-drive/"
  width="100%"
  height="600"
  title="Scene Scorer — Drive [Temp Track]"
  style="border: none;"
  allow="autoplay"
  loading="lazy">
</iframe>
```

Height 600 since the v1.6 letterbox crop (the 2.35:1 window is ~90px shorter than the earlier 16:9 frame at typical Canvas widths). Was 680 pre-crop. Re-measure once live if Canvas shows a scrollbar.

## Build state

v1.1, 2026-08-05. Category: Miscellaneous. Shipped for live testing at Dave's request (local file:// testing doesn't work for this one); levels and bed lengths unverified.

## Config

- Scene: `BHVbbcHWX4k` (Drive opening credits, 2:46, same upload as `quoter-drive-opening-credits/` — shared takedown risk, see that README)
- MUSIC 1: `DqiVp0Nx5I4`, starts at 0:06 (mathcore)
- MUSIC 2: `EsvfptdFXf4` (Star Wars cantina swing)
- MUSIC 3: `dQw4w9WgXcQ`, bed starts at 0:00 but carries `sceneStart: 1` so the scene begins 1s in when chosen from the top (1987 pop)
- Default selection: TEMP TRACK. Bed labels deliberately blind so students judge by ear.
- All volumes 100, untrimmed.

## Interaction model (v1.1)

The selector is the primary control; the transport is demoted to a small quiet row beneath it. Two switching modes, toggled top-right of the selector:

- **FROM TOP** (default): pressing any source button resets the scene and every bed to their start points and plays. Pressing the active button again also restarts.
- **SEAMLESS**: the original Scene Scorer behaviour. Hot-switch between sources while the video keeps rolling; starts playback if stopped.

PLAY/PAUSE and RESTART remain for pausing mid-scene and for FROM TOP-equivalent restarts.

## MUSIC 3 first-trigger lockout

The first time MUSIC 3 is selected (per page load), every control locks for 15 seconds: selector, switch-mode toggle, pause, restart, and the volume knob. There is no visual indication of the lockout except one tell: pressing the pause button flashes it red. When the 15 seconds are up the pause button flashes green three times and everything answers again. Config constants `LOCK_TRACK` (index 2) and `LOCK_SECONDS` (15) at the top of the script. Once per page load only; subsequent MUSIC 3 selections behave normally.

## Technical notes

- Shared Scene Scorer machinery: four synced YT players, click-shield, caption kill, master volume knob scaling per-source volumes.
- The click-shield is fully inert here (no click-to-pause). Pausing lives in the transport button only.
- An opaque black cover (`#videoCover`) sits above the shield whenever the scene is not rolling, hiding YouTube's thumbnail/title chrome pre-start and the paused-state overlay. Status labels: LOADING → READY → (hidden while playing) → PAUSED / END. `play()` hides it, `pause()` and scene ENDED show it, so it never depends on YT state events for hiding (no flicker on FROM TOP re-seeks).
- `applyAudioGate()` is the one place audibility is decided; play/select/restart all route through it.
- Beds keep rolling muted while another source is audible, so seamless switching is instant and stays in sync.
- In FROM TOP mode `selectTrack()` seeks all four players before calling `play()`. The scene's seek target comes from `sceneStartFor(idx)`: a bed may define `sceneStart` to offset the scene against itself (MUSIC 3 uses 1s). RESTART honours the active bed's offset too. In SEAMLESS mode per-bed scene offsets cannot apply (the video keeps rolling), so MUSIC 3 rides 1s off its intended alignment there.
- Selector buttons are disabled until all players report ready.
- Scene ENDED pauses all beds.

## Open TODOs

- Trim per-bed `volume` by ear against the temp track.
- Check MUSIC 2 outlasts the 2:46 scene (some cuts of that piece run shorter).
- Confirm blind labels vs named labels.
- Confirm category (Miscellaneous assumed).
- Note: the parent `scene-scorer/` folder has no README and no INDEX.md row. Flagged 2026-08-05, not fixed here.

## Design-system pass (v1.5)

Brought in line with the Interval Trainer reference spec: rack-hardware card (24px radius, 2px near-black outer frame, 1px light stroke at 0.3 opacity inset 6px), transparent page background so the card sits on Canvas white, 6-8px corner radius on all controls and the video frame (video 8px with overflow clipped), segment-style volume readout (mono accent digits with glow over ghost "888"), transport buttons at off-white text with hierarchy carried by size not dimming.

## Letterbox crop (v1.6)

The film is ~2.35:1 inside the 16:9 upload, so YouTube's chrome (title card, share/watch-later icons, logo) paints in the baked black bars. The video window is cut to the picture and the 16:9 player oversized behind it. v1.6.1: the crop is asymmetric because YouTube's title/channel text hangs below the top bar. Frame is 2.6:1 with the player at `top: -28.4%`: the top crop is one bar plus ~4% of picture (buries the text), the bottom crop stays exactly one bar (logo hidden, no black sliver). Maths in the CSS comment. To verify live: no chrome at play start; embed height 600.

## Last updated

2026-08-05. v1.6.2: page background painted white after the transparent background rendered grey in Canvas (cross-origin iframes don't reliably composite transparency). v1.6.1: asymmetric letterbox crop (2.6:1 frame, top-biased) after channel text peeked in at the top on live. v1.6: letterbox crop clips YouTube chrome; embed height 680 → 600. Earlier same day: v1.5 design-system pass; v1.4 MUSIC 3 first-trigger 15s lockout; v1.3 inert shield + video cover; v1.2 per-track `sceneStart`; v1.1 selector promoted, transport demoted, switch-mode toggle.
