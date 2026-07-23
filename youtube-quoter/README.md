# YouTube Quoter

**Directory:** `youtube-quoter/`

Plays a fixed segment of a single YouTube video and nothing else. Locks students to one short "quote" of footage the way you would cite a line from an interview, with all YouTube chrome and click-through stripped out. Opens on a title card (title, linked source credit, quote length) that dissolves into the clip on play and fades back at the end. A notes panel sits alongside for context on what to listen for.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/youtube-quoter/

## Canvas embed

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/youtube-quoter/?v=4"
  width="100%"
  height="480"
  title="YouTube Quoter: Mark Korven playing the Apprehension Engine"
  style="border: none;"
  allow="autoplay"
  loading="lazy">
</iframe>
```

Height 480 (below the 600 default). Measured content heights:

| Column width | Layout | Height needed |
|---|---|---|
| 800px and up | side by side | ~390px |
| 700px | side by side | ~452px |
| below 660px | stacked | ~600px |

480 covers every side-by-side case with headroom. Below 660px the notes panel drops beneath the video and it wants ~620px. If the Canvas mobile app matters for this page, use 620 and accept the whitespace on desktop.

## Build state

v4, 2026-07-22. Functional. Notes copy is a DRAFT pending approval.

## Current clip

- Video ID `lzk-l8Gm0MY`, Mark Korven playing the Apprehension Engine
- Quote content 32s to 1:04 (64s), displayed length 0:32
- 3s fade in and 3s fade out, so actual playback runs 29s to 67s
- Card title "Mark Korven playing the Apprehension Engine", source credit "Indie Film & Music" linking to the source video
- Volume starts at 50%

## How it works

- Uses the YouTube IFrame Player API (loaded from youtube.com). This is the one MOTE that is not pure self-contained Web Audio, by necessity, since it is quoting real YouTube footage.
- Config block at the top of the script: `videoId`, `start`, `end`, `fadeIn`, `fadeOut`, `title`, `source`, `sourceUrl`, `showLength`. To make a new quote, duplicate the directory, change those values, rewrite the notes prose in the markup, restage.
- A transparent click-shield sits over the iframe and swallows every mouse event, so YouTube never registers a hover or a click. No hover means no title bar, no logo watermark, no end-screen thumbnails. Reinforced with `controls=0`, `rel=0`, `fs=0`, `disablekb=1`, `iv_load_policy=3`, `modestbranding=1`.
- One `.cover` element does three jobs: idle title card, curtain hiding YouTube's start-up overlay flash, and the fade back to black at the end.
- YouTube fires its start-up overlay (title, channel, centre button, "More videos" strip, logo) on the play event itself, not on hover, so the click-shield cannot stop it. The card is held over the video for `REVEAL_HOLD` seconds (currently 4.2) to cover it, then dissolves over `REVEAL_DISSOLVE` (0.8s).
- The PLAY / REPLAY button hides via `opacity`, never `display`, so removing it does not reflow the card and shunt the text downward.
- Audio fades are manual: the API has no native fade, so volume is ramped via `setVolume` in a 50ms `setInterval`. The ramp scales off the volume slider, so it fades toward the student's chosen level rather than a fixed 100.
- The card fades back in across the audio fade-out (`END_FADE`, matching `fadeOut`, floor of 0.6s), so the end mirrors the start.
- The progress bar is a non-interactive read-out spanning the played window, fade tails included.
- Transparent page background with a rounded dark frame, so the widget floats on the Canvas white rather than filling the iframe edge to edge. No drop shadow (causes haze on white Canvas pages).

## Config quirks worth knowing

- YouTube's `end` playerVar is deliberately set past our own end (`ceil(PLAY_END) + 2`). YouTube's segment stopping is imprecise and would otherwise truncate the fade-out. It is only a backstop; the 50ms poll owns the real ending.
- The audio envelope snaps to true zero below 2%, so the clip lands on silence rather than cutting at a low but non-zero volume.
- Set `fadeIn` or `fadeOut` to `0` for a hard cut. The played window auto-extends to carry whatever fades are set. With `fadeOut: 0` the visual still fades over 0.6s so the ending does not snap.
- `source` hidden when empty. `sourceUrl` empty auto-links to `youtube.com/watch?v={videoId}`. Opens in a new tab so the Canvas page survives.
- The source link is disabled while the curtain is up, so it cannot be clicked mid-playback.
- Length shown is `end - start` (quote content), not the played window with fades.
- `REVEAL_AT` is `PLAY_START + max(fadeIn, REVEAL_HOLD)`. For a very short quote, check this does not land past `end` or the video will barely appear.
- Notes prose lives in the markup (between the comment markers), not in the config block, since multi-paragraph prose in a JS string is awkward to edit.
- Stacked layout resets `flex` on the columns. In a column flex container `flex-basis` applies to height, so an unreset basis silently inflates the widget by ~135px.
- iOS ignores programmatic volume (device controls it), so the slider is desktop-only. Play, stop, and fades work everywhere.
- If a source video has third-party embedding disabled, the card shows a "could not be loaded" message rather than a broken frame.

## Open TODOs

- **Approve or rewrite the notes copy.** Currently a draft. The Tony Duggan-Smith attribution and the acoustic-not-synthetic origin story are widely reported but worth a second check before students see them.
- Confirm the fade-out feel now that it lands on true silence.
- Confirm `REVEAL_HOLD` at 4.2s fully covers the overlay flash.
- Decide the embed height, 480 desktop-only or 620 mobile-safe.
- Curves are linear. Equal-power available if the middle of the fade sounds like it dips.
- Reusable template. Future quotes reuse this build with a fresh config and fresh notes.

## Last updated

2026-07-22. Fixed the fade-out truncating at ~2% instead of silence, and stopped YouTube's imprecise segment-end from clipping the tail. End now fades to the title card mirroring the open. Title text no longer jumps when the play button hides. Lightened the transport and volume controls. Added the rounded floating frame and the notes panel. Volume now starts at 50%. Source credit is a hover-highlighted link to the source video.
