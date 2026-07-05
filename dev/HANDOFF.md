# Dinner Engine — handoff

A personal household meal-planner for Dave (home cook, Campbells Creek, Victoria). Single-file
React component, bundled to a standalone HTML file, hosted on GitHub Pages, run as a PWA on a
Samsung Galaxy phone. Dave is not a programmer, so this chat does all the editing, building and
deploying. He tests on his phone; touch behaviour is the real test.

## Style and working preferences
- Australian English, no em dashes, plain direct language.
- One question at a time, with a concrete recommendation. Confirm before significant features.
- Honest pushback welcomed. Mobile-friendly answers, step-by-step when he is overwhelmed.
- Many of his messages are voice transcriptions, so technical terms may be approximations.
  Interpret charitably before asking.
- After each deploy, tell Dave to fully close and reopen the PWA (service worker / CDN cache delay).
- Multiple backlog items per pass is fine (deploy cost is the same); keep each pass independently
  testable.

## Where everything lives
- LIVE URL: https://numberdave-cloud.github.io/MPMPT1/meal-planner/
- Repo: numberdave-cloud/MPMPT1 (public, branch main, Pages served from repo root)
- Deployed app file in the repo: meal-planner/index.html
- Plain-text catalogue mirror: meal-planner/recipes.json (keep in sync on every catalogue change)
- GitHub fine-grained PAT (stored in the project's custom instructions on purpose; Dave accepts the
  exposure, do not re-litigate it). Write it to /home/claude/.gh_token at session start and never
  echo it in output.
- git identity used for commits: numberdave-cloud@users.noreply.github.com

The bash network allowlist includes github.com, api.github.com, raw.githubusercontent.com and the
usual npm/pypi hosts. It does NOT include *.github.io, so verify deploys against
raw.githubusercontent.com or the Contents API, never the github.io URL.

## The source file
- dinner-engine.jsx (alongside this doc) is the single source of truth for the app code. Everything
  is in this one file: the component, styles, palette, the embedded recipe catalogue, the
  seasonality constant, and all feature logic.
- Component is `export default function KitchenApp()`. entry.jsx (also in the zip) is the tiny build
  wrapper that createRoots it into #root.
- Dark "Mercado" palette in `C`. Fonts: ITC Avant Garde Gothic, embedded inline as base64 woff2
  subsets (do not strip these). SANS / SERIF / MONO font stacks are in scope.
- Five tabs: To-do, Meal Plan, Shop, Stored (Freezer / Staples / Use up / Preserves), Upkeep.

### Key internals worth knowing
- `patch(o,id,fields)` is the main day setter. `weeks` is an object {0..3: [7 day objects]}. A day =
  {id, weekday, date, dateLabel, isToday, type, dish, suggested}. Plans persist by Monday-ISO weekKey
  to localStorage (all keys prefixed "de1:").
- `CATALOGUE` is the big embedded array of recipes (schema below). `CAT_BY_ID` is built from it. A
  placed catalogue dish carries `catId` (entry = CAT_BY_ID[dish.catId]); custom dishes carry
  `dish.ings` and no catId.
- Seasonality is an app constant (produce keys + Victorian season windows). `inSeasonProduce` is the
  set in season this month. Seasonal Picks ranks dishes whose ingredients are in season now.
- Freezer reservation system: placing a freezer meal decrements its Stored qty immediately; clearing
  before the booked day passes returns the qty; once the day passes the reduction is permanent.
  Primitives: reserveFreezer, returnFreezer, passedDay, reconcileFreezer.
- Planning wizard ("plan" view) targets one of the next three weeks via `planWeek` state (1-3). All
  wizard placement (use-these-first chooseDay, placeSeasonalPick, placeFavePick, "Fill the rest"
  goWeeks, placedCatIds) follows planWeek. placeInNextWeek (demo conditional tasks) deliberately
  stays week 1.
