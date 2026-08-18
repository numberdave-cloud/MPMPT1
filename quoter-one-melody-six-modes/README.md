# Quoter: One Melody Across Six Modes

**Directory:** `quoter-one-melody-six-modes/`

A YouTube Quoter instance. Plays a Max Konyi demonstration of the same melody and accompaniment cycled through six modes, so students can compare the feeling of each. Tied to the leitmotif task: the closing note asks which mode might suit the student's own leitmotif.

Built from the shared quoter template, copied from `quoter-lotr-history-of-the-ring/`. See `QUOTERS.md` at repo root for the registry and shared machinery notes.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/quoter-one-melody-six-modes/

## Canvas embed

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/quoter-one-melody-six-modes/"
  width="100%"
  height="400"
  title="One melody across six modes"
  style="border: none;"
  loading="lazy"
  allow="autoplay">
</iframe>
```

Height 400. Measured with the real copy: 355px from 900px wide, 294px at 700px, 476px stacked below 660px. Short notes, so the video column sets the height.

## Build state

v1, 2026-08-18. Category: Miscellaneous. Shipped. Copy final (Dave's, used as written). Deployed to Pages, not yet embedded in Canvas. Audio level untested (YouTube will not load over `file://`).

## Clip

- Video ID `4n-O95j05WM`, Max Konyi, one melody across six modes
- Quote content 0:05 to 2:09 (5s to 129s) at full volume, displayed length 2:04
- Plays from 0:00. Audio fades in 0:00 to 0:05 under the title card, full at 0:05. No silent lead.
- Video held under the card for 5.0s (`REVEAL_HOLD`) so YouTube's start-up chrome clears before the reveal. Card dissolves 0:05 to 0:05.8, video fully shown ~5.8s after play.
- Fade-out begins at 2:09 and runs 7s, silent by 2:16.
- Base volume 50% (template default). `levelTrim` 0 dB.

## Fade-in over the opening

Playing from 0:00 with a 5s fade-in means the first mode's melody eases in under the card rather than hitting at full. This is the cost of hiding YouTube's chrome from a cold start. If the opening statement feels undercut on a live listen, shorten `fadeIn`. `REVEAL_HOLD` can stay 5.0 independently, so the chrome stays hidden either way.

## Fade-out

7s fade-out (2:09 to 2:16), longer than the usual 3s because Dave set an explicit stop point 7s after the fade begins. Runs on the same smooth wall-clock path (`performance.now()`) as the other recent instances, so it moves every 50ms rather than in YouTube's coarse reported-time steps. `fadeCurve` is 2 (smooth); a 7s ramp could go to 3 (very gradual) if it reads as holding too long before dropping.

## Notes copy

Dave's copy, used as written. Top paragraph is context in dim body style; second paragraph carries the `listen` class for the divider rule and brighter text. No film title in the body, so no `<em>` needed.

## No crop needed

This is a music-theory demonstration, not a scope film, so there is no letterbox to strip. `--zoom` stays 1, a no-op. The crop machinery is present (inherited) but unused.

## Source durability

Source is Max Konyi's own channel (verified: youtube.com/maxkonyi, maxkonyi.com), not a third-party re-upload of commercial media, so takedown risk is low compared with the film-clip quoters. If it ever goes, the card shows the "could not be loaded" message.

## Layout

Frame `max-width` 900px, video column 440px, notes column 360px, inherited from the template.

## Open TODOs

- Tune `levelTrim` by ear against the 50% base once heard on live.
- Confirm chrome is fully covered on a live view; bump `REVEAL_HOLD` if not.
- Decide whether the opening fade-in should be shortened if it undercuts the first mode's melody.
- Decide whether the displayed length should read 2:04 (current, full-volume window) or 2:16 (full played window incl. the fade-in), or hide it.

## Last updated

2026-08-18. Initial build and ship. Copied from the History of the Ring quoter, retimed to play from 0:00 with a 5s fade-in under a 5s card hold so no chrome shows, quote to 2:09 with a 7s fade-out stopping at 2:16, base volume reset to 50%, source Max Konyi.
