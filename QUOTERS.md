# YouTube Quoter Registry

Every YouTube Quoter instance in the repo. Read this before touching any quoter.

All instances share one machinery. Only four things differ per instance: the `QUOTE` config block, the notes prose in the markup, the page `<title>`, and the folder name. **A fix to the shared machinery must be applied to every folder listed below, not just the one being worked on.**

Category for all quoters: **Miscellaneous**.

## Instances

| Folder | Card title | Video ID | Quote | Length | Trim | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `youtube-quoter/` | Mark Korven playing the Apprehension Engine | `lzk-l8Gm0MY` | 32s to 1:04 | 0:32 | 0 dB | live, embedded in Canvas |
| `quoter-mick-gordon-doom-brief-1/` | Mick Gordon discussing the Doom brief | `U4FNBMZsqrY` | 2:33 to 4:12 | 1:39 | -6 dB | live, untested |
| `quoter-ruiner-instrumental-solo/` | Nine Inch Nails - Ruiner Instrumental Break | `RkT-aMgZvQI` | 2:44 to 3:51 | 1:07 | 0 dB | live, untested |
| `quoter-drive-opening-credits/` | Drive - Opening Credits | `BHVbbcHWX4k` | 0:05 to 1:27 | 1:22 | 0 dB | live, untested, fragile source |
| `quoter-2001-dawn-of-man/` | 2001: A Space Odyssey - The Dawn of Man | `ypEaGQb6dJk` | 6:02 to 7:40 | 1:38 | 0 dB | live, copy final, cropped source, fragile source |
| `quoter-temp-track-fever/` | Temp Track Fever: Ilan Vs. Wojciech | `IEfQ_9DIItI` | 2:02.5 to 2:41 | 0:39 | 0 dB | live, copy final, 4s locked-out silent lead, 16:9 native |
| `quoter-baby-driver/` | Baby Driver (2017) | `6XMuUVw7TOM` | 2:07 to 3:17 | 1:10 | 0 dB | live, copy final, 3s locked-out lead, crop assumed 16:9 |

Live URL pattern: `https://numberdave-cloud.github.io/MPMPT1/<folder>/`

## Naming

`youtube-quoter/` was the first and is already embedded in a live Canvas page, so its name stays. Everything after it uses `quoter-<subject>`, with a trailing index only where one was asked for. Do not rename `youtube-quoter/` without checking the Canvas embed first.

## Making a new one

1. Copy an existing quoter folder to `quoter-<subject>-<n>/`.
2. Change the `QUOTE` config block (see fields below).
3. Rewrite the notes prose in the markup, between the `NOTES` comment markers.
4. Change the page `<title>` so the repo stays greppable by title.
5. Add a row to the table above and a row to `INDEX.md`.
6. Write the folder's `README.md`.

## Config fields

| Field | Notes |
| --- | --- |
| `videoId` | YouTube ID only, not the full URL |
| `start` / `end` | seconds, quote content boundaries |
| `fadeIn` / `fadeOut` | seconds, audio fade either side. `0` for a hard cut |
| `fadeCurve` | `1` linear (abrupt), `2` smooth default, `3` very gradual |
| `levelTrim` | dB trim for this clip, set by ear. Negative to quieten |
| `title` | card title, the name given to the quote |
| `source` | credit text on the card. `''` hides it |
| `sourceUrl` | `''` auto-links to the video on YouTube |
| `showLength` | shows `end - start` on the card |
| `silentLead` | seconds of silence at the very front, before the fade-in. Default 0. Instance-local so far, see below |

## Levels

