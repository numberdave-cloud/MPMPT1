# Quoter: History of the Ring Theme

**Directory:** `quoter-lotr-history-of-the-ring/`

A YouTube Quoter instance. Plays a window from The Lord of the Rings: The Fellowship of the Ring (2001), the Bag End scene where Frodo picks up Bilbo's ring and Gandalf seals it in an envelope. The point of interest is the entrance of Howard Shore's History of the Ring theme as Frodo lifts the ring.

Built from the shared quoter template, copied from `quoter-there-will-be-blood/`. See `QUOTERS.md` at repo root for the registry and shared machinery notes.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/quoter-lotr-history-of-the-ring/

## Canvas embed

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/quoter-lotr-history-of-the-ring/"
  width="100%"
  height="400"
  title="Appearance of the History of the Ring Theme"
  style="border: none;"
  loading="lazy"
  allow="autoplay">
</iframe>
```

Height 400. Measured with the real copy: 355px from 900px wide, 294px at 700px, 476px stacked below 660px. Notes are short, so the video column drives the height here, not the notes.

## Build state

v1, 2026-08-18. Category: Miscellaneous. Shipped. Copy final (Dave's, two fixes flagged below). Deployed to Pages, not yet embedded in Canvas. Audio level and scope crop untested (YouTube will not load over `file://`, so both need a live check).

## Clip

- Video ID `whF2na8AIbw`, LOTR Fellowship, Bag End ring pickup
- Quote content 0:29 to 1:38 (29s to 98s) at full volume, displayed length 1:09
- Play begins at 0:24. Audio fades in 0:24 to 0:29 under the title card, then full at 0:29. No silent lead.
- Video is held under the card for 5.0s (`REVEAL_HOLD`) so YouTube's start-up chrome clears before the reveal. Card dissolves 0:29 to 0:29.8, video fully shown ~5.8s after play. Audio leads the reveal.
- Fade-out begins at 1:38, silent by 1:41.
- Base volume 70%. `levelTrim` 0 dB.

## Reveal timing, why 5.0s

`REVEAL_HOLD` is 5.0 here, up from the 4.2 used elsewhere. Dave's brief was explicit that no chrome should appear before the video is revealed, so the card holds an extra margin. The fade-in is 5s to match, so the audio reaches full right as the reveal completes. If any chrome still peeks through on a live view, bump `REVEAL_HOLD` and lift `fadeIn` to keep them aligned.

## Fade smoothness

Inherited from the There Will Be Blood build: the fade runs off a wall clock (`performance.now()`), not off `player.getCurrentTime()`, so it moves every 50ms poll rather than in the coarse ~4-per-second steps YouTube reports. `fadeInStart` / `fadeOutStart` hold the anchors, reset on each play. Instance-local, a backport candidate for the shared engine.

## Source crop, LIKELY NEEDED

Fellowship is a 2.35:1 scope film, so this upload is almost certainly letterboxed with black bars top and bottom inside the 16:9 player. `--zoom` is currently 1, a no-op, because the letterbox cannot be measured from the build environment. Expected fix: `--zoom` about 1.32 removes a standard 2.35:1 letterbox (`2.35 / 1.78`), cropping roughly 16 percent off each side. Use the `?tune=1` panel to dial it, or send a screenshot for an exact measure as done for the 2001 instance. Do not assume 1.32 until seen.

## Notes copy

Dave's copy, used as written. Two fixes, both flagged at build:

- Title `Appearaqnce` to `Appearance`, and title-cased to "Appearance of the History of the Ring Theme".
- Source credit was given as `LOTR - Hobbit`. The scene is Fellowship of the Ring (2001), not The Hobbit, so the card credit was corrected to "The Lord of the Rings: The Fellowship of the Ring (2001)".

No film title appears in the notes body, so no `<em>` was needed. Top paragraph is context in dim body style; second paragraph carries the `listen` class for the divider rule and brighter text.

## Layout

Frame `max-width` 900px, video column 440px, notes column 360px, inherited from the template.

## Technical notes

Shared machinery identical to every other quoter. Carries the instance-local `silentLead` and crop machinery.

- Third-party upload of a commercial film, so takedown risk is real. If the source goes, the card shows the "could not be loaded" message. Note a backup video ID if one is found.

## Open TODOs

- Confirm the letterbox on a live view and apply the scope crop (about `--zoom: 1.32`).
- Tune `levelTrim` by ear against the 70% base once heard.
- Confirm chrome is fully covered on a live view; bump `REVEAL_HOLD` if not.
- Decide whether the displayed length should read 1:09 (current, full-volume window) or 1:14 (full played window incl. the fade-in).
- Note a backup video ID against takedown.
- Confirm the folder name before it goes into Canvas.

## Last updated

2026-08-18. Initial build and ship. Copied from There Will Be Blood, retimed to play from 0:24 with a 5s audio fade-in under a 5s card hold so no chrome shows before the reveal, quote to 1:38, base volume 70%, source credit corrected to Fellowship.
