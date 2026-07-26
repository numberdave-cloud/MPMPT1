# Quoter: Drive, Opening Credits

**Directory:** `quoter-drive-opening-credits/`

A YouTube Quoter instance, used here as a composition brief rather than an analysis quote. Plays the opening credits of Drive (2011), scored to Kavinsky's "Nightcall," and sets the student a task: capture the atmosphere without cloning the song.

Built from the shared quoter template. See `QUOTERS.md` at repo root for the registry and shared machinery notes.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/quoter-drive-opening-credits/

## Canvas embed

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/quoter-drive-opening-credits/"
  width="100%"
  height="480"
  title="Drive - Opening Credits"
  style="border: none;"
  allow="autoplay"
  loading="lazy">
</iframe>
```

Height 480. Measured: ~389px at 900px wide, ~380px at 700px, ~567px stacked below 660px. 480 covers the side-by-side cases. Use 590 if the Canvas mobile app matters for this page.

## Build state

v1, 2026-07-22. Category: Miscellaneous. Untested live.

## Current clip

- Video ID `BHVbbcHWX4k`
- Quote content 0:05 to 1:27 (5s to 87s), displayed length 1:22
- 4s fade in and 4s fade out, so actual playback runs 1s to 91s
- Card title "Drive - Opening Credits", credit "Drive (2011)" linking to the source video
- Volume starts at 50%, `levelTrim` currently 0 dB

## Notes copy

Dave's brief, used closely with two grammar fixes for student-facing copy: "the texture and pace complement" (was "complements"), and "they... have stated" (was "has stated"), keeping the singular-they consistent through the paragraph. Otherwise his wording.

The task ("create something that captures this atmosphere, do not clone the song") sits in the emphasised prompt slot beneath the rule. The context sits above it.

The brief deliberately does not name the music or its style. That is the point of the exercise: capture the atmosphere without a reference to copy. The card title names the film but not the song.

## Two things flagged to Dave

- **Source credit.** Dave wrote "[Source]" as a placeholder. Filled with "Drive (2011)", crediting the film rather than the re-uploader's channel. Pending confirmation.
- **Source durability.** This is a fan re-upload of a copyrighted film scene set to a commercial track, the highest takedown risk in the set. No official stable upload of the Drive opening with Nightcall exists to fall back on. If it is pulled, the card shows "could not be loaded" and the quote is lost. Note a backup video ID and re-check before each semester. Self-hosting is not an option here: it would put the copyright liability on this repo.

For reference, not for the widget: the track is "Nightcall" by Kavinsky (2010), produced with Guy-Manuel de Homem-Christo of Daft Punk, vocals by Lovefoxxx. Synthwave. Kept out of the notes on purpose.

## Technical notes

Shared machinery identical to every other quoter. Instance specifics:

- Fades are 4s here, not the usual 3s. `PLAY_START` is 1s (5 minus 4). `REVEAL_AT` lands at 5.2s, 0.2s past the content start, so the fade-in plays out behind the card and the video appears as full volume arrives.
- `END_FADE` is 4s, matching `fadeOut`, so the card fades back in across the same window as the audio.
- Commercial master plus film audio, likely louder than the speech quoters. Trim by ear once heard against the others.

## Open TODOs

- Confirm the "Drive (2011)" source credit, or replace it.
- Tune `levelTrim` by ear.
- Note a backup video ID against takedown.
- Confirm the two grammar fixes to the brief are acceptable.
- Live-test overlay flash suppression, fade feel, captions off, embed height.

## Last updated

2026-07-22. Initial build from the current quoter template. 4s fades, composition-brief notes, film-credit source pending confirmation, takedown risk flagged.
