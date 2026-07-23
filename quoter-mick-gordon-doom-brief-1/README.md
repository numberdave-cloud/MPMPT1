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

v1, 2026-07-22. Config clone of `youtube-quoter/` v4. Untested live. Notes listening prompt is a DRAFT.

## Current clip

- Video ID `U4FNBMZsqrY`, GDC 2017 "DOOM: Behind the Music"
- Quote content 2:33 to 4:12 (153s to 252s), displayed length 1:39
- 3s fade in and 3s fade out, so actual playback runs 150s to 255s
- Card title "Mick Gordon discussing the Doom brief", credit "GDC Festival of Gaming" linking to the source video
- Volume starts at 50%

## Notes copy

Paragraph one is Dave's wording, used as given. The listening prompt beneath it is a draft.

The notes deliberately do not state what the brief actually was. The clip says it, and saying it in the panel first would remove the reason to listen.

## Technical notes

Identical to `youtube-quoter/`. See that README for the full account of the click-shield, the title card and curtain, the manual audio fades, and the YouTube `end` backstop. Points that matter for this instance specifically:

- The source URL carried `&t=1560s` (26:00) when supplied, which does not match the 2:33 quote point. Built to the explicitly stated times. Worth confirming on first play that 2:33 is the intended moment.
- The talk lives on the official GDC YouTube channel. The card credit reads "GDC Festival of Gaming" as specified. Adjust `source` in the config if a different credit is wanted.
- `REVEAL_AT` lands at 154.2s, comfortably inside a 99s quote, so the video is visible for the bulk of it.

## Open TODOs

- Assign a category (Composition / Mixing / Arranging / Miscellaneous). Currently TBC in `INDEX.md`.
- Confirm the 2:33 start is the intended moment.
- Approve or rewrite the listening prompt.
- Confirm the source credit wording.
- Live-test: overlay flash suppression, fade feel, embed height.

## Last updated

2026-07-22. Initial build. Config clone of the v4 quoter template with the Mick Gordon GDC clip, new card text, new notes, and a distinct page title.
