# Batman Across the Decades

**Folder:** `batman-decades/`
**Category:** Miscellaneous
**Canvas home:** B1·W1

One line: press a Batman, hear that era's main theme via hidden YouTube playback. Five screen Batmans (1966, 1989, 1995, 2008, 2022), one at a time, exclusive playback. Closing extension for the "same character, different decade" listening discussion.

## Live URL
https://numberdave-cloud.github.io/MPMPT1/batman-decades/

## Canvas embed
```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/batman-decades/?v=1" width="100%" height="320" title="Batman Across the Decades" style="border: none;" allow="autoplay" loading="lazy"></iframe>
```
Height 320 assumes the full five-across row (needs ~820px of column width). In a narrower Canvas column the grid wraps to 4+1 and wants height ~500 instead.

## Build state
v0.1 — shipped unverified by request (Canvas is the test bench). YouTube playback, fade, and ad behaviour not yet confirmed live.

## Technical notes
- YouTube IFrame API, five hidden pre-cued players (no Web Audio, no embedded audio)
- 2-second volume fade-in on every press: setVolume ramp 0 to 100 in 60 steps
- New press cuts the current theme instantly (no crossfade); press the active Batman again to stop
- Stopping re-cues the player at its start time so the next press starts clean
- Yellow bat indicator (base64 PNG embedded in HTML): pulses while buffering, steady with glow while playing
- Images are repo-hosted JPEGs alongside index.html, 600x600, referenced relatively

## Video IDs and start times
| Year | Composer | Video ID | Start |
| --- | --- | --- | --- |
| 1966 | Hefti | vRic84u4aPs | 0:10 |
| 1989 | Elfman | 8JtDHoK9KL8 | 0:00 |
| 1995 | Goldenthal | 4cZBRwV4z9A | 0:00 |
| 2008 | Zimmer / JNH | BdnkbXA_piI | 0:00 |
| 2022 | Giacchino | Cwcinb2OxUo | 0:00 |

Start times are single constants in the BATMEN array in index.html. If a video dies or region-blocks, swap the ID there.

## Open TODOs
- Live verification: correct themes, fade sound, pre-roll ad behaviour per video
- 2008/2022 start times flagged as possibly changing
- Confirm embed height against the real Canvas column width

Last updated: 2026-08-06 — initial ship (v0.1).