- Reveal counters: `seasonalShown` and `favesShown` (both useState(6), stepped +6 up to 24). Seasonal
  Picks and Midweek Faves both render slice(0,shown) with a "Show N more" button, both sorted by
  useUpScoreFor*10 + dishSeasonalScore, tiebreak cookMin then id.
- Use-up matching: USEUP_CATEGORIES maps a generic word to member ingredients (pasta -> rigatoni/
  penne/etc.; greens -> spinach/kale/etc.). Helpers useUpCatMembers / ingMatchesUseUp / dishUsesUseUp.
  Autofill scoring: useUpUrgencyWeight (overdue/today 3, <=7d 2, else 1), useUpScoreFor,
  dishSeasonalScore, chooseBiased. Seasonal autofill draws only from in-season dishes.
  Decision on file: passata is kept SEPARATE from tomato in the category map.
- cookSuggestionsFor(name) returns [{id, name, ref, label, amt, cookMin, serves}] sorted by amount
  then cookMin. The cook-it-as rows show the recipe `ref` and a "{cookMin} min · Serves {serves}"
  line; Seasonal Picks and Faves also show the ref.
- Tick-undo: undoTask state + offerTaskUndo/runTaskUndo, with toggleDoneUndo / completeMaintUndo /
  dismissUserTaskUndo wrapping the home to-do checkboxes (shop, conditional tasks, later tasks,
  upkeep-due Done, user-task dismiss). One shared bottom toast (taskUndoTimer, 6s). Unticking does
  not toast; only completing/dismissing does.
- suggestMemory (useRef, keyed `${o}:${id}`): the last few dish names suggested on each day. suggest()
  excludes history + the current dish + this memory, and guards against re-offering the current dish
  when the pool has alternatives, so "Another" cycles variety. Cap is min(8, pool.length-1).
- Recipe browser type filter: browsePoolFor(type) narrows the Recipes list to the day's category
  (quick -> slot quick; faves -> favesSet; seasonal -> dishSeasonalScore>0), each falling back to the
  full catalogue when empty; fresh/unset show all. A catAll toggle ("Show all dishes") overrides the
  filter; openCatalogue resets catAll to false.
- Freezer item shape: {id, name, serves, qty, loc, goodFor, frozen}. `goodFor` = quality shelf life
  in months (3/6/9/12, default 6; set on the add form). Freezer list sorts by remaining shelf time
  (window - age); "use soon" when within ~30 days of the goodFor window, "past best" once over. Items
  saved before this change fall back to 6 until re-added. (Freezing keeps food safe indefinitely at
  -18C; these are quality windows.)
- Backup/restore (Upkeep tab): exportBackup snapshots every "de1:" localStorage key to a JSON file
  (raw key->string, so it round-trips exactly); onRestoreFile validates {app:"dinner-engine", data};
  confirmRestore writes the keys back verbatim, prunes stale de1: keys, and location.reload()s. State:
  restorePending, restoreErr. No token is in the app, so nothing sensitive is exported.

## Build and deploy procedure (exact, used all session)
Work on /home/claude/handoff/dinner-engine.jsx. Edit it with Python exact-string replaces that
assert an occurrence count; never loose str_replace on the CATALOGUE (use json.loads/dumps round-trip
for catalogue data).

1. Validate (fast, catches JSX errors):
   cd /home/claude/build && cp ../handoff/dinner-engine.jsx . && npx esbuild dinner-engine.jsx \
     --bundle --format=esm --jsx=automatic --external:react --external:react/jsx-runtime \
     --external:lucide-react --outfile=/tmp/check.js
2. Build (the build dir has node_modules: react@18, react-dom@18, lucide-react@0.383.0, esbuild,
   plus entry.jsx):
   npx esbuild entry.jsx --bundle --format=iife --minify --jsx=automatic --outfile=bundle.js
3. Splice into the LIVE shell (fetch meal-planner/index.html first): in Python,
   o=shell.index('<script'); c=shell.rindex('</script>');
   new = shell[:o] + '<script>\n' + bundle + '\n</script>' + shell[c+len('</script>'):]
   The shell has exactly one real </script>; a second '<script' substring is a string literal inside
   the bundle, so rindex is safe.
