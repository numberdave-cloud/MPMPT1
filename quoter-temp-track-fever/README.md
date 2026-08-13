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
- Quote content 2:01 to 2:42 (121s to 162s), displayed length 0:41
- 2s silent lead, then 3s fade in, then hold, then 3s fade out. Actual playback runs 116s (1:56) to 165s (2:45).
- Timeline: 1:56 to 1:58 silent (video rolling, volume zero), 1:58 to 2:01 fade in, 2:01 to 2:42 full, 2:42 to 2:45 fade out.
- The silent lead and fade-in sit on the pre-roll before 2:01, so the quoted cue arrives clean at full volume exactly at 2:01. Same house style as the plain fade-in. The title card holds through the silent lead and the fade, dissolving as the music reaches full.
- Two pieces play back to back inside the window: the Kilar Dracula cue first, then the Eshkeri Stardust cue. The fade brings you into the first and out of the second. The cut between them sits untouched in the middle, which is the whole point of the quote, so do not fade across it.
- Volume starts at 50%, `levelTrim` currently 0 dB

## Source crop

Not needed. This source is a 16:9 native YouTube video essay, so `--zoom` is left at 1, a no-op. The crop machinery and the `?tune=1` panel are still present, inherited from the 2001 build, in case a framing quirk turns up on a real listen. At zoom 1 they do nothing.

## Silent lead

This instance uses `silentLead: 2`, a field not in the other quoters. It inserts silent seconds at the very front, before the fade-in, so the video rolls silent for 2s and then the audio fades up. `PLAY_START` moves back to carry it, `FADE_IN_AT` marks where the ramp actually begins, and `REVEAL_AT` holds the card across the lead plus the fade so it dissolves as the music arrives.

Interpretation worth confirming on a listen: the silent lead and the fade-in both sit on pre-2:01 content, so full volume lands exactly at 2:01 and the cue's attack is heard clean. If instead the intent was for the video to begin at 2:01, hold silent for 2s of the cue, then fade into it, that is a different setup: it plays the first 2s of the Dracula cue silently and fades into it slightly in. Say which you want after hearing it.

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
- Confirm the silent-lead interpretation above after a listen.
- Confirm the two copy edits above.
- Confirm the fade feel across the mid-clip cut between the two pieces.
- Confirm the folder name before it goes into Canvas.
- Live-test overlay flash suppression, fade feel, captions off.
- Note a backup video ID against takedown.

## Last updated

2026-08-13. Initial build, clip window 2:01 to 2:44 with 3s fades, crop reset to no-op, Dave's title, credit and copy in. Then moved the fade-out 2s earlier (end 2:44 to 2:42) and added a 2s silent lead before the fade-in.
