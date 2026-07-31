# Song Structure Analyser: Live Set Export + Detailed Sections

**Directory:** `song-structure-v4-als-export/` · **Category:** Composition

Tap along to a track marking each bar's section, read detailed songwriting notes per section, then export the tapped structure as an Ableton Live Set (`.als`) with locators.

Supersedes `song-structure-v3-als-export/`, which stays live and untouched. v4 adds the full detailed section content (Function, Features, Quotes) for all seven Verse-Chorus sections and rebuilds the timeline as a fixed 16-bar grid.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/song-structure-v4-als-export/

## Canvas iframe embed

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/song-structure-v4-als-export/" width="100%" height="600" title="Song Structure Analyser: Live Set Export" style="border: none;" allow="autoplay" loading="lazy"></iframe>
```

Height 600 (default).

## Build state

Live. Merged from v2 (detailed section content) and v3 (ALS export), plus timeline and clear fixes.

## Technical notes

- Single self-contained HTML, ~70 KB. No playback audio.
- ALS export: an empty Live 12.4 set is embedded as gzipped XML, base64-encoded, decoded via `atob()`. On export the single `<Locators />` node is spliced with the tapped locators and the set is recompressed via `CompressionStream` and downloaded. Locator time in beats = (bar - 1) * 4, 4/4 fixed.
- Timeline is a fixed 16-bar grid. Each bar is 1/16 of a row, sections wrap to a new row after 16 bars, remaining slots on the active row render as dashed ghost cells. Per-bar tick dividers via a repeating gradient. Selection maps to the global section run, so a section that wraps across rows still highlights and deletes as one unit.
- Detailed section content exists for Verse-Chorus (pop) only. Verse-Hook and Build-Drop show simple content; their Detailed toggle shows a placeholder note.
- Clear All uses a two-tap confirm ("Confirm Clear?"), not `confirm()`, which sandboxed Canvas iframes swallow. Arms for 3 seconds and cancels on any other interaction.
- Info panel hides once Finish is pressed, to keep the iframe within its height.
- Widget content capped at 960px wide.

## Open TODOs

- Detailed content for Verse-Hook and Build-Drop pending a research round.
- The Detailed-toggle placeholder on Verse-Hook / Build-Drop still reads "only available for Verse-Chorus currently, let DJ know" (inherited from v2). Reword when the research round lands.
- Segmentation tick contrast is deliberately subtle. Revisit if it needs to read stronger.

## Last updated

2026-07-31 — Initial ship. New folder off the v2 and v3 merge, with detailed sections, a fixed 16-bar grid timeline, and two-tap clear.
