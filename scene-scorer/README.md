# Score Switcher

Directory: `scene-scorer/`
Category: Miscellaneous

## What it does
A fixed dialogue scene (Shawshank Redemption) plays with three swappable music
beds underneath it. Students audition each bed against the same picture to hear
how a score changes the read of a scene. Dialogue and beds run on synced,
volume-balanced YouTube players; a master Vol knob scales the whole mix.

Note: the eyebrow reads SCORE SWITCHER. The folder stays `scene-scorer/` (it is
Canvas-embedded under that path). Do not rename the folder without spinning a new
one and updating every embed.

## Live URL
https://numberdave-cloud.github.io/MPMPT1/scene-scorer/

## Canvas embed
Height 630 (not the 600 default): the video is an uncropped 16:9 player, so the
card is taller than the letterboxed `scene-scorer-drive` sibling. Card height is
bounded because `max-width: 740` stops the video growing past ~416px tall, so 630
clears the tallest case.

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/scene-scorer/"
  title="Score Switcher"
  width="100%"
  height="630"
  style="border: none;"
  allow="autoplay"
  loading="lazy"></iframe>
```

## Build state
Live. Shared rack frame applied (matches the newer devices).

## Technical notes
- YouTube IFrame API drives one scene player plus one hidden player per bed.
  Playback is kept in sync; a transparent click-shield over the video swallows
  clicks so the native YouTube play/pause can't desync the beds.
- Captions are force-unloaded on start (`unloadModule('captions')` / `'cc'`).
- Config lives in the `CONFIG` block near the top of the script and is the only
  thing edited per scene: `scene.id`, per-bed `id`/`volume`/`label`/`start`, and
  `startWith`.
- `startWith: 'none'` — the scene opens dry (no bed). Students select a bed
  deliberately. `startWith: 0..n` would auto-play that bed instead.
- The Vol knob is a MASTER control: it scales the scene and the active bed
  together via `effVol()`, so the per-bed balance set in CONFIG is preserved.
- Page background is transparent so the rounded card floats on Canvas' own
  wrapper. Do not set a page background colour: a fixed value shows as a
  mismatched slab inside the Canvas wrapper.
- Frame: `.rack` at 24px radius, 2px near-black outer border, inset 1px light
  stroke at 18px via `::after`. Video frame corners clipped at 8px.
- No base64 audio here: all sound comes from YouTube, so the CSP audio rules
  (atob over fetch, OGG loops) do not apply to this MOTE.

## Open decisions / TODO
- Levels: per-bed volumes (71 / 100 / 40) and scene volume (100) were set by ear
  and have not been re-checked against the rounded build. Verify on the live page.
- The Drive sibling (`scene-scorer-drive/`) carries a letterbox crop; this one
  does not. If a future scene here is widescreen film, port the crop across.

## Last updated
2026-08-13 — Applied shared rack frame, renamed eyebrow to SCORE SWITCHER,
changed default accompaniment to none. Added this README and an INDEX row (the
folder was previously uncatalogued).
