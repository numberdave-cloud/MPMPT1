# Brief Generator

**Directory:** `brief-randomiser/`

A slot-machine style creative-prompt generator for media composition. Each press of NEW BRIEF lands a random one-off scoring brief (genre, scene, target emotion, style reference, required and forbidden instrumentation, and a curveball constraint). It is a reflection stimulus: students read the brief and think through how they would approach it while keeping their own voice, rather than actually writing to it.

## Live URL
https://numberdave-cloud.github.io/MPMPT1/brief-randomiser/

## Canvas embed
```
<iframe src="https://numberdave-cloud.github.io/MPMPT1/brief-randomiser/"
  width="100%" height="720" style="border: none;"
  title="Brief Generator" allow="autoplay" loading="lazy"></iframe>
```
Height 720 (above the 600 default): the seven brief fields at the larger type size plus the button row stand about 704px tall on a full-width desktop column. 720 clears the tallest brief without clipping the buttons. If the embed column is narrower than a full desktop width, long values may wrap and need a little more height.

## Build state
Shipped. Single self-contained HTML file, no external libraries, no audio. Layout revision: everything now sits in one contained dark panel.

## Technical notes
- No Web Audio. This MOTE is text only, so there is nothing to decode and no loop clock.
- Layout: the panel background is dark but the iframe/body background is transparent, so Canvas (white) shows around the panel as an even 20px frame on top and sides. This replaced the earlier full-bleed dark background. The `--frame` CSS variable controls the inset (20px desktop, 12px under 560px).
- The buttons live inside the panel, below a divider, so the whole device is one unit.
- Fully random across all seven reels with no coherence weighting, by design. The chaos is the pedagogical point.
- The final brief is pre-rolled before the animation runs. The cycling frames during a spin are cosmetic only; the landed values are what matter. Landing is a staggered cascade (fields lock top to bottom, "the catch" last).
- Include vs Off-limits family lock: each MUST INCLUDE item is tagged by instrument family and each OFF-LIMITS item bans a family, so the same thing can never land in both (for example "full orchestra" will not appear against off-limits strings, brass, drums or orchestra). Saxophone is intentionally not tagged as brass, so "off-limits brass" against a saxophone is allowed because a sax is a woodwind.
- Copy button uses the clipboard API with an execCommand textarea fallback for the Canvas iframe sandbox. Disabled mid-spin.
- Consecutive spins avoid immediately repeating the previous value in each reel.

## Open decisions / TODOs
- Frame size is an even 20px on top and sides. The exact top gap cannot be pixel-matched from inside the iframe because Canvas adds its own spacing above the frame. Nudge `--frame` if the balance looks off in situ.
- Panel currently runs near the full width of the Canvas column (minus the frame). Alternative not taken: a narrower centred card. Swap on request.

## Last updated
2026-07-20. Layout reworked into a single contained panel framed by Canvas white; embed height raised to 720 to stop the button row clipping (previous 680 was scrolling).