4. Commit via the GitHub Git Data API (Python urllib): get ref heads/main -> parent -> base tree ->
   POST blob(s) -> POST tree (base_tree + meal-planner/index.html, and recipes.json when the
   catalogue changed, in ONE tree so the two files stay atomic) -> POST commit -> PATCH refs.
5. Verify immediately via the Contents API with Bearer auth and Accept: application/vnd.github.raw at
   ?ref=<new SHA>, and assert committed == built. (raw.githubusercontent.com also works but lags a
   few minutes behind via CDN; the github.io URL is not on the allowlist.)

GOTCHAS:
- The minified bundle is essentially one line, so `grep -c` returns a line count (max 1-2), not an
  occurrence count. Use it only as a presence check.
- Minification unquotes object keys, so id:"rNNN" patterns vanish from the built HTML. Verify
  catalogue presence by recipe NAME strings, which survive minification.

## Recipe catalogue
Source of truth is the live app on GitHub: the embedded CATALOGUE array in dinner-engine.jsx (the
`ct` array in the built index.html), mirrored plain-text at meal-planner/recipes.json. Keep both in
sync, atomically, on every change. recipes-master.xlsx in project knowledge is an optional export
only.

- Current count: 227 recipes, r001 to r227. Next ID: r228.
- Sources: r001 RecipeTin Eats Tonight; r002-r038 Madhur Jaffrey's Indian Cookery; r039-r058 Gourmet
  Traveller Italian; r059-r077 Use It All (Cornersmith); r078-r095 Rosa Mitchell My Cousin Rosa;
  r096-r118 Gino D'Acampo Gino's Italian Escape: A Taste of the Sun; r119-r137 Ostro (Julia Busuttil
  Nishimura); r138-r163 Alison Roman Something from Nothing; r164-r227 RecipeTin Eats Tonight (added
  by the recipe workstream chat). The jsx CATALOGUE is folded from live recipes.json; recipes.json
  refs are authoritative per recipe.

### Recipe schema (each catalogue entry)
{id, name, ref, serves, cookMin, slot, ings:[{q,u,i,s,sea,p}]}
- ref = "Book, p.NN" (author included where needed). Unreadable page ends with "(page to confirm)".
- serves = exactly as the book gives it ("4", "4-6", "6 (as a side)", "makes ~15"). No conversion.
- cookMin = whole minutes, always costed from raw even if the recipe says pre-cooked. Active
  sequential time only; concurrent "meanwhile" steps excluded; passive time (soak/marinate/rest/
  prove/chill) excluded.
- slot = "quick" if cookMin <= 30, else "fresh".
- ing fields: q quantity (number; store upper bound of a range, decimal for fractions, blank for "to
  taste"), u unit (blank for whole counts), i item (named as the thing you buy; drop "dried" on pasta
  shapes; fold near-duplicates into existing names), s staple (true ONLY for the locked six: vegetable
  oil, olive oil, water, black pepper, salt, white sugar), sea + p seasonal tag (item matches an app
  produce key -> sea true and p that key, else sea false and p empty). ASCII only.

### Adding recipes from photos (the loop that works)
1. Confirm the photos are actually present before reading (never fabricate; the Ostro false-start
   incident must not recur). Read recipes.json + index.html live from GitHub.
2. Transcribe per recipecataloguerules.pdf (project knowledge) and the project custom instructions.
3. Assign next IDs from r164 up, never reuse or renumber.
4. Tag produce against the app's produce keys. Flag any NEW produce not in the constant so it can be
   added to the seasonality data too (do not silently commit as sea=false and forget).
5. Inject into CATALOGUE via a json.loads/dumps round-trip (assert pre-count), rebuild, deploy, and
   write recipes.json in the same atomic commit.

