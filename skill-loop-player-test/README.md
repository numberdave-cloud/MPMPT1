# Skill Loop Player (test build)

Directory: `skill-loop-player-test/`

A loop-a-section player for lecture video. It embeds a YouTube video and lets students click a named skill to loop that segment for repeated watching. A proportional timeline shows where each skill sits in the video, with the intro and gaps left as empty track.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/skill-loop-player-test/

## Canvas embed

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/skill-loop-player-test/?v=1"
        width="100%" height="640"
        title="Skill Loop Player"
        style="border: none;"
        allow="autoplay"
        loading="lazy"></iframe>
```

Height is 640 rather than the usual 600. The 16:9 player sits above the timeline strip and skill buttons, which need the extra vertical room. The video is capped at 680px wide so it does not balloon on a wide Canvas column.

## Build state

Test / staging build for review. Real video and timings are wired in. Awaiting a live sign-off before the final ship to `skill-loop-player/`.

## Technical notes

- Not self-contained. It loads YouTube's IFrame Player API at runtime (`https://www.youtube.com/iframe_api`) and needs the student online. There is no embedded base64 audio payload like the synthesis MOTEs.
- Control is via the IFrame API. `getCurrentTime()` is polled every 150ms to drive the active-section highlight and the loop. `seekTo(start, true)` fires when the playhead passes an armed region's end.
- Error 153 mitigation is built in: a `strict-origin-when-cross-origin` referrer meta tag, the `youtube-nocookie.com` host, and an `origin` playerVar set automatically when the page is served over http or https. Opening from `file://` has no valid origin and will still throw 153, so test over http.
- Loop seam: YouTube's `seekTo` is not frame accurate and rebuffers on each jump, so the loop point has a small hitch that smooths out once the segment is cached.
- One loop armed at a time. Click an armed skill again or press Escape to release. Clicking the empty track scrubs to that position.

## Config

Edit two things at the top of the inline script to reuse this for another lecture:

- `VIDEO_ID`: currently `5PVdExtOY9o`
- `REGIONS`: array of `{ label, start, end }` in seconds. Currently: Adding Drum Kit (36 to 70), Programming Beat 1 (97 to 131), Programming Beat 2 (149 to 177).

## Video requirements

The YouTube video must be unlisted (not private) with "allow embedding" turned on, or the player has nothing to play.

## Open / TODO

- Live test of the loop behaviour and the 153 fix on the Pages URL.
- On approval, ship the final version to `skill-loop-player/`.
- Confirm whether the loop seam at each region boundary is acceptable in practice or needs the seek pulled a fraction earlier.

## Last updated

2026-06-11: initial test / staging build.
