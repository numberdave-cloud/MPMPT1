# Quoter: There Will Be Blood

**Directory:** `quoter-there-will-be-blood/`

A YouTube Quoter instance. Plays a 1:07 window from There Will Be Blood (2007), the ocean scene where Daniel Plainview deduces that Henry is a fraud. The point of interest is the gap between the calm sunlit setting and Jonny Greenwood's dissonant score tracking Plainview's suspicion.

Built from the shared quoter template, copied from `quoter-baby-driver/`. See `QUOTERS.md` at repo root for the registry and shared machinery notes.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/quoter-there-will-be-blood/

## Canvas embed

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/quoter-there-will-be-blood/"
  width="100%"
  height="380"
  title="There Will Be Blood (2007) - Peachtree Dance Scene"
  style="border: none;"
  loading="lazy"
  allow="autoplay">
</iframe>
```

Height 380. Measured with the real copy: 355px from 900px wide upward, 338px at 800px, 379px at 700px, 584px stacked below 660px. Notes-driven height.

## Build state

v1, 2026-08-13. Category: Miscellaneous. Shipped. Copy final. Title is Dave's. No source credit supplied. Deployed to Pages, not yet embedded in Canvas.

## Clip

- Video ID `GBeiNFPNWQM`, There Will Be Blood ocean scene
- Quote content 1:13 to 2:20 (73s to 140s) at full volume, displayed length 1:07
- Fade-in begins at 1:10 and reaches full at 1:13. Fade-out begins at 2:20 and is silent by 2:23.
- Timeline: 1:07 to 1:10 silent and locked out (video rolling under the card, volume zero), 1:10 to 1:13 fade in, full at 1:13, hold to 2:20, 2:20 to 2:23 fade out
- `silentLead` 3s plus `fadeIn` 3s give a 6s card cover from play, so YouTube's overlay is never seen. Card dissolves at 1:13 as full volume arrives.
- Volume starts at 50%, `levelTrim` currently 0 dB

## Fade interpretation, needs confirming

Dave said "fade in from 1:10" and "fade out from 2:20". Read literally and symmetrically: both fades begin at those points. So the fade-in runs 1:10 to 1:13 and full volume lands at 1:13, and the displayed length reads 1:07 rather than 1:10 because the full-volume span is 1:13 to 2:20.

The other reading is full volume by 1:10 with the fade-in as pre-roll before it. That would pull in audio from before 1:10 (outside the stated window), so the literal reading was chosen to keep everything at or after 1:10. If full-by-1:10 is wanted instead, set `start` to 70 and `fadeIn` stays 3, and the length reads 1:10.

## Source crop, LIKELY NEEDED

There Will Be Blood is a 2.35:1 scope film, so this upload is almost certainly letterboxed, black bars top and bottom, inside the 16:9 player. `--zoom` is currently 1, a no-op, because the exact letterbox could not be measured from the build environment (YouTube will not load over `file://`).

Expected fix once confirmed on a live view: `--zoom` about 1.32 removes a standard 2.35:1 letterbox (`2.35 / 1.78`), cropping roughly 16 percent off each side. Use the `?tune=1` panel to dial it exactly, or send a screenshot and it can be measured precisely as was done for the 2001 instance. Do not assume 1.32 is exact until seen.

## Notes copy

Dave's copy, used as written apart from two silent fixes, both flagged:

- "Daniel Day Lewis" to "Daniel Day-Lewis" in the top paragraph, to match the hyphenated form Dave used in the prompt.
- "familiar dialog" to "familiar dialogue", Australian spelling.

The prompt sentence "Watch out for Daniel Day-Lewis' expressions change ..." reads a little awkwardly and may be a dictation artefact. Left as written; smooth it if wanted.

Top paragraph is the context in dim body style, prompt carries the `listen` class for the divider rule and brighter text. No film title appears in the body, so no `<em>` was needed.

## Layout

Frame `max-width` 900px, video column 440px, notes column 360px, inherited. Balanced at 291px each, widget height 355px.

## Technical notes

Shared machinery identical to every other quoter. Carries the instance-local `silentLead` and crop machinery.

- Third-party upload of a commercial film, so takedown risk is real. If it goes, the card shows the "could not be loaded" message. Note a backup video ID if needed.
- Scope film with a wide dynamic range and a quiet, dissonant score, so `levelTrim` may need lifting by ear so the low score is audible.

## Open TODOs

- Confirm the letterbox on a live view and apply the scope crop (about `--zoom: 1.32`).
- Supply a source credit / link title if one is wanted (currently none, credit line hidden).
- Confirm the fade interpretation and the 1:07 length readout.
- Tune `levelTrim` by ear, the score is quiet.
- Confirm the folder name before it goes into Canvas.
- Note a backup video ID against takedown.

## Last updated

2026-08-13. Initial build and ship. Clip 1:10 to 2:20 with 3s fades and a 3s locked-out lead, no crop yet (scope letterbox expected), Dave's title, no credit, copy in.
