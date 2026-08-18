# YouTube Quoter [Spielberg & Williams on Jaws]

Directory: `quoter-spielberg-williams-jaws/`

A YouTube Quoter: a chrome-free, fade-topped video quote with a title-card
curtain and a notes column beside it. Plays a fixed segment of one video with
audio fades either side, then stops.

## Live URL
https://numberdave-cloud.github.io/MPMPT1/quoter-spielberg-williams-jaws/

## Canvas embed
Height 480 is the family default and covers this instance. Measured rendered
heights: 355px at 900px wide, 294px at 700px, 451px stacked at 480px. The notes
are short and one-section, so the video column drives the height.

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/quoter-spielberg-williams-jaws/"
  width="100%"
  height="480"
  title="Spielberg & Williams on Jaws"
  style="border: none;"
  allow="autoplay"
  loading="lazy">
</iframe>
```

## Build state
v1.0. Built from the canonical quoter template (`quoter-one-melody-six-modes/`),
config, title and notes swapped. First quoter built through the intake panel.

## What it plays
Steven Spielberg and John Williams discussing the music of Jaws, from The Late
Show with Stephen Colbert. YouTube ID `YTKs0JRVlrQ`.

## Quote and fade
Intake values: full at 4:18, fade-out from 5:16, 6s fade-in, 7s fade-out, no
silent lead, smooth curve, length shown.

Resolved:
- `start` 258 (4:18), audio fully up.
- `end` 316 (5:16), fade-out begins.
- Play begins at 4:12 (start minus the 6s fade-in), under the title card.
- Fade-out runs 5:16 to 5:23, then stops.
- Length badge reads 0:58 (end minus start).
- `fadeCurve` 2 (smooth), `levelTrim` 0, base volume 50%.

## Notes
One section, no divider. Single block, no listen prompt. Jaws italicised on
first mention.

## Technical notes
- Video and audio come from the YouTube IFrame API, not embedded. Chrome is
  suppressed by a click-shield plus caption unloading; the title card is held
  over the video for the first few seconds to cover YouTube's start-up overlay,
  then dissolves.
- Fade envelope is curved (`fadeCurve`), not linear, since a linear amplitude
  ramp reads as a cut.
- Source crop (`--zoom`, `--offx`, `--offy`) is at the no-op default. A `?tune=1`
  panel is built in for dialling it by eye if the source needs de-letterboxing.

## Open decisions / TODOs
- Level not yet checked live. It is spoken interview audio, so the base volume
  may want lifting; trim by ear on the live URL.
- Source crop not checked. Add `?tune=1` to the URL if the frame needs it.

## Last updated
18 August 2026 (v1.0). Built via the intake panel. Quote 4:18 to 5:16, 6s/7s
fades, one-section notes.
