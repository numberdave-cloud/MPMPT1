# YouTube Quoter [Morricone Pan Pipe]

Directory: `quoter-morricone-pan-pipe/`

## What it plays
Sir Christopher Frayling discussing Ennio Morricone's use of pan pipe in the score for *Once Upon a Time in America*, quoted from a Channel 4 News segment. Chrome-free video quote with audio fades either side, a title-card curtain, and a one-section notes column.

## Live URL
https://numberdave-cloud.github.io/MPMPT1/quoter-morricone-pan-pipe/

## Canvas embed
Height 480 (family default). Measured rendered heights: 900px -> 355, 700px -> 294, 480px stacked -> 451. The default 480 covers all three.

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/quoter-morricone-pan-pipe/"
  width="100%"
  height="480"
  title="Ennio Morricone's Use of Pan Pipe"
  style="border: none;"
  allow="autoplay"
  loading="lazy">
</iframe>
```

## Quote config
- Video ID: `hcjnVyaIZXI`
- Start (full at): 254s (4:14)
- End (fade-out from): 293s (4:53)
- Fade-in: 5s, Fade-out: 7s, Silent lead: 0s
- Fade curve: 2 (smooth)
- Level trim: 0 dB (base volume 50%, template default)
- Resolved play window: begins at 249s (4:09, `start - fadeIn - silentLead`), stops at 300s (5:00, `end + fadeOut`)
- Length badge: 39s (`end - start`)

## Notes layout
One section, single paragraph, no listen prompt. Film title *Once Upon a Time in America* italicised on first mention.

## Technical notes
- Title-card curtain holds over YouTube's start-up overlay for `REVEAL_HOLD` seconds, then dissolves.
- Fades are curved (`fadeCurve` exponent), not linear, so they do not read as a cut.
- YouTube's `end` playerVar is set past the real end; the 50ms poll owns the true ending so the fade-out is not truncated.
- Captions force-unloaded on ready, on a timer, and on play.
- Source crop defaults to a no-op (16:9 native assumed). `?tune=1` opens the crop panel if the frame turns out letterboxed. Never seen by students.

## Open decisions / TODOs
- Level: `levelTrim` at 0 dB, to be trimmed by ear on the live URL.
- Crop: assumed 16:9 native, no crop applied. Confirm on the live URL; use `?tune=1` if the frame needs de-letterboxing.

## Last updated
2026-08-21. Built through the intake panel (one-section notes) and shipped. Level and crop pending live tuning.
