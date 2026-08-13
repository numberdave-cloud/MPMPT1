# Quoter: 2001, The Dawn of Man

**Directory:** `quoter-2001-dawn-of-man/`

A YouTube Quoter instance. Plays a 1:38 window from the Dawn of Man sequence of 2001: A Space Odyssey (1968), fading in and out either side so the clip is heard as a quote rather than a chunk of a longer video.

Built from the shared quoter template, copied from `quoter-drive-opening-credits/`. See `QUOTERS.md` at repo root for the registry and shared machinery notes.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/quoter-2001-dawn-of-man/

## Canvas embed

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/quoter-2001-dawn-of-man/"
  width="100%"
  height="480"
  title="2001: A Space Odyssey - The Dawn of Man"
  style="border: none;"
  loading="lazy"
  allow="autoplay">
</iframe>
```

Height 480. Measured with the current placeholder notes: 388px at 900px wide, 326px at 700px, 497px stacked below 660px. Re-measure once the real notes copy lands, since notes length drives the stacked height.

## Build state

v1, 2026-08-13. Category: Miscellaneous. Deployed for live testing only. Not yet embedded in Canvas. Card title, source credit and notes copy are all placeholders awaiting Dave.

## Current clip

- Video ID `ypEaGQb6dJk`, a third-party upload of the Dawn of Man sequence, roughly 9:33 long
- Quote content 6:02 to 7:40 (362s to 460s), displayed length 1:38
- 3s fade in and 3s fade out, so actual playback runs 359s to 463s
- `PLAY_START` 359, `REVEAL_AT` 363.2, so the title card lifts 1.2s after full volume arrives
- Volume starts at 50%, `levelTrim` currently 0 dB

## Fade interpretation, needs confirming

The brief read "start fade from 6:02, fade out at 7:40". Two readings were possible and the template convention was followed: 6:02 and 7:40 are the boundaries of the fully audible quote, with the fades sitting outside them. Audio therefore begins creeping in at 5:59 and finishes decaying at 7:43.

The other reading is fades inside the window: silence at 6:02 rising to full at 6:05, decay starting at 7:40. If that is what was wanted, change `start` to 365 and leave `end` at 460. Displayed length becomes 1:35.

## Source crop

This upload is 4:3 pillarboxed inside the 16:9 player, and the film image is letterboxed inside that 4:3 frame, so the raw picture arrives with black bars on all four sides. Measured off a live screenshot: the picture occupies 0.747 of the stage width, which is 3/4 to within measurement error, and 0.699 of its height. The picture itself is about 1.91:1 and sits dead centre, so no recentring is needed.

The fix enlarges the iframe past the stage and lets the stage's `overflow: hidden` clip it, rather than `transform: scale()`. YouTube then genuinely renders at the larger size instead of a smaller frame being blown up, so the picture does not go soft.

Three `--zoom` values worth knowing:

| Value | Result |
| --- | --- |
| 1.000 | raw source, bars on all four sides |
| 1.333 | side bars gone exactly, thin top/bottom bars remain, reads as a deliberate letterbox |
| 1.430 | picture fills the frame, roughly 3.4% lost off each side |

Currently set to 1.430. `--offx` and `--offy` are both 0% and exist for sources whose letterbox is not symmetrical.

## Crop tune panel

Add `?tune=1` to the URL for zoom and X/Y offset sliders plus the three presets above. It prints the three CSS custom property lines ready to paste back into `:root`. Hidden otherwise, so students never see it. Same pattern as the Energy Dial tune panel.

This is currently local to this instance. The other four quoters are untouched and bit-identical to before. Worth backporting to the shared template with `--zoom: 1` as the default, since a no-op default makes it harmless everywhere and several sources have this problem.

## Notes copy

Placeholder. Two paragraphs sized to roughly match the other quoters so the layout and height measurements are meaningful. Replace both, keeping the second one in the `listen` class so it keeps the divider rule and brighter text.

## Technical notes

Shared machinery identical to every other quoter, no changes made to it in this commit.

- Film audio with very wide dynamic range across this sequence. Expect `levelTrim` to need setting by ear, and expect it to differ from the speech quoters.
- Source is a third-party upload of a commercial film, so takedown risk is real. If it goes, the card shows the "could not be loaded" message rather than breaking. Note a backup video ID.

## Open TODOs

- Supply the real notes copy, card title and source credit.
- Confirm the fade interpretation above.
- Confirm the folder name before it goes into Canvas.
- Tune `levelTrim` by ear.
- Confirm 1.43 (fills the frame) against 1.333 (keeps a thin letterbox).
- Decide whether to backport the crop to the shared quoter template.
- Re-measure stacked height after the real copy lands.
- Live-test overlay flash suppression, fade feel, captions off.
- Note a backup video ID against takedown.

## Last updated

2026-08-13. Initial build from the current quoter template. Clip window 6:02 to 7:40, 3s fades, placeholder title, credit and notes. Then added the source crop at `--zoom: 1.43` to remove the four-sided letterbox, plus a `?tune=1` crop panel.
