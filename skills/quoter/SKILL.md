---
name: quoter
description: Build a new YouTube Quoter MOTE for the MPMPT1 repo. Use this whenever the user pastes a YouTube link and asks to "make a quoter" or "quote this video", or wants a chrome-free video quote with a title-card curtain, audio fades either side, and a notes column beside it, to sit on a Canvas page, or to add another quoter to the family. Also use when fixing shared quoter machinery, since a fix must be applied across the whole family. Drives the build from a single intake panel and ships on build so the quote can be checked live.
---

# YouTube Quoter

Build one YouTube Quoter MOTE, consistent with the existing family in MPMPT1. A
quoter plays a fixed segment of one video with audio fades either side, hides
YouTube's chrome, holds a title card over the start-up overlay, then dissolves to
the quote. Beside the video sits a notes column of teaching prose.

The build is copy the canonical folder, change the `QUOTE` config block, rewrite
the notes prose, change the page `<title>`. Everything else is shared machinery
that already works. Do not re-implement it.

## Before you start

1. Clone the repo fresh if not already cloned. HTTPS with the PAT from project
   instructions. Never write the PAT into any repo file.
2. Read `INDEX.md` at the repo root, then `QUOTERS.md` at the repo root.
   `QUOTERS.md` is the family registry: the config fields, the instances, the
   shared behaviours, the level and crop rules, the embed heights.
3. The YouTube video ID comes from the trigger message. Pull it from the link.

## Intake

Collect everything in one panel. The panel is `assets/intake.html`.

1. Read `assets/intake.html`. Replace every `__VIDEO_ID__` with the ID.
2. Render it with the visualizer (`show_widget`) so it appears inline. The panel
   collects the title, source credit, quote start and end, fades, silent lead,
   fade curve, show-length, and the notes (one or two sections), and validates
   before it will build.
3. When the user taps Build, the panel calls `sendPrompt` and the spec arrives as
   the next message, in this shape:

   ```
   Build the quoter from this intake:
   video: <id>
   title: <title>
   source: <source or (none)>
   start (full at): 4:18
   end (fade-out from): 5:16
   fade-in: 6s
   fade-out: 7s
   silent lead: 0s
   fade curve: smooth
   show length: on
   notes layout: one section
   notes:
   <notes prose, may be several paragraphs>
   ```

   Two-section layout instead reads `notes (above the line):` followed by the
   prose, then `listen prompt (below the line):` and the prompt line.
4. Parse the spec and build.

### The timing convention

`start` is where the audio is fully up. `end` is where the fade-out begins. The
played window is widened to carry the fades: playback begins at
`start - fadeIn - silentLead` (silent for the lead, then the fade-in), and stops
at `end + fadeOut`. The quoted content sits clean at full volume from `start` to
`end`. The length badge shows `end - start`.

### Spec to QUOTE block

Parse the mm:ss times to whole seconds and fill the config:

- `videoId` = the ID.
- `start` = the full-at time in seconds.
- `end` = the fade-out-from time in seconds.
- `fadeIn`, `fadeOut`, `silentLead` = the given seconds. `0` for a hard cut or no
  lead.
- `fadeCurve` = smooth -> 2, linear -> 1, very gradual -> 3.
- `title` = the card title, verbatim. It is the user's copy.
- `source` = the credit, or `''` if the panel sent `(none)`.
- `sourceUrl` = `''` (auto-links to the video).
- `showLength` = on -> true, off -> false.
- `levelTrim` = 0. Tuned by ear on the live URL, never guessed here.

### Notes markup

The notes live in the markup between the `NOTES` comment markers, inside
`<div class="notes-body">`. Do not put them in the config.

- **One section:** the prose only. One `<p>` per paragraph (split on blank
  lines). No `.listen` block, so no divider line.
- **Two sections:** the prose as `<p>` paragraphs, then the listen prompt as a
  final `<p class="listen">...</p>`. That paragraph's top border draws the line.
- Wrap a film title in `<em>` on its first mention, matching the family. Use the
  user's words as written, including Australian spelling and punctuation.

## Build

1. Copy the canonical quoter and drop its README:

   ```
   cp -r quoter-one-melody-six-modes quoter-<subject>
   rm quoter-<subject>/README.md
   ```

2. In `quoter-<subject>/index.html`:
   - Set the `QUOTE` config block from the spec (see mapping). Keep the mm:ss
     comment on each timing accurate.
   - Rewrite the notes between the `NOTES` markers per the layout.
   - Set the page `<title>` so the repo stays greppable by title.
   - Leave the shared machinery alone.

