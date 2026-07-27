# Brief Generator

**Directory:** `brief-randomiser/`

A slot-machine style creative-prompt generator for media composition. Each press of NEW BRIEF lands a random one-off scoring brief (genre, scene, target emotion, a temp-track reference, required and forbidden instrumentation, and a curveball constraint). It is a reflection stimulus: students read the brief and think through how they would approach it while keeping their own voice, rather than actually writing to it.

## Live URL
https://numberdave-cloud.github.io/MPMPT1/brief-randomiser/

## Canvas embed
```
<iframe src="https://numberdave-cloud.github.io/MPMPT1/brief-randomiser/"
  width="100%" height="760" style="border: none;"
  title="Brief Generator" allow="autoplay" loading="lazy"></iframe>
```
Height 760. The panel is capped at 580px wide and centred (portrait, sheet-of-paper proportions), so on a narrow column the longer values (the catch, sometimes the scene) wrap to two lines and the sheet runs taller than a full-width layout would. 760 clears the tallest brief without clipping the button row.

## Build state
Shipped. Single self-contained HTML file, no external libraries, no audio.

## Technical notes
- No Web Audio. This MOTE is text only, so there is nothing to decode and no loop clock.
- The "current temp track" reel holds 20 real cues, formatted "track by composer". Bernard Herrmann's entry keeps "(Taxi Driver)" because "Main Title" alone is not findable; the rest are track and composer only, deliberately without the source film so students focus on the sound rather than the original picture. No links: students find the tracks themselves.
- Layout: a single dark panel, `max-width: 580px`, centred. The iframe/body background is transparent, so Canvas (white) shows around the panel as a frame. The `--frame` CSS variable sets the minimum inset (20px desktop, 12px under 560px).
- The buttons live inside the panel, below a divider, so the whole device is one unit.
- Fully random across all seven reels with no coherence weighting, by design. The chaos is the pedagogical point. Roughly 2.2 billion possible briefs.
- The final brief is pre-rolled before the animation runs. The cycling frames during a spin are cosmetic only; the landed values are what matter. Landing is a staggered cascade (fields lock top to bottom, "the catch" last).
- Include vs Off-limits family lock: each MUST INCLUDE item is tagged by instrument family and each OFF-LIMITS item bans a family, so the same thing can never land in both. Saxophone is intentionally not tagged as brass, so "off-limits brass" against a saxophone is allowed because a sax is a woodwind.
- Copy button uses the clipboard API with an execCommand textarea fallback for the Canvas iframe sandbox. Disabled mid-spin.
- Consecutive spins avoid immediately repeating the previous value in each reel.

## Open decisions / TODOs
- None outstanding.

## Last updated
2026-07-20. Replaced the "in the style of" composer reel with a "current temp track" reel of 20 specific cues (track by composer). No embed change: height stays 760.
