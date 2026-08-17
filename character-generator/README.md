# Character Generator

**Directory:** `character-generator/`

A slot-machine style prompt generator for character-theme writing. Each press pairs a film-archetype character with a hidden subtext, giving students a one-line brief to sketch or score a short theme that expresses what the character is feeling underneath. Reflection stimulus, same family as the Brief Generator: students read the pairing and think through how they would voice it, they do not have to write to it.

## Live URL
https://numberdave-cloud.github.io/MPMPT1/character-generator/

## Canvas embed
```
<iframe src="https://numberdave-cloud.github.io/MPMPT1/character-generator/"
  width="100%" height="420" style="border: none;"
  title="Character Generator" allow="autoplay" loading="lazy"></iframe>
```
Height 420. Two reels only, so nothing like the Brief Generator's 760. Device renders ~335px at full width, up to ~389px at a narrow Canvas column when the longest subtext wraps to two lines. 420 clears the tallest state with buffer.

## Build state
Shipped, v1.0. Single self-contained HTML file, no external libraries, no audio.

## Technical notes
- No Web Audio. Text only, nothing to decode, no loop clock.
- Two independent reels: 24 characters x 24 subtexts. Drawn separately with no coherence weighting, by design. The cross-pollination is the point (a soldier falling for someone forbidden, a fashion editor seeking revenge).
- Film references for each pool entry are kept as code comments only, hidden from the displayed value, same convention as the Brief Generator.
- Consecutive spins avoid immediately repeating the previous value in each reel.
- The landed pairing is pre-rolled before the animation runs. Cycling frames during a spin are cosmetic. Landing is a staggered two-field cascade.
- Secret combo: roughly 1 in 45 spins fills both reels together with the sumo pair ("A lactose intolerant sumo wrestler" / "who drank four milkshakes at lunch"). When it lands, both values glow in the hot accent and the counter reads 8888 (all nixie segments lit). Not documented in the student-facing instructions, it is meant to be a surprise. The Copy button will copy it as-is.
- Copy button uses the clipboard API with an execCommand textarea fallback for the Canvas iframe sandbox. Disabled mid-spin.

## Open decisions / TODOs
- None outstanding.
- Note (not this MOTE's job): `brief-randomiser/` is still missing from the INDEX table. Add its row next time that repo area is touched.

## Last updated
2026-08-18. Initial ship. Pools grew from 20 to 24 each before ship: added Fashion editor, Dressmaker, Governess, Novelist to characters, and torn between duty and desire, waiting for someone who may never return, realising they married the wrong person, longing for the life they gave up to subtexts, to widen the balance toward drama and romance.