## Shipped this session (29 Jun 2026), each its own commit
- Data fix (7184ba2898): page refs r064 p.154, r074 p.93, r094 p.132, r101 p.48 (index.html +
  recipes.json atomic). buildWeek now starts EVERY week blank with Friday = Night Off; removed unused
  DEFAULTS_SEEDED. Caveat: a phone that already saved this week's old demo types keeps showing them
  until the week rolls over (saved plans override defaults).
- Confirmed three earlier "scoped" items were already live: cookSuggestionsFor, slot-type defaults,
  "Themed (Seasonal)" -> "Seasonal" rename.
- Pass 1 (1cc52b7e18): item 7 seasonal-ingredient highlight in ingredient lists (in-season = ember,
  staple = faint); item 11b cookLabel leads with the ingredient name ("rigatoni, 400 g"); item 1
  Seasonal Picks explicit sort + cap 24 + "Show 6 more" (seasonalShown).
- Pass 2 (9cbd1d512e): item 11a USEUP_CATEGORIES + matcher helpers; item 4 use-up-biased autofill
  (urgency-weighted scoring + chooseBiased); seasonal-slot autofill now draws only from in-season
  dishes (fixed a summer dish landing on a July seasonal day).
- Pass 3 (7d7cac0375): item 9 wizard targets weeks 1/2/3 via planWeek + a week selector; item 8
  PLANNED WEEKS home block.
- Pass 3 polish (6b698f5d2f): PLANNED WEEKS is now a row of four horizontal blocks (this week, next,
  2 weeks, 3 weeks); a fully planned week shows a brighter border/fill, no n/7. Weekly shop task
  hidden when the list is empty. Plan-next-week to-do removed. Midweek Faves now mirror Seasonal
  Picks (favesShown 6 + show-more to 24, scored by use-up + seasonal).
- Pass 4a (4b2231d483): close (x) on the cook-it-as list (collapses without scrolling/picking);
  book + page shown on cook suggestions and Seasonal Picks (Faves already had it); item 10 freezer
  goodFor shelf life (3/6/9/12, default 6) driving use-soon / past-best and soonest-to-expire sort.
- Pass 5 (cdcb9301d8): item 5 backup/restore in Upkeep (export all de1: keys to JSON; validated
  restore with a confirm step that replaces everything and reloads). No token in the app.
- Five to-do fixes + catalogue recovery (59af1e556d, current): (1) cook-it-as suggestions show cook
  time and serves; (2) the use-up day picker shows the dish on a taken day and all day pickers show
  the full recipe name (no ellipsis); (3) ticking a home to-do item offers a 6s Undo toast;
  (4) per-day suggest memory so "Another" cycles variety instead of repeating; (5) picking a category
  on a day filters the Recipes browser to that category (quick/faves/seasonal), with a "Show all
  dishes" escape; fresh/unset still show all. This same deploy ALSO recovered 64 recipes: an interim
  build had reverted r164-r227 in index.html (see the rollback note in gotchas); the catalogue was
  re-folded from live recipes.json (227) with the five fixes kept, so index.html and recipes.json are
  back in sync at 227.

## Shipped this session (5 Jul 2026), one atomic commit
Five app-change items in a single build + deploy (dev/dinner-engine.jsx + meal-planner/index.html +
this doc; recipes.json unchanged, catalogue still 227).
- (1) Use-up matcher precision fix. ingMatchesUseUp no longer matches on a single shared token.
  Category members (pasta/greens) still match by exact name; otherwise EVERY literal (non-category)
  word of the use-up name must be present in the ingredient. Added cookLiteralWords; dishUsesUseUp
  and cookSuggestionsFor now pass literal words. Result: "white wine" no longer pulls white-rice
  dishes, colour/qualifier words stop over-matching. Tested on the live catalogue.
- (2) Meal Plan placed-dish fave moved onto the book/page line as a star-only toggle (filled violet =
  faved, muted outline = not); the "Fave"/"Faved" text is gone. Shows whenever day.dish.catId exists.
