# Skill Loop Player (staging — 2B build)

Directory: `skill-loop-player-test/`

A loop-a-section player for lecture video. It embeds a YouTube lecture and lets a student loop a named skill segment to rewatch while following along, with notes for each loop. This is the redesigned 2B layout with the real YouTube IFrame Player API wired in.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/skill-loop-player-test/

## Canvas embed

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/skill-loop-player-test/?v=4"
        width="100%" height="980"
        title="Skill Loop Player"
        style="border: none;"
        allow="autoplay"
        loading="lazy"></iframe>
```

Height 980 is deliberately generous. This MOTE is the focus of its page, so it runs full width up to a 920px layout cap and tall enough to show the video, timeline, chapter cards, and notes with no internal scrollbar. Trim the height if your Canvas column is narrower and you see dead space at the bottom.

## Build state

Staging build for live review. 2B design, real player, real notes. Pending sign-off before the final ship to `skill-loop-player/`.

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

- Live test of the build: play, loop, scrub, and notes.
- iOS check: first play.
- On sign-off, ship the final to `skill-loop-player/`.

## Last updated

2026-06-11: removed the header strip above the video (title, volume, mute, turtle). Play, volume, and speed now come from YouTube's own control bar. Cleaner layout, video first.
