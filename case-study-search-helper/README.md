# Case Study Search Helper

## What it does
Helps students build a paste-ready Google search query for researching a
composer's work on a specific film, TV show, or game, without needing to
know Boolean search syntax. Subject fields plus one-click content-type and
source-blocking chips assemble the query live in a ticker readout at the
bottom.

## Live URL
https://numberdave-cloud.github.io/MPMPT1/case-study-search-helper/

## Canvas embed
```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/case-study-search-helper/"
  width="100%" height="750" style="border: none;"
  title="Case Study Search Helper" allow="autoplay" loading="lazy"></iframe>
```
Height set to 750 (taller than the 600 default) to fit the full stack of
fields, two chip rows, and toggles without internal scrolling.

## Current build state
v1.0, first ship. No audio, no Web Audio API. Verified in headless Chromium
only, not yet checked inside an actual Canvas iframe.

## Technical notes
- Pure HTML/CSS/JS, no external libraries.
- Fields: Composer, Film/Show/Game, Scene or cue (optional), Exact phrase.
- FIND chips (Interview, Score, Soundtrack, Scoring Process, Behind The
  Scenes, Composer Commentary, Analysis, Press Notes) are disabled until
  Composer or Film/Show/Game has text in it, with an inline note explaining
  why. BLOCK chips (Reddit, Quora, Pinterest, TikTok, Facebook, Instagram)
  are always available.
- Multi-word terms auto-quote in the assembled query. Typed quote marks in
  any input are stripped so students can't double-quote themselves into a
  broken string.
- TRUSTED SOURCES toggle wraps the query in a `site:` OR group. Domain list
  is a placeholder pending Dave's review:
  musictech.com, cdm.link, soundonsound.com, filmscoremonthly.com,
  filmtracks.com, soundtrack.net. This is a hard restriction, not a soft
  preference — it can return zero results for obscure or very new
  composers. No in-widget warning about this yet (in-widget teaching text
  is generally avoided per house style); worth a line on the Canvas page.
- WEB RESULTS ONLY toggle (on by default) appends `&udm=14` to the Open in
  Google link only, not to the copyable text, since that parameter has no
  meaning pasted into a search box. This forces Google's plain "Web"
  results view, which removes the AI Overview, People Also Ask, and the
  video/image carousels that otherwise dominate the top of the page.
- Open in Google is a real `<a target="_blank">`, not `window.open()`, so
  it should survive a sandboxed Canvas iframe. Not yet confirmed inside an
  actual Canvas embed.
- Copy button uses the Clipboard API with a `document.execCommand('copy')`
  fallback. May need `allow="clipboard-write"` added to the iframe embed if
  Canvas blocks the Clipboard API in this sandbox — same open question as
  Scene Scorer.

## Open decisions / TODOs
- Trusted source domain list is a starting six, likely thin. No game-score
  specialist sites included yet, only film-score and general music trade
  press. Needs Dave's review and expansion.
- Block list may get more entries; current six were the agreed starting
  point, not necessarily final.
- Student-facing copy for the Canvas page (what AND/quotes/minus/site: mean,
  and the "trusted sources can return zero results" caveat) has not been
  written or approved. All labels inside the widget are structural, not
  final copy.
- Not yet verified inside a live Canvas iframe (clipboard, open-in-new-tab
  behaviour, and iframe height all pending real-world check).

## Last updated
10 August 2026 — first ship.
