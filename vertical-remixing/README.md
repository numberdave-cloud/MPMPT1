# Vertical Remixing

**Folder:** `vertical-remixing/`
**Category:** Arranging

Demonstrates vertical remixing (adaptive game audio layering): three stems locked to one
continuous loop, with game states revealing or hiding layers via musically timed fades.

**Live URL:** https://numberdave-cloud.github.io/MPMPT1/vertical-remixing/

## Canvas embed

```html
<iframe src="https://numberdave-cloud.github.io/MPMPT1/vertical-remixing/?v=1"
        width="100%"
        height="560"
        style="border: none;"
        allow="autoplay"
        loading="lazy"
        title="Vertical Remixing"></iframe>
```

Height 560 rather than the usual 600. The widget is a fixed 660 x 508 box (not fluid), and
560 is the exact document height with the advanced panel closed. When the panel is opened the
widget scales itself down to ~0.71 to stay inside the same iframe height, so one number covers
both states with no clipping and no dead space.

## Build state

v1.1, 23 July 2026. Feature complete.

## What it does

- Three stems, one 12-bar loop at 120 BPM, phase-locked and continuous. The loop never stops
  or restarts; gain does all the work.
- Three cumulative states: Explore (layer 1), Alert (1+2), Combat (1+2+3).
- Per-layer mute and exclusive solo. Solo overrides state entirely so any layer can be heard
  alone. Mute subtracts from the active state's stack. Both snap at 10 ms and ignore the grid.
- Any state press wipes all manual mute/solo and reasserts, including re-pressing the current
  state.
- A 12-block strip under each state panel shows the current bar of the loop. Only the active
  state's strip is lit, so it reads as "bar 7 of Explore".
- Run Cycle: automated demo that ping-pongs up and down the state ladder indefinitely. It
  resumes from wherever the widget currently is rather than restarting, and does not restart
  the loop.

## Technical notes

**Audio.** Three OGG Vorbis stems, 44.1 kHz stereo, 24.000000 s each, base64-embedded and
decoded with `atob()`. Loop period is 24.000 s exactly (12 bars @ 120 BPM, 4/4), so every
grid division divides cleanly with no drift and no orphaned boundaries. AudioContext is forced
to 44100 for consistent sample counts across devices. Sources are fired by a lookahead
scheduler at exact multiples of the loop period rather than `loop = true`.

**Quantise.** The grid boundary starts the fade, it does not finish it. Fade length is
independent of the quantise division, so a long fade can run through subsequent boundaries.
Modelled on Ableton clip launch. Defaults: quantise 1/4, fade in 1 bar, fade out 4 bars.

**Fade curves.** Three shapes, selectable per direction. `Smooth` (raised cosine) is the
default and the correct one. `Linear` is linear in amplitude. `Log` is linear across 60 dB and
is retained only as a demonstration of what a badly chosen curve sounds like: it puts the
halfway point of any fade at -30 dB, so fade-outs vanish in the first quarter. Fade in and out
resolve per layer by direction (rising uses fade-in time and curve, falling uses fade-out), so
it stays correct even for non-nested states.

**Run Cycle timing.** Each transition is armed so its fade *completes* on the loop boundary.
Trigger offset = `loop end - fade duration - one sixteenth`, resolved against the current loop
position so the cycle can be armed from any point in a pass. The sixteenth of lead-in lets the
quantiser land the fade start on the intended grid point. With the defaults this puts fade-ins
on bar 12 beat 1 and fade-outs on bar 9 beat 1, both finishing at the top of the next pass.
The offset self-adjusts if the fade lengths are changed in the advanced panel.

**Run Cycle direction.** The states are a linear ladder, so the cycle is a ping-pong rather
than a fixed sequence: it walks up to the top, flips, walks down to the bottom, flips again.
Resuming is unambiguous at either end (Explore can only ascend, Combat can only descend). For
a middle state it reads `lastFrom`, the state most recently departed, to decide whether it is
on the way up or on the way down. Alert reached from Explore continues to Combat; Alert
reached from Combat continues to Explore. With no history it defaults to ascending.

**Cycle interrupts.** Only pressing a *different* state cancels the cycle. Mute, solo, and
re-pressing the current state all leave it running, so a student can inspect layers without
losing the demo. Any manual mute/solo is cleared by the next automatic transition, since a
state change always reasserts its own stack. Pressing Run Cycle again cancels but keeps
playing; Stop ends everything.

**Advanced panel.** Hidden by default. Ten clicks on the "VERTICAL REMIXING" title within a
rolling 3-second window toggles it. Exposes quantise, fade in, fade out, curve in, curve out.

**Layout.** Fixed 660 px box, never fluid. On viewports narrower or shorter than it needs, the
whole box scales as a single unit rather than reflowing, so the ratio always holds.

**Icons.** WebP data URIs (~102 KB total for all three), `object-fit: contain`. Swap them at
the `STATE_ART` constant at the top of the script block.

**Colour feedback.** Layer meters run green while a gain is rising, red while falling,
terracotta when steady and audible, empty when silent. State panels carry the same logic as a
progress bar: green filling across the incoming state, red draining off the outgoing one. A
cued-but-not-yet-fired state pulses green in time with the active quantise division.

**Volume.** Master fader defaults to -10 dB (squared taper), sitting after the stem gains so
it cannot interfere with fade scheduling.

## Known limits / TODO

- File is 3.48 MB because the source stems are 256-308 kbps. Re-encoding to ~128 kbps would
  bring the whole thing to roughly 1.6 MB with no meaningful loss for this use. Not done:
  stems are used as supplied. Revisit if load time is a complaint.
- With quantise set to 2 bars in the advanced panel, bar 12's downbeat is not on that grid, so
  a Run Cycle fade-in slips to the next loop top. Only affects that one setting.
- Category filed as Arranging (first entry in that category). Move to Composition if preferred.

## Last updated

23 July 2026. v1.1: Run Cycle now resumes from the current state using ping-pong direction
logic instead of restarting at Explore; mute and solo no longer interrupt the cycle; added
per-state 12-block bar strips; removed the top-right bar counter and the layer-number labels
from the state panels; embed height 540 to 560.
