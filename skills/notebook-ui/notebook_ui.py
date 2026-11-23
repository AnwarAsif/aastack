"""Small helpers for readable, consistent notebooks. Works without pandas for the HTML helpers.

    import notebook_ui as ui
    T = ui.load_theme(); ui.apply_chart_style(T)
    ui.callout("good", "Top 100 leads ready")
    ui.kpi_row([("Leads", 100), ("Precision@100", "0.31")])
    ui.style_table(df, color_col="score")
"""
import html
import json
import pathlib

_DEFAULT = pathlib.Path(__file__).resolve().parents[2] / "themes" / "default.json"


def load_theme(path=None):
    return json.loads(pathlib.Path(path or _DEFAULT).read_text())


def fmt(x, kind="num"):
    """One place for number formats. kind: num, pct, int, money."""
    if x is None or x != x:
        return "-"
    if kind == "pct":
        return f"{x * 100:.1f}%"
    if kind == "int":
        return f"{int(round(x)):,}"
    if kind == "money":
        return f"{x:,.0f}"
    return f"{x:,.2f}"


def _show(h):
    try:
        from IPython.display import HTML, display
        display(HTML(h))
    except ImportError:
        print(h)


def callout_html(kind, text, theme=None):
    t = theme or load_theme()
    c = t["status"].get(kind, t["colors"]["accent"])
    icon = {"good": "OK", "warn": "!", "bad": "X", "info": "i"}.get(kind, "i")
    return (f'<div style="border-left:4px solid {c};background:{t["colors"]["surface"]};padding:10px 14px;'
            f'margin:8px 0;border-radius:4px;color:{t["colors"]["text"]}"><b style="color:{c}">{icon}</b> '
            f'{html.escape(text)}</div>')


def callout(kind, text, theme=None):
    _show(callout_html(kind, text, theme))


def kpi_row_html(items, theme=None):
    t = theme or load_theme()
    cells = "".join(
        f'<div style="flex:1;min-width:140px;border:1px solid {t["colors"]["border"]};border-radius:8px;padding:10px 14px">'
        f'<div style="color:{t["colors"]["muted"]};font-size:12px">{html.escape(str(k))}</div>'
        f'<div style="font-size:24px;font-weight:700;color:{t["colors"]["text"]}">{html.escape(str(v))}</div></div>'
        for k, v in items)
    return f'<div style="display:flex;gap:12px;flex-wrap:wrap;margin:8px 0">{cells}</div>'


def kpi_row(items, theme=None):
    _show(kpi_row_html(items, theme))


def style_table(df, color_col=None, bar_col=None, theme=None, max_rows=100):
    """Return a pandas Styler: header colours from the theme, one colour-coded column, optional bar column."""
    t = theme or load_theme()
    s = df.head(max_rows).style.set_table_styles([
        {"selector": "th", "props": [("background", t["colors"]["surface"]), ("color", t["colors"]["text"]),
                                      ("border-bottom", f"1px solid {t['colors']['border']}"), ("text-align", "left")]},
        {"selector": "td", "props": [("border-bottom", f"1px solid {t['colors']['border']}")]},
    ])
    if color_col:
        s = s.background_gradient(subset=[color_col], cmap="Blues")
    if bar_col:
        s = s.bar(subset=[bar_col], color=t["colors"]["accent"])
    return s


def apply_chart_style(theme=None):
    """Set matplotlib defaults from the theme: palette order, clean axes, readable sizes."""
    import matplotlib as mpl
    t = theme or load_theme()
    mpl.rcParams.update({
        "axes.prop_cycle": mpl.cycler(color=t["categorical"]),
        "axes.spines.top": False, "axes.spines.right": False,
        "axes.edgecolor": t["colors"]["border"], "axes.labelcolor": t["colors"]["text"],
        "text.color": t["colors"]["text"], "xtick.color": t["colors"]["muted"], "ytick.color": t["colors"]["muted"],
        "axes.grid": True, "grid.color": t["colors"]["border"], "grid.linewidth": 0.6,
        "figure.facecolor": t["colors"]["background"], "axes.facecolor": t["colors"]["background"],
        "font.size": 11, "axes.titlesize": 13, "axes.titleweight": "bold", "figure.dpi": 110,
    })
