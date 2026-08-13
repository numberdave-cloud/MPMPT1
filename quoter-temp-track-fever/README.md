# Quoter: Temp Track Fever

**Directory:** `quoter-temp-track-fever/`

A YouTube Quoter instance. Plays a 43-second window from Every Frame a Painting's supplementary video on temp scores, the companion piece to their Marvel Symphonic Universe essay. The clip sets a Wojciech Kilar cue from Bram Stoker's Dracula against Ilan Eshkeri's Stardust score to show how a temp track's shadow survives into the final music.

Built from the shared quoter template, copied from `quoter-2001-dawn-of-man/`. See `QUOTERS.md` at repo root for the registry and shared machinery notes.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/quoter-temp-track-fever/

## Canvas embed

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/quoter-temp-track-fever/"
  width="100%"
  height="380"
  title="Temp Track Fever: Ilan Vs. Wojciech"
  style="border: none;"
  loading="lazy"
  allow="autoplay">
</iframe>
```

Height 380. Measured with the real copy: 355px from 900px wide upward, 326px at 800px, 338px at 700px, 563px stacked below 660px. 380 gives a small buffer at normal Canvas desktop width. Below about 780px wide the widget scrolls inside the frame. Use 590 if the Canvas mobile app matters for this page.

## Build state

v1, 2026-08-13. Category: Miscellaneous. Copy final. Card title and source credit are Dave's, as given. Deployed for live testing, not yet embedded in Canvas.

## Clip

- Video ID `IEfQ_9DIItI`, Every Frame a Painting, roughly 4:30 long
- Quote content 2:01 to 2:44 (121s to 164s), displayed length 0:43
- 3s fade in and 3s fade out, so actual playback runs 118s to 167s
- Two pieces play back to back inside the window: the Kilar Dracula cue first, then the Eshkeri Stardust cue. The fade brings you into the first and out of the second. The cut between them sits untouched in the middle, which is the whole point of the quote, so do not fade across it.
- Volume starts at 50%, `levelTrim` currently 0 dB

## Source crop

Not needed. This source is a 16:9 native YouTube video essay, so `--zoom` is left at 1, a no-op. The crop machinery and the `?tune=1` panel are still present, inherited from the 2001 build, in case a framing quirk turns up on a real listen. At zoom 1 they do nothing.

## Notes copy

Dave's copy, used as written apart from two changes, both flagged to him:

- "composed for the film by by Ilan Eshkeri" to "by Ilan Eshkeri". Dictation doubling.
- A comma added after "Listening to the two pieces".

Film titles (Stardust, Bram Stoker's Dracula) are wrapped in `<em>` on first mention, which the notes stylesheet renders as italic in full-strength text. Paragraph one is context in the dim body style. Paragraph two carries the `listen` class, which gives it the divider rule and brighter text, and holds the three questions.

## Layout

Frame `max-width` 900px, video column 440px, notes column 360px, inherited from `quoter-2001-dawn-of-man/`. This copy is shorter, so the two columns land dead even at 291px each and the widget comes to 355px with no rebalancing needed.

## Technical notes

Shared machinery identical to every other quoter.

- Source is an official-ish channel upload (Every Frame a Painting's own channel), so more durable than a fan upload, but the channel went largely dormant after 2016 and had a copyright history, so not risk-free. If it goes, the card shows the "could not be loaded" message. Note a backup video ID if one is needed.
- Video essay audio tends to sit at a consistent level, so `levelTrim` may well stay at 0, but confirm by ear against the other cards.

## Open TODOs

- Tune `levelTrim` by ear.
- Confirm the two copy edits above.
- Confirm the fade feel across the mid-clip cut between the two pieces.
- Confirm the folder name before it goes into Canvas.
- Live-test overlay flash suppression, fade feel, captions off.
- Note a backup video ID against takedown.

## Last updated

2026-08-13. Initial build from the current quoter template. Clip window 2:01 to 2:44, 3s fades, crop reset to no-op, Dave's title, credit and copy in.
