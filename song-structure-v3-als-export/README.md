# Song Structure Analyser — Live Set Export

**Directory:** `song-structure-v3-als-export/` · **Category:** Composition

Same tap-along section analysis as v2, plus export of the tapped structure as an Ableton Live Set (`.als`) with locators.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/song-structure-v3-als-export/

## Canvas iframe embed

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/song-structure-v3-als-export/" width="100%" height="600" title="Song Structure Analyser — Live Set Export" style="border: none;" allow="autoplay" loading="lazy"></iframe>
```

Height 600 (default). Adjust if clipped in Canvas.

## Build state

Live.

## Technical notes

Single self-contained HTML, ~60 KB. No playback audio; `atob()` used for the `.als` template blob, written out via gzip. Locator time in beats = (bar - 1) * 4.

## Open TODOs

None tracked.

## Last updated

2026-07-14 — README backfilled from repo inspection. Audio specs marked "verify" were inferred, not read from a spec sheet; confirm at next edit.
