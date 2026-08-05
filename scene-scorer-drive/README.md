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
  height="680"
  title="Scene Scorer — Drive [Temp Track]"
  style="border: none;"
  allow="autoplay"
  loading="lazy">
</iframe>
```

Height 680, not the default 600: the card stacks a 16:9 video, transport row, and a four-button selector, and at typical Canvas column widths the video alone is ~400px tall. Re-measure once live if Canvas shows a scrollbar.

## Build state

v1, 2026-08-05. Category: Miscellaneous. Shipped for live testing at Dave's request (local file:// testing doesn't work for this one); levels and bed lengths unverified.

## Config

- Scene: `BHVbbcHWX4k` (Drive opening credits, 2:46, same upload as `quoter-drive-opening-credits/` — shared takedown risk, see that README)
- MUSIC 1: `DqiVp0Nx5I4`, starts at 0:06 (mathcore)
- MUSIC 2: `EsvfptdFXf4` (Star Wars cantina swing)
- MUSIC 3: `dQw4w9WgXcQ` (1987 pop)
- Default selection: TEMP TRACK. Bed labels deliberately blind so students judge by ear.
- All volumes 100, untrimmed.

## Technical notes

- Shared Scene Scorer machinery: four synced YT players, click-shield, caption kill, master volume knob scaling per-source volumes.
- `applyAudioGate()` is the one place audibility is decided; play/select/restart all route through it.
- Beds keep rolling muted while another source is audible, so switching is instant and stays in sync.
- Scene ENDED pauses all beds.

## Open TODOs

- Trim per-bed `volume` by ear against the temp track.
- Check MUSIC 2 outlasts the 2:46 scene (some cuts of that piece run shorter).
- Confirm blind labels vs named labels.
- Confirm category (Miscellaneous assumed).
- Note: the parent `scene-scorer/` folder has no README and no INDEX.md row. Flagged 2026-08-05, not fixed here.

## Last updated

2026-08-05. Initial ship for live testing.
