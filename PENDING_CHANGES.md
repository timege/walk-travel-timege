# Walk Travel Timege 0.9.6 (45) — draft, NOT compiled

## New changes since the last delivered APK (0.9.5)
1. Plain article titles in the places list. Visited places retain ✓. Map markers remain ? / ✓; no clustering added.
2. A 75-metre transparent preview around every catalog place, with an outer feather of at most 10 metres. Geographic radius, no screen-pixel minimum. Import/sync/clear/restore refresh the previews. They are visual hints only: no exploration or discovery credit.
3. Ocean water stays visible through the fog using the ocean polygons in the map's OpenMapTiles water layer. Inland water is not automatically revealed. Polygon holes preserve islands. Loaded offline tiles supply the same ocean geometry. Unknown/uncached areas still require map data to show their coastline.
4. One map style: Liberty. The normal/light selector and the old preference are no longer used.
5. Offline maps screen: name and download the visible map area (zoom levels 0–16), view actual downloaded MB and progress, pause/resume, show a saved area, delete with confirmation. Saved regions use MapLibre's persistent offline database.
6. Downloads run while the app is visible, pause on leaving, and can be resumed later or after restart. Only one download is active at a time. Completed status requires a precise non-zero resource count. Network errors pause the region. Very large selections and critically low storage are rejected/paused.
7. Offline access does not mark the land explored. Walks, POIs and GPX storage are separate from offline-map deletion.

## Already included from 0.9.4–0.9.5
- Home-screen widget and clear-all places with confirmation.
- Samui article titles visible before a visit and correction of old imported names by article URL (60 points / 27 articles); same IDs and discovery history.
- Glossy sky-blue GPS position marker with white rim, highlight, halo and shadow.

## Product limits
- Downloaded regions include the map and its style resources. Online place search, new route calculation, external article/photo loading still need internet. GPS recording, saved places, opened progress and imported GPX remain local.
- No background-download service. Leaving the app pauses downloads; completed maps stay available.
- Download selection crossing the date line or covering too much land asks the user to choose a smaller area.

## Validation performed without compilation
- Reviewed MapLibre 13.6.1 public API signatures for source queries and offline callbacks.
- Reviewed callback/lifecycle handling, stale asynchronous results, completion states, pause/resume and deletion isolation.
- Parsed Android XML and checked patch reconstruction against the source tree.
- Android compilation, emulator/device checks, flight-mode download/restart/delete testing and sea rendering verification are NOT done yet. They require the user's build approval.

## Build gate
Do NOT dispatch GitHub Actions or update main until the user explicitly approves compilation. Changes are kept on draft/poi-preview-75m; main remains the last delivered 0.9.5 APK source.

## References
- https://maplibre.org/maplibre-native/android/api/-map-libre%20-native%20-android/org.maplibre.android.offline/-offline-region/index.html
- https://maplibre.org/maplibre-native/android/api/-map-libre%20-native%20-android/org.maplibre.android.style.sources/-vector-source/query-source-features.html
- https://github.com/openmaptiles/openmaptiles/blob/master/layers/water/water.yaml
