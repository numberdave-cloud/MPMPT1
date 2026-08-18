---
name: audio-player
description: Build a new audio-only YouTube player MOTE for the MPMPT1 repo. Use this whenever the user pastes a YouTube link and asks to "make an audio player", or wants a slim single-row player that plays a fixed YouTube track as a musical bed (no video, no scrubbing) to sit at the top of a Canvas page, or asks for a "musical bed" or a track that "fades in", "fades out", or is "quoted" from a YouTube ID, or to add another player to the audio-player family. Also use when fixing shared player machinery, since a fix must be applied across the whole family. Drives the build from a short tap intake, covers the four fade shapes, and ships on build so the player can be tested live.
---

# Audio Player

Build one audio-only YouTube player MOTE, consistent with the existing family in
MPMPT1. The player is a slim rack card with a single transport row: play button,
EQ bounce indicator, display-only progress bar, mono time readout, and a custom
volume fader. It plays one fixed YouTube track as a bed. No video is shown, there
is no scrubbing.

The whole build is copy the right source folder, change the config constants, the
card `<title>` and the on-card title line. Everything else is shared machinery
that already works. Do not re-implement it.

## Before you start

1. Clone the repo fresh if not already cloned. HTTPS with the PAT from project
   instructions. Never write the PAT into any repo file.
2. Read `INDEX.md` at the repo root, then `PLAYERS.md` at the repo root.
   `PLAYERS.md` is the family registry: the shape table, the instances, the
   shared behaviours.
3. The YouTube video ID comes from the trigger message. Pull the ID from the URL
   the user pasted.

## Intake

