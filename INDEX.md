# MOTE Index — MPMPT1

Single source of truth for the MOTE estate. Read this first in any new chat.
Base URL: https://numberdave-cloud.github.io/MPMPT1/<folder>/

Categories: Composition · Mixing · Arranging · Miscellaneous

## Live MOTEs

| MOTE (title) | Folder | Category | Status | README |
| --- | --- | --- | --- | --- |
| MOTE-1 — What is a MOTE? | `mote-1/` | Miscellaneous | live | YES |
| BPM Tap | `bpm-tap/` | Composition | live | YES |
| Chord Explorer | `chord-explorer/` | Composition | live | YES |
| Step Sequencer — Drums | `step-sequencer/` | Composition | live | YES |
| Melodic Step Sequencer | `melodic-sequencer/` | Composition | live | YES |
| Quantisation | `quantise/` | Composition | live | YES |
| Mix Balance [Industrial] | `mix-balance-industrial/` | Mixing | live | YES |
| Mix Balance [Reggae] | `mix-balance-reggae/` | Mixing | live | YES |
| Song Structure Analyser | `song-structure-v2/` | Composition | live | YES |
| Song Structure Analyser — Live Set Export | `song-structure-v3-als-export/` | Composition | live | YES |
| Song Structure Navigator | `song-nav-nowhere/` | Composition | live | YES |
| Vintage Sampler | `vintage-sampler/` | Composition | live | YES |
| Skill Loop Player | `skill-loop-player/` | Miscellaneous | live | YES |
| EQ Explorer | `eq-explorer/` | Mixing | live (v0.1, single source) | YES |
| Vertical Remixing | `vertical-remixing/` | Arranging | live | YES |
| YouTube Quoter [Korven — Apprehension Engine] | `youtube-quoter/` | TBC | live | YES |
| YouTube Quoter [Mick Gordon — Doom brief] | `quoter-mick-gordon-doom-brief-1/` | TBC | live | YES |

## Work in progress (not yet in repo)

| MOTE | Intended folder | Category | Status |
| --- | --- | --- | --- |
| Beat Recreate | `beat-recreate/` | Composition | built locally, pending kit WAVs + MIDI answers |
| Groove Maker (.agr export) | `groove-maker/` | Composition | built locally, not pushed |
| Compression Explorer | `compression-explorer/` | Mixing | fully built, not pushed |

## Archived (moved out of production, still live at new URL)

| Folder | New URL | Note |
| --- | --- | --- |
| `archive/meal-planner/` | .../MPMPT1/archive/meal-planner/ | non-MOTE, kept by request |
| `archive/hello/` | .../MPMPT1/archive/hello/ | pipeline test |
| `archive/sanity-check/` | .../MPMPT1/archive/sanity-check/ | browser sanity check |
| `archive/dev/` | .../MPMPT1/archive/dev/ | no HTML |
| `archive/skill-loop-player-test/` | .../MPMPT1/archive/skill-loop-player-test/ | duplicate of skill-loop-player |
| `archive/chord-sequencer.html` | .../MPMPT1/archive/chord-sequencer.html | loose legacy root file |
| `archive/song-structure.html` | .../MPMPT1/archive/song-structure.html | loose legacy root file, superseded by v2/v3 |

## Conventions
- Nothing exists until it is in GitHub. WIP (incl. source audio) gets committed, not left in a chat.
- Ship-then-tweak: overwrite in place (same folder) for fixes and additions — git history is the undo. Spin a NEW named folder only to protect a version that is live in front of students.
- New MOTE = assign a category before ship (Composition / Mixing / Arranging / Miscellaneous).
- Each MOTE carries its own README.md as session handoff.
- YouTube Quoter instances share one template. Only the config block, the notes prose, and the page `<title>` differ per instance. A fix to the shared machinery must be applied across every `quoter-*` / `youtube-quoter` folder, not just one.
- `.nojekyll` present at root so Pages serves every folder (incl. any with leading underscores).
