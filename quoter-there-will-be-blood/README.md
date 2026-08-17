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

v2, 2026-08-13. Category: Miscellaneous. Shipped. Copy final. Title is Dave's. No source credit supplied. Deployed to Pages, not yet embedded in Canvas.

## Clip

- Video ID `GBeiNFPNWQM`, There Will Be Blood ocean scene
- Quote content 1:10 to 2:20 (70s to 140s) at full volume, displayed length 1:10
- Fade-in runs 1:05 to 1:10, a smooth 5s ramp, then full at 1:10. Fade-out begins at 2:20 and is silent by 2:23.
- Timeline: 1:05 sound starts fading in from silence (video hidden under the card), 1:09.2 the card begins dissolving, 1:10 both audio and video fully up, hold to 2:20, 2:20 to 2:23 fade out.
- No silent lead. The sound fades in from the moment of play and leads the video reveal by about 4.2s, so it never feels like nothing is happening. The card still covers YouTube's overlay for 4.2s, which clears in time.
- Volume starts at 50%, `levelTrim` currently 0 dB

## Fade smoothness

The fade is driven off a wall clock, not off `player.getCurrentTime()`. YouTube only updates its reported time about four times a second, so a fade computed straight from it lands in roughly twelve coarse steps and sounds ragged. The poll now uses the reported time only to decide which phase it is in (fade-in, hold, fade-out) and runs the actual ramp off `performance.now()`, so the volume moves every 50ms poll. Measured over the fade-in: the old path made 18 volume changes with jumps up to 5 units at once, the new path makes 49 changes with a largest jump of 2.

`fadeInStart` and `fadeOutStart` hold the wall-clock anchors, set the first poll tick that enters each fade and reset on each play. This is instance-local, a good backport candidate for the shared engine since every quoter's fade runs through the same coarse-time path.

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
- Tune `levelTrim` by ear, the score is quiet.
- Confirm the folder name before it goes into Canvas.
- Note a backup video ID against takedown.

## Last updated

2026-08-13. Initial build and ship, then reworked the fade after Dave's feedback: rebuilt it off a wall clock so it is smooth not stepped, removed the silent lead so sound starts at play, and retimed so sound and video are both fully up by 1:10 with sound leading the video. Scope letterbox crop still expected.