3. Validate. Extract the script and `node --check` before anything else:

   ```
   sed -n '/<script>/,/<\/script>/p' quoter-<subject>/index.html \
     | sed '1d;$d' > /tmp/q.js && node --check /tmp/q.js
   ```

4. Measure the rendered height with Playwright (Chromium, `--no-sandbox`) over
   the `file://` URL at 900, 700 and 480px widths, reading
   `document.body.scrollHeight`. The IFrame API will not load from `file://`
   (error 153); ignore that, the layout height is still valid. Pick the embed
   height from the measurements (default 480, see below).

## Ship (this family ships on build)

A quoter cannot be tested until it is live: the IFrame API does not run from
`file://`, and the level and crop can only be judged on the live URL. So for this
family, build and ship without a pre-ship wait, then hand the live URL back for
testing. This is a deliberate exception to the general show-first rule.

Once the build validates, in one commit:

1. Write `quoter-<subject>/README.md`. Concise and factual:
   - MOTE name and directory.
   - One line on what it plays.
   - Live GitHub Pages URL.
   - Canvas embed with the chosen height, and the measured heights.
   - Video ID and the quote (start, end, fades, silent lead, curve).
   - Resolved play window (begins at `start - fadeIn - silentLead`, stops at
     `end + fadeOut`) and the length badge value.
   - Notes layout (one or two section).
   - Technical notes worth keeping (title-card curtain, curved fade, crop no-op).
   - Open decisions: level and crop pending live tuning.
   - "Last updated" date and a one-line note on what changed.
   - Never the PAT or the project instructions.
2. Add a row to `QUOTERS.md` (instances table) and, where it fits, the embed
   heights table, and a row to `INDEX.md` (Miscellaneous, live).
3. Commit, then `git fetch`, `git rebase origin/main`, push. Never merge. If
   `INDEX.md` or a registry conflicts on rebase, keep both rows.
4. Verify on the raw URL with a short sleep buffer:
   `https://raw.githubusercontent.com/numberdave-cloud/MPMPT1/main/quoter-<subject>/index.html`.
   Compare `git rev-parse HEAD` against `git ls-remote` to confirm the push.
5. Hand back the live URL, the embed block, and a one-line quote summary. Flag
   the two live-only checks: level (trim by ear) and crop (`?tune=1` if the frame
   needs de-letterboxing).

## Canvas embed

Height 480 is the family default and covers most instances side by side. Some run
shorter (380 to 400). Stacked heights below 660px width vary with notes length,
so re-measure per instance and raise the height if the stacked measurement
exceeds the default.

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/quoter-<subject>/"
  width="100%"
  height="480"
  title="<card title>"
  style="border: none;"
  allow="autoplay"
  loading="lazy">
</iframe>
```

## Non-negotiable technical notes

These break the quoter if changed carelessly. They are why the build is
copy-and-swap, not rewrite.

- **The title card covers YouTube's start-up overlay.** That overlay (title,
  channel, centre button, "More videos", logo) fires on the play event, not on
  hover, so the click-shield cannot stop it. The card is held over the video for
  `REVEAL_HOLD` seconds, then dissolves. Bump the hold if any chrome peeks
  through.
- **Captions** are suppressed with `cc_load_policy: 0` and `unloadModule` calls
  on ready, on a timer, and on play. The flag alone is not enough.
- **Fades are curved, not linear** (`fadeCurve` is the exponent). A linear
  amplitude ramp holds near full then collapses, which reads as a cut.
- **YouTube's `end` playerVar is set past the real end** on purpose. YouTube's
  segment stop is imprecise and would truncate the fade-out. The poll owns the
  real ending.
- **The click-shield** swallows mouse events so YouTube never sees a hover, which
  suppresses its chrome. The PLAY/REPLAY button hides by opacity, never
  `display`, so it does not reflow the card.
- **Source crop** (`--zoom`, `--offx`, `--offy`) defaults to a no-op. A `?tune=1`
  panel dials it by eye for a letterboxed source. Never seen by students.
- **Level** has no automatic normalisation and cannot. Set `levelTrim` by ear on
  the live URL. Reference: -3 dB is x0.71, -6 dB is x0.50.
- **Notes drive height once they run long.** Reach for notes-column width before
  font size (see `QUOTERS.md`).

## Design system

The copied folder already carries the styling, so leave it. For reference:
transparent page, background `#1E1A17`, text `#EAE0D0`, accent `#C07838`, Inter
for UI, Courier New for readouts.
