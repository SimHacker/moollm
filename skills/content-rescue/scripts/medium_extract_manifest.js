// content-rescue: extract an ordered image manifest + video ids from a Medium page.
//
// WHY: curl of a Medium article is often bot-walled (~5KB stub), BUT:
//   (a) the image CDN (miro.medium.com) is open, and
//   (b) the page embeds window.__APOLLO_STATE__ with every image id + caption,
//       in paragraph order, regardless of lazy-loading.
// So: open the article in a real browser (e.g. the Cursor browser MCP), run this
// via Runtime.evaluate (returnByValue:true) or paste in DevTools console, and pipe
// the output into a manifest.psv for fetch_images.py.
//
// AVOID BACKSLASH-ESCAPING PAIN over CDP: this version uses no regex backslashes
// in the IMAGE manifest path and String.fromCharCode(10) for newlines.

// ---- IMAGE MANIFEST:  "<paraIndex>|<imageId>|<caption>" per line ----
(function () {
  var s = window.__APOLLO_STATE__;
  if (!s) return "ERROR: no __APOLLO_STATE__ (is this a rendered Medium page?)";
  var NL = String.fromCharCode(10), imgs = [];
  for (var k in s) {
    var p = s[k];
    if (p && p.__typename === "Paragraph" && p.type === "IMG" && p.metadata && p.metadata.id) {
      var idx = parseInt(k.split("_").pop(), 10);
      var cap = (p.text || "").split(NL).join(" ").split("|").join("/");
      imgs.push({ idx: idx, id: p.metadata.id, cap: cap });
    }
  }
  imgs.sort(function (a, b) { return a.idx - b.idx; });
  return imgs.map(function (o) { return o.idx + "|" + o.id + "|" + o.cap; }).join(NL);
})();

// ---- VIDEO / EMBED ids (run separately):  "<youtubeId|?>|<title>" per line ----
// (function () {
//   var s = window.__APOLLO_STATE__, NL = String.fromCharCode(10), out = [];
//   for (var k in s) {
//     var m = s[k];
//     if (m && m.__typename === "MediaResource" && m.iframeSrc) {
//       var src = decodeURIComponent(m.iframeSrc);
//       var mt = src.match(/youtube\.com\/(?:embed\/|watch\?v=)([A-Za-z0-9_-]+)/);
//       out.push((mt ? mt[1] : "?") + "|" + (m.title || "").split("|").join("/"));
//     }
//   }
//   return out.join(NL);
// })();
//
// NEXT: paste the IMAGE output into manifest.psv, then:
//   python3 fetch_images.py manifest.psv images --source-url '<article url>'
