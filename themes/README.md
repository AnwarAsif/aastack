# Themes

`default.json` is a neutral theme: text and surface colours, status colours (good, warn, bad, info) and a colour-blind-safe categorical palette (Okabe-Ito).

To use a brand look, copy `default.json` to `<brand>.json` **in your own project**, change the values, and point `notebook_ui.load_theme("themes/<brand>.json")` at it. Keep brand files private: this public repo ships only the neutral theme. Keep status colours separate from brand colours, because a brand red also reads as "bad".
