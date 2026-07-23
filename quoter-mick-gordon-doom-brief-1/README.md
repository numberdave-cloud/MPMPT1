# Quoter: Mick Gordon, The Doom Brief

**Directory:** `quoter-mick-gordon-doom-brief-1/`

A YouTube Quoter instance. Plays one fixed segment of a single YouTube video and nothing else, with all YouTube chrome and click-through stripped out. This one quotes Mick Gordon at GDC describing the brief id Software gave him for the DOOM score.

Built from the `youtube-quoter/` template. Shared machinery is identical; only the config block, the notes prose, and the page `<title>` differ.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/quoter-mick-gordon-doom-brief-1/

## Canvas embed

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/quoter-mick-gordon-doom-brief-1/"
  width="100%"
  height="480"
  title="Mick Gordon discussing the Doom brief"
  style="border: none;"
  allow="autoplay"
  loading="lazy">
</iframe>
```

Height 480 (below the 600 default). Measured content heights for this instance:

| Column width | Layout | Height needed |
|---|---|---|
| 900px | side by side | ~389px |
| 700px | side by side | ~326px |
| 480px | stacked | ~505px |

480 covers every side-by-side case. Below 660px the notes drop beneath the video and it wants ~520. Heights differ per quoter because the notes prose length differs; 480 is the shared safe desktop number across quoter instances so far.

## Build state

v2, 2026-07-22. Category: Miscellaneous. Untested live.

## Current clip

- Video ID `U4FNBMZsqrY`, GDC 2017 "DOOM: Behind the Music"
- Quote content 2:33 to 4:12 (153s to 252s), displayed length 1:39
- 3s fade in and 3s fade out, so actual playback runs 150s to 255s
- Card title "Mick Gordon discussing the Doom brief", credit "GDC Festival of Gaming" linking to the source video
- Volume starts at 50%, with a -6 dB `levelTrim` applied (STARTING GUESS, tune by ear)

## Notes copy

Approved wording, used as given. A drafted listening prompt was removed: it described something the clip does not cover.

The notes deliberately do not state what the brief actually was. The clip says it.

## Technical notes

Identical to `youtube-quoter/`. See that README for the full account of the click-shield, the title card and curtain, the manual audio fades, and the YouTube `end` backstop. Points that matter for this instance specifically:

- The source URL carried `&t=1560s` (26:00) when supplied. Confirmed as incidental; 2:33 to 4:12 are the correct times.
- The talk lives on the official GDC YouTube channel. The card credit reads "GDC Festival of Gaming" as specified. Adjust `source` in the config if a different credit is wanted.
- `REVEAL_AT` lands at 154.2s, comfortably inside a 99s quote, so the video is visible for the bulk of it.

## Open TODOs

- Tune `levelTrim` by ear. Currently -6 dB as a starting guess.
- Confirm the curved fade now reads as a fade rather than a cut.
- Confirm captions stay off.
- Confirm the source credit wording ("GDC Festival of Gaming"; the talk sits on the official GDC channel).
- Live-test overlay flash suppression and embed height.

## Last updated

2026-07-22. Removed the incorrect listening prompt. Fades are now curved rather than linear, which fixes them sounding abrupt. Added per-clip `levelTrim`, set to -6 dB here. Captions now force-unloaded, not just policy-flagged. Slider moves mid-fade no longer punch the level back to full. Category set to Miscellaneous.
