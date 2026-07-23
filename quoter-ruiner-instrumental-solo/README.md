# Quoter: Nine Inch Nails, Ruiner Instrumental Break

**Directory:** `quoter-ruiner-instrumental-solo/`

A YouTube Quoter instance. Plays one fixed segment of a single YouTube video and nothing else, with all YouTube chrome and click-through stripped out. This one quotes the instrumental section at the centre of Ruiner, from The Downward Spiral.

Built from the shared quoter template. See `QUOTERS.md` at repo root for the registry and the shared machinery notes.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/quoter-ruiner-instrumental-solo/

## Canvas embed

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/quoter-ruiner-instrumental-solo/"
  width="100%"
  height="480"
  title="Nine Inch Nails - Ruiner Instrumental Break"
  style="border: none;"
  allow="autoplay"
  loading="lazy">
</iframe>
```

Height 480. Measured: ~389px at 900px wide, ~329px at 700px, ~537px stacked below 660px. 480 covers the side-by-side cases. Use 560 if the Canvas mobile app matters for this page.

## Build state

v1, 2026-07-22. Category: Miscellaneous. Untested live.

## Current clip

- Video ID `RkT-aMgZvQI`
- Quote content 2:44 to 3:51 (164s to 231s), displayed length 1:07
- 3s fade in and 3s fade out, so actual playback runs 161s to 234s
- Card title "Nine Inch Nails - Ruiner Instrumental Break", credit "1710tmk" linking to the source video
- Volume starts at 50%, `levelTrim` currently 0 dB

## Notes copy

Approved wording, used as given, with two changes worth knowing:

- A comma added after "here" in the Trent sentence.
- The listening prompt ("Pay attention to the drastic change in energy and atmosphere") moved to last. It sits in the styled prompt slot beneath the dividing rule, and a paragraph after that slot looks wrong. Original order was prompt in the middle, Trent sentence last.

The Reznor claim was checked before shipping. In a magazine interview about this solo he said he is not a soloist, described the sound as ridiculous and cheesy, and said he had effectively attempted a "Comfortably Numb"-type solo. He put the Pink Floyd quality down to accidentally calling up the wrong patch on a Zoom pedal. The copy as written is accurate.

An optional upgrade: the specific Pink Floyd reference is "Comfortably Numb" rather than Pink Floyd generally, and a short verbatim Reznor quote is available if a quote is wanted rather than paraphrase.

## Technical notes

Shared machinery is identical to every other quoter. Points specific to this instance:

- **Source durability.** The credit "1710tmk" reads as a personal upload rather than an official channel. Unofficial uploads of commercial music are removed more often than conference talks. If it goes, the card shows a "could not be loaded" message rather than breaking, but the quote is lost. Worth checking periodically, or repointing at an official upload if one exists.
- **Level.** This is a commercial master, likely hotter than the speech-based quoters. YouTube only normalises loud content down toward roughly -14 LUFS and never lifts quiet content, so this one may sit louder than the others. `levelTrim` is at 0; expect to trim by ear.
- `REVEAL_AT` lands at 165.2s, comfortably inside a 67s quote.

## Open TODOs

- Tune `levelTrim` by ear against the other quoters.
- Confirm the notes ordering change is acceptable.
- Decide whether to use a verbatim Reznor quote instead of the paraphrase.
- Live-test overlay flash suppression, fade feel, captions off, embed height.

## Last updated

2026-07-22. Initial build from the current quoter template, including curved fades, per-clip level trim, and forced caption unloading.