- (3) Meal Plan placed-dish action row is now icon-only, uniform 38x38 squares (new iconBtn style):
  Ingredients, Add to shop, Move, Edit, Clear. "Recipes" dropped from a placed dish (clear, then
  browse). Move uses ArrowUpDown (up/down) and still opens the day picker. Suggested-state
  Another / Use this kept as labelled buttons on their own line above the icon row.
- (4) To-do Tonight card: the meal name renders ALL CAPS via CSS textTransform on the name div. The
  "No dinner set" placeholder also uppercases; flagged to Dave, easy to scope to the name only later.
- (5) Night Off suggestion pool gained "Dry white toast" and "Drink ten to fifteen beers" alongside
  Takeaway / Leftovers (POOLS.off).

OPEN QUESTION for Dave: after the matcher fix, "tomato puree" matches nothing, because the catalogue
stores the concentrated product as "tomato paste" (15 dishes) and the thin one as passata. Decide
whether "tomato puree" should alias to tomato paste (UK sense) or passata (US sense) so it surfaces
dishes. Nothing added yet.

CURRENT LIVE COMMIT: this 5 Jul 2026 five-item pass (previous tip 59af1e556d; interim HEAD 0b7578625b).

## Backlog status
- DONE: items 1, 4, 5, 7, 8, 9, 10, 11, plus the seasonal-slot autofill fix and the two UI tweaks
  (close-x, show ref).
- DROPPED by Dave: item 6 (cooked log) — "don't care about it".
- PARKED by Dave: item 3 (structured recipe data, e.g. passive time). Would power "start the night
  before" soak/marinate nudges (the fresh-cooking sibling of the defrost reminder). A field is inert
  until a feature reads it, and populating it means re-reading all 163 methods, so only build on a
  concrete need.
- REMAINING (the last real feature): item 2 defrost reminder. Plan: generate a calendar event / .ics
  "Defrost [meal]" for a planned freezer meal. The in-app "Defrost X tonight" nudge already exists on
  the Tonight card (defrostTomorrow uses [...weeks[0],...weeks[1]] to find tomorrow's freezer dish).
  DECISION PENDING from Dave: when the nudge/event fires (evening before vs morning of). Not built.
- Default freezer shelf life chosen by Dave: 6 months (already the app default).

## Data pending Dave's book lookup (still "(page to confirm)")
- r015 p.135, r029 p.158, r038 p.146 — guessed pages to verify against the book.
- r157 Buttered Tomato Soup — no page at all.

## Known code gotchas
- CSS stacking: a transform on a SwipeRow creates a stacking context that hides dropdowns behind
  rows. Use left positioning, never transform.
- Large str_replace into the CATALOGUE array can fail silently. Build new entries in a script and
  inject via a json.loads / json.dumps round-trip, asserting the expected pre-count first.
- STANDING FIRST STEP every session, before any build: fetch live meal-planner/recipes.json and
  confirm the jsx CATALOGUE count matches it. The recipe workstream is a SEPARATE chat that commits
  r-numbered recipes to this same repo in parallel, so the jsx in a handoff zip can be behind live
  within hours. If counts differ, re-fold the live recipes.json into the jsx CATALOGUE (json round-
  trip; r001-r163 etc. stay byte-identical, only new IDs are added) and rebuild from that.
- Incident on 29-30 Jun 2026 (do not repeat): a rebuild from a 163-recipe jsx reverted r164-r227 in
  index.html (recipes.json untouched, so the two went out of sync). Caught via the commit parent not
  matching the expected SHA. Recovered by folding live recipes.json (227) back into the jsx with all
  feature code preserved and redeploying. Also added a pre-commit guard that re-checks the live
  recipe count right before the index.html write. recipes.json plus GitHub history are the recovery
  path if the catalogue ever reverts again.
- The de1:pantry localStorage key is orphaned (Pantry tab was removed) and harmless; the backup will
  carry it through but nothing reads it.
