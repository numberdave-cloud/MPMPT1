# Brief Generator

**Directory:** `brief-randomiser/`

A slot-machine style creative-prompt generator for media composition. Each press of NEW BRIEF lands a random one-off scoring brief (genre, scene, target emotion, style reference, required and forbidden instrumentation, and a curveball constraint). It is a reflection stimulus: students read the brief and think through how they would approach it while keeping their own voice, rather than actually writing to it.

## Live URL
https://numberdave-cloud.github.io/MPMPT1/brief-randomiser/

## Canvas embed
```
<iframe src="https://numberdave-cloud.github.io/MPMPT1/brief-randomiser/"
  width="100%" height="680" style="border: none;"
  title="Brief Generator" allow="autoplay" loading="lazy"></iframe>
```
Height 680 (above the 600 default): the seven brief fields at the larger type size plus the NEW BRIEF / COPY button row run past 600. 680 clears the tallest common brief without an internal scrollbar.

## Build state
Shipped v1. Single self-contained HTML file. No external libraries, no audio.

## Technical notes
- No Web Audio. This MOTE is text only, so there is nothing to decode and no loop clock.
- Fully random across all seven reels with no coherence weighting, by design. The chaos is the pedagogical point.
- The final brief is pre-rolled before the animation runs. The cycling frames during a spin are cosmetic only; the landed values are what matter.
- Landing is a staggered cascade (fields lock top to bottom, "the catch" lands last).
- Include vs Off-limits family lock: each MUST INCLUDE item is tagged by instrument family and each OFF-LIMITS item bans a family, so the same thing can never land in both (for example "full orchestra" will not appear against off-limits strings, brass, drums or orchestra). Saxophone is intentionally not tagged as brass, so "off-limits brass" against a saxophone is allowed because a sax is a woodwind.
- Copy button uses the clipboard API with an execCommand textarea fallback for the Canvas iframe sandbox. Disabled mid-spin so a half-landed brief cannot be grabbed.
- Consecutive spins avoid immediately repeating the previous value in each reel.

## Open decisions / TODOs
- None outstanding. Pools, off-limits wording, genre casing (lowercase "of" in Coming-of-Age), field labels, and header/button copy are all approved.
- Possible future ideas, not scoped: lockable individual reels, a short brief history, an optional plausible/weighted mode.

## Last updated
2026-07-20. Initial ship.