Drive the build from a short tap sequence, not a typed spec. Use the tappable
input tool for the categorical choices. Only two things are typed, because
buttons cannot hold them: the title (it is the user's copy) and any exact
timecodes.

1. **Title.** Ask for it, or take it from the trigger. Track title and artist,
   used verbatim. Do not invent or paraphrase copy. Italicise a film title with
   `<em>` on first mention only if the user's text does.
2. **Whole track or quote.** One tap.
   - Whole track: no fades, no offset. Plays from the top to the natural end.
   - Quote: has a start side and an end side, each of which can be left open.
3. **For a quote, one tap per side.**
   - Start: "From the top" (cold, no fade-in), or "Start point plus fade-in".
   - End: "To the end" (no fade-out, plays out), or "End point plus fade-out".
4. **Numbers.** For any side not left open, ask for the values on one typed line:
   the start point and fade-in length, the end point and fade-out length.

### The fade convention

The start and end points are the edges of the clean quote. The fades sit outside
them, so the quoted content is always at full volume between the two points.

- Start point is where the fade-in finishes. Start 1:05 with a 5s fade-in means
  playback enters silent at 1:00 and is full by 1:05.
- End point is where the fade-out begins. End 2:01 with a 10s fade-out means the
  fade starts at 2:01 and reaches silence at 2:11, where it stops.

### Intake to shape

The two side answers pick the shape and the source folder to copy:

| Start side | End side | Shape | Source folder |
| --- | --- | --- | --- |
| From the top | To the end | plain | `audio-player-order-in-chaos/` |
| From the top | End point plus fade-out | fade-out | `audio-player-under-the-skin/` |
| Start point plus fade-in | To the end | fade-in | `audio-player-mausam-escape/` |
| Start point plus fade-in | End point plus fade-out | fade-in+out | `audio-player-history-of-the-ring/` |

A "whole track" is the plain row. Set the source's constants from the intake,
where `fadeIn` and `fadeOut` are the lengths the user gave, all in seconds:

- **plain:** `START_AT = 0`.
- **fade-out:** `FADE_START = end`, `FADE_DURATION = fadeOut`. Starts cold from
  the top.
- **fade-in:** `START_AT = start - fadeIn`, `FADE_DURATION = fadeIn`. Enters
  silent, full at the start point, plays to the natural end.
- **fade-in+out:** `START_AT = start - fadeIn`, `FADE_IN_END = start`,
  `FADE_OUT_START = end`, `FADE_OUT_DURATION = fadeOut`.

The entry for the two fade-in shapes is the start point minus the fade-in length,
because the engine's entry is where the source begins silent and the start point
is where it reaches full. Do the subtraction, convert to whole seconds, and keep
the mm:ss comment on each constant accurate.

## Build

1. Copy the shape's source folder and drop the copied README:

   ```
   cp -r audio-player-<source> audio-player-<subject>
   rm audio-player-<subject>/README.md
   ```

2. In `audio-player-<subject>/index.html`:
   - Set `VIDEO_ID` to the track's ID.
   - Set the timing constants from the intake mapping above. Update the mm:ss
     comment on each.
   - Set the page `<title>` and the on-card `.meta-title` line to the title.
     Keep it greppable.
   - Leave the shared machinery alone.

3. Validate. Extract the script and run `node --check` before anything else:

   ```
   sed -n '/<script>/,/<\/script>/p' audio-player-<subject>/index.html \
     | sed '1d;$d' > /tmp/check.js && node --check /tmp/check.js
   ```

4. If a timing change is delicate, simulate the fade tick-by-tick in `/tmp/sim.js`
   in Node before trusting it. `fadeFactor(t)` is the function to step through.

A Playwright screenshot over the `file://` URL only confirms layout, not
playback: the IFrame API will not load from `file://` (error 153). So layout can
be checked locally, playback cannot.

## Ship (this family ships on build)

An audio player cannot be tested until it is live: the IFrame API does not run
from `file://`, so playback can only be verified on the live URL. So for this
family, and only this family, build and ship without a pre-ship wait, then hand
the live URL back for testing. This is a deliberate exception to the general
show-first rule, granted for audio players because the review has to happen live.

After the intake, once the build validates, in one commit:

1. Write `audio-player-<subject>/README.md`. Concise and factual:
   - MOTE name and directory.
   - One line on what it plays and the fade shape.
   - Live GitHub Pages URL.
   - Canvas embed with height 190 (see below), noting why 190 not 600.
   - Video ID and the intake values (start point, fade-in, end point, fade-out).
   - Resolved constants (`START_AT`, fade constants) and where it stops.
   - Technical notes worth keeping (1px host, ticker automation, iOS gesture).
   - Any open decisions or TODOs.
   - "Last updated" date and a one-line note on what changed.
   - Never the PAT or the project instructions.
2. Add a row to `PLAYERS.md` (instances table) and a row to `INDEX.md`
   (Miscellaneous, live).
3. Commit, then `git fetch`, `git rebase origin/main`, push. Never merge. If
   `INDEX.md` conflicts on rebase, keep both rows.
4. Verify on the raw URL with a short sleep buffer:
   `https://raw.githubusercontent.com/numberdave-cloud/MPMPT1/main/audio-player-<subject>/index.html`.
   Compare `git rev-parse HEAD` against `git ls-remote` to confirm the push
   landed regardless of CDN cache.
5. Hand back the live URL, the embed block, and a one-line timing summary so the
   user can test. Tweak from their feedback. Level is the one thing only checkable
   live, so a fader-default tweak may follow.

## Canvas embed

Height 190, not the 600 default. The player is a single slim row; content runs
about 169px desktop, about 184px on narrow mobile where a long title wraps to two
lines. 190 clears the tallest case without clipping the fader. Keep it at or
above 185.

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/audio-player-<subject>/"
  width="100%"
  height="190"
  title="<track title> audio player"
  style="border: none;"
  allow="autoplay"
  loading="lazy"></iframe>
```

## Non-negotiable technical notes

These break the player if changed carelessly. They are why the build is
copy-and-swap, not rewrite.

- **The IFrame API player lives in a 1px `overflow:hidden` host** (`.yt-host`),
  absolutely positioned and clipped out of view. It is rendered, never
  `display:none`. `display:none` stops YouTube playback.
- **The fade is automation, not a real audio tap.** Web Audio cannot read a
  cross-origin YouTube stream. An 80ms ticker polls `getCurrentTime` and calls
  `setVolume`. `fadeFactor(t)` multiplies the fader level; effective volume is
  only pushed when it changes.
- **Fade-in is eased (raised cosine), fade-out is linear.** A linear ramp out of
  silence sounds like a cut, so the fade-in uses `0.5 - 0.5*cos(pi*p)`.
- **Progress forks by shape.** Fixed-window shapes (fade-out, fade-in+out) run
  `START_AT` to `SCALE` (`FADE_OUT_START + FADE_OUT_DURATION`, or
  `FADE_START + FADE_DURATION`) and call `finish`. Play-to-end shapes (plain,
  fade-in) set `scale` from `getDuration()` once known and end on the `ENDED`
  event. Do not cross the two.
- **playerVars** stay as set: `autoplay: 0, controls: 0, disablekb: 1, fs: 0,
  cc_load_policy: 0, iv_load_policy: 3, modestbranding: 1, rel: 0,
  playsinline: 1`.
- **iOS Safari needs the play tap as the audio gesture**, so the play handler
  calls `playVideo` directly. Keep it in the click handler.
- **`html` and `body` are locked to 100% height with `overflow:hidden`,** so the
  page can never exceed the iframe. Do not add scrolling content.
- **The volume fader ignores click-to-jump.** Drag on the handle, scroll, arrow
  keys. It initialises at 70% (`userVol`). Raise that default for a louder bed.

## Design system

The copied folder already carries the styling, so leave it. For reference: the
rack card sits on a transparent page, palette background `#1E1A17`, text
`#EAE0D0`, accent `#C07838`, hot accent `#D8904A`, Inter for UI, Courier New for
the time readout. Glow is reserved for the active play button, the time readout
and the fading progress bar.
