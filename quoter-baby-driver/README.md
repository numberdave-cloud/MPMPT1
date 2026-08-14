# Quoter: Baby Driver

**Directory:** `quoter-baby-driver/`

A YouTube Quoter instance. Plays a 1:10 window from Baby Driver (2017), from a ColumbiaPicturesPH upload.

Built from the shared quoter template, copied from `quoter-temp-track-fever/`. See `QUOTERS.md` at repo root for the registry and shared machinery notes.

## Live URL

https://numberdave-cloud.github.io/MPMPT1/quoter-baby-driver/

## Canvas embed

```html
<iframe
  src="https://numberdave-cloud.github.io/MPMPT1/quoter-baby-driver/"
  width="100%"
  height="380"
  title="Baby Driver (2017)"
  style="border: none;"
  loading="lazy"
  allow="autoplay">
</iframe>
```

Height 380, provisional. Measured with placeholder notes: 355px from 900px wide upward, 326px at 800px, 294px at 700px, 522px stacked below 660px. Re-measure once the real notes copy lands, since notes length drives the height.

## Build state

v2, 2026-08-13. Category: Miscellaneous. Copy final. Card title and source credit are Dave's, as given. Deployed for live testing, not yet embedded in Canvas.

## Clip

- Video ID `6XMuUVw7TOM`, ColumbiaPicturesPH upload
- Quote content 2:07 to 3:17 (127s to 197s), displayed length 1:10
- Full volume and card dissolved by 2:07, fade-out begins at 3:17
- Timeline: 2:01 to 2:04 silent and locked out (video rolling under the card, volume zero), 2:04 to 2:07 fade in, full and visible at 2:07, hold to 3:17, 3:17 to 3:20 fade out
- `silentLead` 3s plus `fadeIn` 3s give a 6s card cover from play, so YouTube's overlay is never seen. Card dissolves at 2:07 as full volume arrives.
- Volume starts at 50%, `levelTrim` currently 0 dB

## Source crop

Not set. `--zoom` is 1, a no-op, on the assumption this ColumbiaPicturesPH upload is 16:9 native. If it turns out pillarboxed or letterboxed, the `?tune=1` panel gives zoom and offset sliders, same as the 2001 instance. Confirm on a live view.

## Notes copy

Dave's copy, used as written. Top paragraph on spotting and Wright's edit-to-music approach, prompt line below in the `listen` class. Film title italicised on first mention with `<em>`. Opening letter of the prompt capitalised (Dave sent it lowercase).

A Wright quote from a 2017 interview was built in and then dropped at Dave's call. The quote-block CSS (`.notes-body blockquote`) is left in place but inert, since it is a reasonable thing to reuse if a quote is wanted later.

The prompt line uses the notes column at 291px balanced against a 291px video, widget height 355px.

## Layout

Frame `max-width` 900px, video column 440px, notes column 360px, inherited from the temp-track build. Balanced at 291px each with the placeholder. Re-check once real copy lands.

## Technical notes

Shared machinery identical to every other quoter. Carries the instance-local `silentLead` field and crop machinery inherited from the temp-track build.

- ColumbiaPicturesPH is a studio-affiliated channel, so more durable than a fan upload, but studio clips still get pulled or region-locked. If it goes, the card shows the "could not be loaded" message. Note a backup video ID if needed.
- Film audio, so `levelTrim` may need setting by ear against the other cards.

## Open TODOs

- Tune `levelTrim` by ear.
- Confirm the crop assumption (16:9 native) on a live view.
- Confirm the fade feel and that the overlay stays hidden to 2:07.
- Confirm the folder name before it goes into Canvas.
- Note a backup video ID against takedown.

## Last updated

2026-08-13. Initial build, clip window 2:07 to 3:17, 3s fades, 3s locked-out silent lead, no crop. Then Dave's final copy in (top spotting paragraph, prompt line), a Wright quote added and then dropped at Dave's call.