There is no automatic loudness normalisation and there cannot be. The IFrame API exposes no loudness data (Stats for Nerds is internal to YouTube's player UI), and the audio cannot be measured from outside because it sits in a cross-origin iframe, the same wall that blocks Web Audio analysis of YouTube audio.

YouTube applies its own normalisation but only ever turns loud content **down** toward roughly -14 LUFS. It never lifts quiet content. So levels still vary between clips, and each one needs `levelTrim` set by ear.

Reference: -3 dB is x0.71, -6 dB is x0.50, -9 dB is x0.36, -12 dB is x0.25.

## Shared machinery, known behaviours

- **Fades are curved, not linear.** Perceived loudness tracks roughly amplitude^0.6, so a linear amplitude ramp holds near full loudness for most of its length then collapses at the end, which reads as a cut. `fadeCurve` is the exponent.
- **Captions** are suppressed with `cc_load_policy: 0` *and* `unloadModule('captions')` / `unloadModule('cc')`, called on ready, twice more on a timer, and again on play. The policy flag alone is not enough: a viewer's account preference or the video's own default can switch them back on.
- **YouTube's start-up overlay** (title, channel, centre button, "More videos" strip, logo) fires on the play event, not on hover, so the click-shield cannot stop it. The title card is held over the video for `REVEAL_HOLD` seconds to cover it, then dissolves.
- **YouTube's `end` playerVar** is deliberately set past our own end. YouTube's segment stopping is imprecise and would otherwise truncate the fade-out. The 50ms poll owns the real ending.
- **The click-shield** swallows every mouse event so YouTube never registers a hover, which suppresses its chrome.
- **The PLAY / REPLAY button** hides by opacity, never `display`, so removing it does not reflow the card and shunt the title text.
- **Stacked layout** resets `flex` on both columns. In a column flex container `flex-basis` applies to height, so an unreset basis silently inflates the widget.

## Long notes blocks

The notes column, not the video, sets the widget height once the notes run long. `quoter-2001-dawn-of-man/` hit this: at the standard 258px column its notes ran 439px against a 324px video column. Widening the notes column to 360px, inside a 900px frame with a 440px video column, balanced the two and took the widget from 503px to 379px. Reach for column width before font size.

## Silent lead, instance-local

`quoter-temp-track-fever/` adds a `silentLead` field and the constants `SILENT_LEAD` and `FADE_IN_AT`, plus a silent-lead branch in the envelope poll. It plays the video silent for N seconds before the fade-in begins. `PLAY_START` moves back to carry it and `REVEAL_AT` holds the card across the lead so it dissolves as the music arrives.

The silent lead and fade-in sit on the pre-roll, so the quoted content still arrives clean at full volume at `start`. Default 0, a no-op for every other quoter. Good backport candidate for the shared engine alongside the crop.

## Source crop, instance-local

`quoter-2001-dawn-of-man/` adds `--zoom`, `--offx` and `--offy` to `:root` and sizes the iframe with them, to strip the letterbox off a source that arrives pillarboxed and letterboxed at once. It ships with a `?tune=1` panel for dialling the values.

This is not yet in the shared machinery. The other four folders are unchanged. It is a good candidate for backporting with `--zoom: 1` as the default, which is a no-op for sources that do not need it.

## Embed

Height 480 covers most instances in side-by-side layout. `quoter-2001-dawn-of-man/` uses 400 and `quoter-temp-track-fever/` and `quoter-baby-driver/` use 380, all after the wider-notes-column layout. Stacked (below 660px) heights vary with notes length, so re-measure per instance:

| Folder | 900px | 700px | 480px stacked |
| --- | --- | --- | --- |
| `youtube-quoter/` | 389 | 452 | ~600 |
| `quoter-mick-gordon-doom-brief-1/` | 389 | 326 | 439 |
| `quoter-ruiner-instrumental-solo/` | 389 | 329 | 537 |
| `quoter-drive-opening-credits/` | 389 | 380 | 567 |
| `quoter-2001-dawn-of-man/` | 379 | 462 | 645 |
| `quoter-temp-track-fever/` | 355 | 338 | 563 |
| `quoter-baby-driver/` | 355 | 294 | 501 |

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/<folder>/"
  width="100%"
  height="480"
  title="<card title>"
  style="border: none;"
  allow="autoplay"
  loading="lazy">
</iframe>
```

## Source durability

Quoter clips depend on the source video staying up. An unofficial or fan upload of commercial music is more likely to be removed than an official channel or a conference talk. If a source disappears the card shows a "could not be loaded" message rather than breaking, but the quote is gone. Prefer official uploads where one exists, and check any quoter that has been sitting unused for a while.

## Last updated

2026-08-13. Added `quoter-baby-driver/` (Baby Driver 2017, ColumbiaPicturesPH, 2:07 to 3:17, 3s locked-out lead, copy pending). Shared machinery unchanged.
