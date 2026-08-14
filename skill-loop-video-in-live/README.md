# Video in Live: Skill Loops

Directory: `skill-loop-video-in-live/`

A loop-a-section player for a lecture video on working with video in Ableton Live. It embeds the lecture and lets a student loop a named skill segment to rewatch while following along, with per-loop notes. Built on the Skill Loop Player engine (real YouTube IFrame Player API).

Covers four skills: adding a video file to Live, finding the hit point, adding audio to the hit, and exporting video with audio.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/skill-loop-video-in-live/

## Canvas embed

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/skill-loop-video-in-live/?v=1"
        width="100%" height="980"
        title="Video in Live: Skill Loops"
        style="border: none;"
        allow="autoplay"
        loading="lazy"></iframe>
```

Height 980 matches the sibling Skill Loop Player. Measured worst case across widths is about 940 (narrow columns, where cards stack and notes wrap), so 980 clears it with no internal scrollbar. Trim if your Canvas column is wide and you see dead space.

## Build state

Shipped v1.0. Four loops, real YouTube player, per-loop notes with keycap-styled shortcuts. Layout verified locally at widths 420 to 1000. Player itself only runs on the deployed HTTPS origin, so playback is unverified until checked live in Canvas.

## Technical notes

- Not self-contained. Loads YouTube's IFrame Player API at runtime and needs the student online.
- Play, pause, scrubbing, volume, and speed are handled by YouTube's own control bar. The widget adds the timeline, the chapter loops, and the per-loop notes. The timeline also scrubs, and Escape releases a loop.
- `getCurrentTime()` is polled at 150ms to drive the playhead, the active-chapter highlight, and the loop. `seekTo(start, true)` fires when the playhead passes an armed region's end, with a short guard against double-seeks.
- Error 153 mitigation: a `strict-origin-when-cross-origin` referrer meta tag, the `youtube-nocookie.com` host, and an `origin` playerVar on https. `file://` has no valid origin and will 153, so test over http/https.
- Duration reads from `getDuration()` once ready, then the timeline blocks reposition. A 420s placeholder holds until then.
- Chapter cards grid is 4-up on wide, 2-up under 720px, 1-up under 420px.

## Loops (video YEuZr1zeWVA)

1. Adding a Video File to Live: 1:04 to 2:06 (64 to 126)
2. Finding the Hit Point: 2:54 to 3:31 (174 to 211)
3. Adding Audio to the Hit: 4:20 to 4:53 (260 to 293)
4. Exporting Video with Audio: 5:03 to 6:10 (303 to 370)

## Config

Edit `VIDEO_ID` and the `REGIONS` array at the top of the inline script. Each region has `label`, `start`, `end` in seconds, and a `notes` array of dot-point strings. Wrap a shortcut in `<code>...</code>` for the keycap highlight.

## Video requirements

Unlisted (not private), with "allow embedding" turned on.

## Open / TODO

- Verify playback in Canvas on the deployed URL (levels, first-play on iPhone).
- Loop 3 tip 3 has no shortcut keycap. Grid narrowing is Cmd+2 / Ctrl+2 if one is wanted later.
- Consider whether this belongs under Arranging rather than Miscellaneous, given the content. Filed Miscellaneous to match the Skill Loop Player family (delivery format).

## Last updated

2026-08-14: initial ship. Four loops on the Skill Loop Player engine, Ableton video workflow, keycap shortcuts on the export loop.
