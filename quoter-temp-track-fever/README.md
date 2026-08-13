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

Height 380. Measured with the real copy: 355px from 900px wide upward, 326px at 800px, 338px at 700px, 563px stacked below 660px. Timing changes do not affect height. 380 gives a small buffer at normal Canvas desktop width. Below about 780px wide the widget scrolls inside the frame. Use 590 if the Canvas mobile app matters for this page.

## Build state

v1, 2026-08-13. Category: Miscellaneous. Copy final. Card title and source credit are Dave's, as given. Deployed for live testing, not yet embedded in Canvas.

## Clip

- Video ID `IEfQ_9DIItI`, Every Frame a Painting, roughly 4:30 long
- Quote content 2:02.5 to 2:41 (122.5s to 161s), displayed length 0:39. The Dracula theme starts at 2:02.5.
- Timeline: 1:56.5 to 2:00.5 silent and visually locked out (video rolling under the title card, volume zero), 2:00.5 to 2:02.5 fade in, full at 2:02.5 as the theme starts, hold to 2:41, 2:41 to 2:43 fade out, silent by 2:43.
- The silent lead runs 4s and the fade-in 2s, so the title card covers the video for a full 6s from the moment of play. YouTube's start-up overlay fires at play and clears within 3 to 4s, so it is never seen. The card dissolves at 2:02.5 as the music arrives.
- Two pieces play back to back inside the window: the Kilar Dracula cue first, then the Eshkeri Stardust cue. The cut between them sits untouched in the middle, which is the whole point of the quote, so do not fade across it.
- Volume starts at 50%, `levelTrim` currently 0 dB

## Source crop

Not needed. This source is a 16:9 native YouTube video essay, so `--zoom` is left at 1, a no-op. The crop machinery and the `?tune=1` panel are still present, inherited from the 2001 build, in case a framing quirk turns up on a real listen. At zoom 1 they do nothing.

## Silent lead and lockout

This instance uses `silentLead: 4`, a field not in the other quoters. It plays the video silent for 4s before the 2s fade-in begins, and `REVEAL_AT` holds the title card across the whole 6s so YouTube's overlay is never seen. The card dissolves as the music reaches full volume at 2:02.5.

`silentLead` is the lever if any overlay ever peeks through: raise it and the lockout grows, the card still dissolving at `start`. `start` is deliberately 2:02.5, the exact moment the Dracula theme begins, so full volume lands on the theme's first note.

The silent lead and fade-in sit on the pre-2:02.5 content, so the quoted theme arrives clean at full volume. The 2s fade-in therefore rides over whatever is in the source at 2:00.5 to 2:02.5, the run-up to the theme. Confirm that run-up is quiet enough on a listen; if it carries audible narration, the fade will lift it slightly before the theme.

The field defaults to 0 elsewhere, so it is a no-op for every other quoter. Good candidate to backport into the shared engine alongside the crop.

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
- Confirm on a listen: theme entry clean at 2:02.5, overlay fully hidden, silent by 2:43.
- Confirm the two copy edits above.
- Confirm the fade feel across the mid-clip cut between the two pieces.
- Confirm the folder name before it goes into Canvas.
- Live-test overlay flash suppression, fade feel, captions off.
- Note a backup video ID against takedown.

## Last updated

2026-08-13. Initial build, then retimed twice. Now: Dracula theme start at 2:02.5 with full volume landing there, a 4s silent and locked-out lead plus a 2s fade-in (6s of card cover so the YouTube overlay is never seen), and a fade-out ending silent at 2:43.
