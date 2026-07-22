# YouTube Quoter

**Directory:** `youtube-quoter/`

Plays a fixed segment of a single YouTube video and nothing else. Locks students to one short "quote" of footage the way you would cite a line from an interview, with all YouTube chrome and click-through stripped out.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/youtube-quoter/

## Canvas embed

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/youtube-quoter/"
  width="100%"
  height="440"
  title="YouTube Quoter: Mark Korven plays the Apprehension Engine"
  style="border: none;"
  allow="autoplay"
  loading="lazy">
</iframe>
```

Height 440 (below the 600 default): this is a compact vertical stack, a caption over a 16:9 video capped at 520px wide (about 292px tall) plus a thin transport row. 440 clears it at any column width with headroom.

## Build state

v1, shipped 2026-07-22. Functional, awaiting live Canvas test.

## Current clip

- Video ID `lzk-l8Gm0MY`, Mark Korven playing the Apprehension Engine
- Quote content 32s to 1:04 (64s)
- 3s fade in and 3s fade out, so actual playback runs 29s to 67s

## How it works

- Uses the YouTube IFrame Player API (loaded from youtube.com). This is the one MOTE that is not pure self-contained Web Audio, by necessity, since it is quoting real YouTube footage.
- Playback is locked to a segment with a config block at the top of `index.html`: `videoId`, `start`, `end`, `fadeIn`, `fadeOut`, `context`, `instruction`, `source`. To make a new quote, duplicate the directory, change those values, restage. No other edits needed.
- A transparent click-shield sits on top of the iframe and swallows every mouse event, so YouTube never registers a hover or a click. No hover means no title bar, no logo watermark, no end-screen thumbnails. Reinforced with `controls=0`, `rel=0`, `fs=0`, `disablekb=1`, `iv_load_policy=3`, `modestbranding=1`.
- An opaque cover hides the raw YouTube thumbnail before first play and the frozen frame after the clip ends, showing a clean PLAY / REPLAY button instead.
- On play, that same cover is held opaque as a curtain over the video for the first few playback-seconds. YouTube flashes its start-up overlay (title bar, channel, centre play/pause button, "More videos" strip, logo) on the play event itself, not on hover, so the click-shield cannot stop it. The curtain hides it, then fades away once it has cleared. Reveal timing is `REVEAL_AT` near the top of the script: `PLAY_START + max(fadeIn, 3.5)` playback-seconds. With a fade-in of about 3s the reveal lands right as the quote proper starts. Nudge the 3.5 if the overlay ever sneaks through or the reveal feels late.
- Fades are done by hand: the API has no native fade, so volume is ramped via `setVolume` inside a 50ms `setInterval`. The ramp scales off the volume slider, so it fades toward whatever level the student has set rather than a fixed 100.
- The progress bar is a non-interactive read-out. It spans the full played window including the fade tails, not the whole source video.

## Config quirks worth knowing

- Set `fadeIn` or `fadeOut` to `0` for a hard cut on that end. The played window auto-extends to hold whatever fades are set.
- `instruction` and `source` are hidden when set to an empty string.
- iOS ignores programmatic volume (device controls it), so the slider is effectively desktop-only. Play, stop, and fades work everywhere.
- Play is user-gesture triggered (the PLAY button), so audio is permitted. `allow="autoplay"` is set on the embed as a backstop for the nested player.
- If a future source video has third-party embedding disabled, the cover shows a "could not be loaded" message rather than a broken frame. Pick a different source.

## Open TODOs

- Live-test in Canvas and confirm the fade feel. Curves are linear at the moment, which is usually fine for short musical fades. Equal-power curve is available if the middle of the fade sounds like it dips.
- Confirm final timestamps after testing.
- Decide whether the progress bar should span the quote only (32 to 64) or the full played window including fades (current behaviour).
- Reusable template. Future quotes reuse this build with a fresh config.

## Last updated

2026-07-22. Added a curtain over the video during playback start to hide YouTube's start-up overlay (title, centre button, "More videos" strip, logo), which fires on the play event and so bypassed the click-shield. Curtain fades away once the overlay clears, timed off `REVEAL_AT`.
