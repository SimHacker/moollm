# Temporal Semantic Zoom

*Don Hopkins · August 2026*

**Thesis:** Semantic zoom applies to time as well as space. Tag a recording live with lightweight marks, then play it back warped to the density of what you cared about — *one wow per second* — and let the same semantic track drive visual scale, conditional hiding, and summary length.

Part of the **pie-stack-views** design cluster ([README](README.md)). Critique origin: [DYE-A-TRIBE](../DYE-A-TRIBE.md). The parameter model is [Sparse View Overlays](SPARSE-VIEW-OVERLAYS.md); the spatial version is [Pumping Up Pie Menus](PUMPING-UP-PIE-MENUS.md).

---



## Tags as temporal testimony

Drop lightweight tags while something is happening — say *wow* aloud, or tap, and a timestamped mark lands on the track. The marks are the temporal form of the scale-as-testimony argument ([Views as Testimony](VIEWS-AS-TESTIMONY.md)): each one is a recorded judgment that this moment mattered, cheap enough to make without leaving the moment.

## The shipped precedent

The pattern shipped at Interval Research. Marc Davis's **MediaFlow** ([design document](https://donhopkins.com/home/interval/mediaflow-design.html)) was a visual programming language for video processing with semantic annotation tracks — semantic video before vision AI existed — whose operations included process, edit, filter, cut, **time warp**, overlay, and recombine. **MediaGraph**'s time-warping component analyzed those semantic tracks and could play a sitcom back at *one joke per five seconds*.

## Warping more than the clock

Playback rate is only one of the parameters the semantic track should drive. The same track can control visual scale, conditional hiding, and summary length — the whole overlay parameter set, keyed to time — so one bike ride renders *around wow*, *around yikes*, *around beautiful*, or *around green*, each tag raising a different city out of the fog. A tour recorded once becomes as many films as it has tag vocabularies, and the vocabularies compose: *around beautiful, but only where someone else also said wow*.

## The eBike Safari case

eBike Safari's ride playback already does the degenerate version: it detects when you stopped moving and lets you skip over the dead time. That detection is a semantic track that nobody had to author — *not moving* is a tag derived automatically from the telemetry — which is the unifying observation: manual wow-taps and derived metrics are the same kind of signal, timestamped judgments about interestingness, differing only in who or what did the judging.

The next steps follow from treating them that way. Map scale synchronized to speed — low-pass filtered so the camera breathes smoothly instead of twitching with every pedal stroke — zooming in on interesting sections and fast-forwarding over boring ones, where *interesting* can be any metric: tags, speed, scenery density, someone else's testimony. And beyond the mechanical couplings, the camera should zoom in and out intelligently, as useful and natural for the viewer — behavior that still needs to be designed, which is exactly why the API must not prejudge it.

Live, the same signal inverts. During playback *not moving* is dead time to skip; on the ride it is dwell — the bicycle's hover event. Pause the bike and the map starts zooming in, raising nearby points of *your* interest out of the fog, and opens a popup for the address you are standing in front of: website, reviews, hours, whatever sources the node offers. Stopping is the ride-scale version of the pie menu's dwell timing ([Reselection](RESELECTION.md)): people point at what they are interested in, and a stopped bicycle is pointing at where it stands. Ride on and it all folds away again, reversibly — fog-of-war disclosure ([Pumping Up Pie Menus](PUMPING-UP-PIE-MENUS.md)) with the city as the menu.

So the API contract has three separable parts: **signals** (any time-keyed metric — tags, telemetry, derived analysis), **conditioning** (low-pass filters, hysteresis, thresholds — whatever turns a raw signal into something fit to drive a continuous parameter), and **bindings** (which overlay, camera, or playback parameter the conditioned signal drives). Get that separation right and the intelligent-camera design becomes a matter of authoring signals and bindings — editable data, per the configuration argument in [Reselection](RESELECTION.md) — rather than rewriting the player. The dwell-zoom above is the proof case: the same *not moving* signal, conditioned with a dwell threshold, bound to map zoom and popup disclosure in live mode and to fast-forward in playback mode — two behaviors, one track, zero new machinery.

## The natural-language warp

The gap between a natural-language description of the warp — *linger on anything beautiful, skim the straightaways, never cut a sentence in half* — and the actual mapping parameters is the adventure-compiler pattern once more: the LLM compiles what the editor means into what the timeline needs. The editor's contract is the same one demanded everywhere in this series: the compiled warp must be inspectable, adjustable, and reversible, so the description and the parameters stay two views of one editable thing.

---



## Related

- [DYE-A-TRIBE](../DYE-A-TRIBE.md) — the critique this cluster grew out of
- [Sparse View Overlays](SPARSE-VIEW-OVERLAYS.md) — the parameter set being keyed to time
- [Views as Testimony](VIEWS-AS-TESTIMONY.md) — tags as judgments, views as opinions
- [Pumping Up Pie Menus](PUMPING-UP-PIE-MENUS.md) — the spatial version of the same zoom
- [MediaFlow design document](https://donhopkins.com/home/interval/mediaflow-design.html) — Marc Davis, Interval Research
- [eBike Safari](https://github.com/SimHacker/WillWrightShowForFood/tree/main/apps/ebike-safari) — ride playback with stop detection; the signal/conditioning/binding testbed

