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
- TRUSTED SOURCES toggle wraps the query in a `site:` OR group. The list is
  25 verified domains covering composer interviews, film-score and
  game-music publications. Small/niche domains (shmuplations.com,
  motionpictures.org, filmmusicfoundation.org, revolvermag.com,
  zeldadungeon.net, awardswatch.com, awardsdaily.com, goldderby.com,
  parade.com, laist.com, collider.com, vice.com) were live-fetched and
  confirmed real on 10 Aug 2026. This matters: squareenixmusic.com was a
  strong candidate until a live check found the domain had expired and been
  bought by affiliate spam, so search snippets alone can't be trusted for a
  domain allowlist. Re-verify the niche domains roughly each semester. The
  toggle is a hard restriction, not a soft preference, so it can return zero
  results for obscure or very new composers. No in-widget warning beyond the
  field hint; worth a line on the Canvas page.
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
- Trusted source list is game-score-light; only a handful of game-specific
  domains (shmuplations.com, gamedeveloper.com, zeldadungeon.net,
  revolvermag.com) survived verification. If case studies lean game-heavy, a
  further targeted pass on game composers (Shimomura, Wintory, Coker, Korb)
  would strengthen it.
- Niche domains need periodic re-verification (see squareenixmusic.com note
  above). Next check due start of next semester.
- Block list currently seven entries (Reddit, Quora, Pinterest, TikTok,
  Facebook, Instagram, YouTube); may grow.
- Student-facing copy for the Canvas page (what the operators mean, and the
  "trusted sources can return zero results" caveat) has not been written or
  approved. All labels inside the widget are structural, not final copy.
- Not yet verified inside a live Canvas iframe (clipboard, open-in-new-tab
  behaviour, and iframe height all pending real-world check).

## Last updated
10 August 2026 — loaded the 25-domain verified trusted-source list
(replacing the placeholder six), expanded block list to include YouTube,
transparent page background outside the card.
