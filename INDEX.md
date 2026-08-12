# MOTE Index — MPMPT1

Single source of truth for the MOTE estate. Read this first in any new chat.
Base URL: https://numberdave-cloud.github.io/MPMPT1/<folder>/

Categories: Composition · Mixing · Arranging · Trainers · Miscellaneous

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
| Song Structure Analyser [Live Set Export + Detailed] | `song-structure-v4-als-export/` | Composition | live | YES |
| Song Structure Navigator | `song-nav-nowhere/` | Composition | live | YES |
| Vintage Sampler | `vintage-sampler/` | Composition | live | YES |
| Skill Loop Player | `skill-loop-player/` | Miscellaneous | live | YES |
| EQ Explorer | `eq-explorer/` | Mixing | live (v0.1, single source) | YES |
| Vertical Remixing | `vertical-remixing/` | Arranging | live | YES |
| YouTube Quoter [Korven — Apprehension Engine] | `youtube-quoter/` | Miscellaneous | live | YES |
| YouTube Quoter [Mick Gordon — Doom brief] | `quoter-mick-gordon-doom-brief-1/` | Miscellaneous | live | YES |
| YouTube Quoter [NIN — Ruiner instrumental] | `quoter-ruiner-instrumental-solo/` | Miscellaneous | live | YES |
| YouTube Quoter [Drive — opening credits] | `quoter-drive-opening-credits/` | Miscellaneous | live | YES |
| Groove Maker | `groove-maker/` | Composition | live (v0.1, audibly unverified) | YES |
| Orchestra Stems | `orchestra-stems/` | Miscellaneous | live | YES |
| Compression | `compression-explorer/` | Mixing | live | YES |
| Interval Trainer | `interval-trainer/` | Trainers | live (v0.9) | YES |
| Tuning Practice | `tuning-practice/` | Trainers | live (v1.0) | YES |
| Scene Scorer — Drive [Temp Track] | `scene-scorer-drive/` | Miscellaneous | live (levels untested) | YES |
| Custom Scene Scorer | `custom-scene-scorer/` | Miscellaneous | live (phantom error-150 fix applied, pending live verification) | YES |
| Batman Across the Decades | `batman-decades/` | Miscellaneous | live (v0.2, playback unverified) | YES |
| Energy Dial | `energy-dial/` | Miscellaneous | live (v1.0, untested) | YES |
| Case Study Search Helper | `case-study-search-helper/` | Miscellaneous | live (v1.0, not yet verified in Canvas) | YES |

## Work in progress (not yet in repo)

| MOTE | Intended folder | Category | Status |
| --- | --- | --- | --- |
| Beat Recreate | `beat-recreate/` | Composition | built locally, pending kit WAVs + MIDI answers |

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
- New MOTE = assign a category before ship (Composition / Mixing / Arranging / Trainers / Miscellaneous).
- Each MOTE carries its own README.md as session handoff.
- YouTube Quoter instances share one template and are catalogued in `QUOTERS.md` at repo root. Read that before touching any quoter. A fix to the shared machinery must be applied across every folder listed there, not just one.
- `arcade-high-scores/` is a shared leaderboard service, not a MOTE. Not listed in the table above; it backs Interval Trainer.
- `.nojekyll` present at root so Pages serves every folder (incl. any with leading underscores).
