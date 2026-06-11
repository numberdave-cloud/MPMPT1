# Skill Loop Player

Directory: `skill-loop-player/`

A loop-a-section player for lecture video. It embeds a YouTube lecture and lets a student loop a named skill segment to rewatch while following along, with notes for each loop. Built on the 2B layout with the real YouTube IFrame Player API.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/skill-loop-player/

## Canvas embed

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/skill-loop-player/?v=1"
        width="100%" height="980"
        title="Skill Loop Player"
        style="border: none;"
        allow="autoplay"
        loading="lazy"></iframe>
```

Height 980 is deliberately generous. This MOTE is the focus of its page, so it runs full width up to a 920px layout cap and tall enough to show the video, timeline, chapter cards, and notes with no internal scrollbar. Trim the height if your Canvas column is narrower and you see dead space at the bottom.

## Build state

Shipped. 2B layout, real YouTube player, real per-loop notes. The staging copy at `skill-loop-player-test/` holds the same build for future tinkering.

## Technical notes

- Not self-contained. Loads YouTube's IFrame Player API at runtime and needs the student online.
- Play, pause, scrubbing, volume, and speed are all handled by YouTube's own control bar. The widget adds the timeline, the chapter loops, and the per-loop notes. The timeline also scrubs, and Escape releases a loop.
- `getCurrentTime()` is polled at 150ms to drive the playhead, the active-chapter highlight, and the loop. `seekTo(start, true)` fires when the playhead passes an armed region's end, with a short guard against double-seeks.
- Error 153 mitigation: a `strict-origin-when-cross-origin` referrer meta tag, the `youtube-nocookie.com` host, and an `origin` playerVar on https. `file://` has no valid origin and will still 153, so test over http.
- Duration is read from `getDuration()` once ready, then the timeline blocks reposition. A 195s placeholder is used until then.

## Config

Edit `VIDEO_ID` and the `REGIONS` array at the top of the inline script. Each region has `label`, `start`, `end` in seconds, and a `notes` array of dot-point strings. Wrap a shortcut in `<code>...</code>` for the keycap highlight. Current: video 5PVdExtOY9o, three loops (36-70, 97-131, 149-177).

## Video requirements

Unlisted (not private), with "allow embedding" turned on.

## Open / TODO

- iOS check: confirm first play behaves on iPhone.

## Last updated

2026-06-11: initial ship. 2B layout, YouTube native controls, real per-loop notes with keycap-styled shortcuts.
