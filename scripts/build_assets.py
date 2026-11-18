"""Generate every SVG used by the profile README.

Edit the CONTENT section below, then run:  python scripts/build_assets.py
All assets are written to ./assets (no external widgets, no web fonts).
"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets"
OUT.mkdir(exist_ok=True)

# ----------------------------------------------------------------- palette
BG, BG2, BORDER, GRID = "#0B0F19", "#0E1422", "#1E2638", "#1A2234"
TEXT, MUTED, DIM, NEUTRAL = "#E6EDF7", "#8B97AD", "#5B6780", "#6B7A99"
CYAN, INDIGO, VIOLET = "#22D3EE", "#818CF8", "#C084FC"
EMERALD, AMBER, ROSE = "#34D399", "#FBBF24", "#FB7185"

SANS = "'Inter','Segoe UI',-apple-system,BlinkMacSystemFont,'Helvetica Neue',Arial,sans-serif"
MONO = "ui-monospace,'SFMono-Regular','JetBrains Mono',Menlo,Consolas,'DejaVu Sans Mono',monospace"
MONO_W = 0.6  # advance width of a monospace glyph, in em

BASE_CSS = f"""
.sans{{font-family:{SANS}}}
.mono{{font-family:{MONO}}}
@media (prefers-reduced-motion: reduce){{*{{animation:none!important}}}}
"""

# ----------------------------------------------------------------- content
NAME_FIRST, NAME_LAST = "Amine", "Bousmah"
ROLE = "Data & AI Engineer"
LOCATION = "based in paris · fr"
CYCLE_WORDS = ["data platforms", "ml models", "dashboards", "ai automations"]

TERMINAL = [
    ("cmd", "whoami"),
    ("out", [(TEXT, "Data & AI engineer"), (MUTED, " — I turn raw data into reliable products.")]),
    ("cmd", "cat focus.txt"),
    ("out", [(CYAN, "◆ "), (MUTED, "data engineering   "), (VIOLET, "◆ "), (MUTED, "machine learning   "),
             (AMBER, "◆ "), (MUTED, "analytics & bi   "), (EMERALD, "◆ "), (MUTED, "ai automation")]),
    ("cmd", "echo $MOTTO"),
    ("out", [(MUTED, '"build it, measure it, make it better."')]),
]

# Stack: picked from the Malt skill list, kept to what the market asks for most
STACK = {
    "data": ("Data Engineering", "batch · streaming · lakehouse", CYAN,
             ["Python", "SQL", "Spark", "Databricks", "Snowflake", "dbt", "Airflow", "Kafka", "PostgreSQL"]),
    "ai": ("AI & Machine Learning", "ml · genai · mlops", VIOLET,
           ["LLM", "RAG", "AI Agents", "LangChain", "MLflow", "scikit-learn", "XGBoost", "pandas"]),
    "cloud": ("Cloud & DevOps", "cloud · containers · ci/cd", EMERALD,
              ["AWS", "Azure", "Fabric", "Docker", "GitLab CI/CD", "FastAPI"]),
    "bi": ("BI & Automation", "dashboards · workflow automation", AMBER,
           ["Power BI", "Tableau", "n8n", "Make"]),
}

PROJECTS = [
    ("openlakehouse", "OpenLakehouse", "Data Platform", CYAN,
     ["An open-source lakehouse, from raw files", "to an analytics-ready model."]),
    ("velistream", "VeliStream", "Streaming", EMERALD,
     ["Real-time data pipeline with ingestion,", "orchestration and monitoring."]),
    ("hotelforecast", "HotelForecast", "Forecasting", AMBER,
     ["Demand & revenue forecasting", "for the hospitality industry."]),
    ("noshow", "NoShow", "Machine Learning", VIOLET,
     ["Cancellation risk prediction", "and overbooking optimisation."]),
    ("autofacture", "AutoFacture", "AI Automation", ROSE,
     ["Document processing workflow mixing", "AI extraction and business rules."]),
    ("elevenfields", "Eleven-Fields", "Sports Analytics", INDIGO,
     ["Football scouting & analytics app."]),
]

SECTIONS = [("about", "01", "about", CYAN), ("stack", "02", "stack", VIOLET),
            ("work", "03", "selected work", AMBER), ("activity", "04", "activity", EMERALD)]

BUTTONS = [("portfolio", "portfolio", CYAN), ("linkedin", "linkedin", INDIGO), ("email", "email", VIOLET)]


def svg(w, h, body, css="", title=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'width="{w}" height="{h}" viewBox="0 0 {w} {h}" fill="none" role="img">'
            f'<title>{escape(title)}</title><style>{BASE_CSS}{css}</style>{body}</svg>')


def write(name, content):
    (OUT / name).write_text(content, encoding="utf-8")
    print("wrote", name)


def mono_width(text, size, spacing=0):
    return len(text) * (size * MONO_W + spacing)


# ----------------------------------------------------------------- header
def header():
    W, H = 1000, 340
    css = f"""
.word{{opacity:0;animation:cycle 12s infinite}}
.w0{{animation-delay:0s}}.w1{{animation-delay:3s}}.w2{{animation-delay:6s}}.w3{{animation-delay:9s}}
@keyframes cycle{{0%{{opacity:0;transform:translateY(8px)}}3%{{opacity:1;transform:none}}
22%{{opacity:1;transform:none}}25%{{opacity:0;transform:translateY(-8px)}}100%{{opacity:0}}}}
.caret{{animation:blink 1s steps(1) infinite}}
@keyframes blink{{50%{{opacity:0}}}}
@media (prefers-reduced-motion: reduce){{.w0{{opacity:1}}}}
"""
    b = []
    b.append(f"""<defs>
<pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="1" fill="{GRID}"/></pattern>
<radialGradient id="g1" cx="220" cy="140" r="340" gradientUnits="userSpaceOnUse"><stop stop-color="{INDIGO}" stop-opacity=".22"/><stop offset="1" stop-color="{INDIGO}" stop-opacity="0"/></radialGradient>
<radialGradient id="g2" cx="790" cy="175" r="230" gradientUnits="userSpaceOnUse"><stop stop-color="{CYAN}" stop-opacity=".14"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></radialGradient>
<linearGradient id="brand" x1="0" y1="0" x2="1" y2="0"><stop stop-color="{CYAN}"/><stop offset=".5" stop-color="{INDIGO}"/><stop offset="1" stop-color="{VIOLET}"/></linearGradient>
<linearGradient id="edge" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{CYAN}" stop-opacity=".55"/><stop offset=".5" stop-color="{BORDER}"/><stop offset="1" stop-color="{VIOLET}" stop-opacity=".55"/></linearGradient>
<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<clipPath id="card"><rect width="{W}" height="{H}" rx="20"/></clipPath>
</defs>""")
    b.append(f'<g clip-path="url(#card)"><rect width="{W}" height="{H}" fill="{BG}"/>'
             f'<rect width="{W}" height="{H}" fill="url(#dots)"/>'
             f'<rect width="{W}" height="{H}" fill="url(#g1)"/><rect width="{W}" height="{H}" fill="url(#g2)"/></g>')
    b.append(f'<rect x=".75" y=".75" width="{W-1.5}" height="{H-1.5}" rx="19.5" stroke="url(#edge)" stroke-width="1.5"/>')

    # location pill
    pw = mono_width(LOCATION, 12.5) + 44
    b.append(f'<rect x="48" y="44" width="{pw:.0f}" height="30" rx="15" fill="{BG2}" stroke="{BORDER}"/>')
    b.append(f'<circle cx="66" cy="59" r="4" fill="{EMERALD}"><animate attributeName="opacity" values="1;.35;1" dur="2s" repeatCount="indefinite"/></circle>')
    b.append(f'<circle cx="66" cy="59" r="4" fill="none" stroke="{EMERALD}"><animate attributeName="r" values="4;10" dur="2s" repeatCount="indefinite"/>'
             f'<animate attributeName="opacity" values=".6;0" dur="2s" repeatCount="indefinite"/></circle>')
    b.append(f'<text x="80" y="63.5" class="mono" font-size="12.5" fill="{MUTED}">{escape(LOCATION)}</text>')

    # name + role
    b.append(f'<text x="46" y="152" class="sans" font-size="60" font-weight="800" letter-spacing="-1.8" fill="{TEXT}">'
             f'{NAME_FIRST} <tspan fill="url(#brand)">{NAME_LAST}</tspan></text>')
    b.append(f'<text x="48" y="192" class="sans" font-size="22" font-weight="500" fill="{MUTED}">{escape(ROLE)}</text>')

    # cycling line
    fs = 17
    prefix = "$ building "
    b.append(f'<text x="48" y="250" class="mono" font-size="{fs}" fill="{DIM}">{escape(prefix)}</text>')
    x0 = 48 + mono_width(prefix, fs)
    for i, w in enumerate(CYCLE_WORDS):
        cx = x0 + mono_width(w, fs) + 3
        b.append(f'<g class="word w{i}"><text x="{x0:.1f}" y="250" class="mono" font-size="{fs}" fill="url(#brand)">{escape(w)}</text>'
                 f'<rect class="caret" x="{cx:.1f}" y="236" width="9" height="18" rx="1.5" fill="{INDIGO}"/></g>')

    b.append(f'<text x="48" y="300" class="mono" font-size="11.5" letter-spacing="2.2" fill="{DIM}" xml:space="preserve">'
             f'DATA ENGINEERING  /  MACHINE LEARNING  /  ANALYTICS  /  AUTOMATION</text>')

    # pipeline graphic
    sx, px, ox = 628, 782, 936
    rows = [102, 175, 248]
    for x, lab in ((sx, "SOURCES"), (px, "PLATFORM"), (ox, "OUTPUTS")):
        b.append(f'<text x="{x}" y="62" text-anchor="middle" class="mono" font-size="10" letter-spacing="2" fill="{DIM}">{lab}</text>')
    paths = []
    for i, y in enumerate(rows):
        paths.append((f"in{i}", f"M{sx+10},{y} C{sx+70},{y} {px-90},175 {px-40},175", CYAN, i * 0.55))
        paths.append((f"out{i}", f"M{px+40},175 C{px+90},175 {ox-70},{y} {ox-14},{y}", VIOLET, 1.2 + i * 0.55))
    for pid, d, _, _ in paths:
        b.append(f'<path id="{pid}" d="{d}" stroke="#25304A" stroke-width="1.5"/>')
    for pid, d, col, delay in paths:
        for k in range(2):
            begin = delay + k * 1.3
            b.append(f'<circle r="3" fill="{col}" filter="url(#glow)"><animateMotion dur="2.6s" begin="{begin:.2f}s" repeatCount="indefinite">'
                     f'<mpath href="#{pid}" xlink:href="#{pid}"/></animateMotion></circle>')
    for y in rows:  # source nodes
        b.append(f'<circle cx="{sx}" cy="{y}" r="11" fill="{BG}" stroke="{CYAN}" stroke-opacity=".35"/>'
                 f'<circle cx="{sx}" cy="{y}" r="4.5" fill="{CYAN}"/>')
    # platform node
    b.append(f'<rect x="{px-40}" y="135" width="80" height="80" rx="18" fill="{BG2}" stroke="url(#brand)" stroke-width="1.5"/>')
    b.append(f'<rect x="{px-40}" y="135" width="80" height="80" rx="18" fill="none" stroke="{INDIGO}" stroke-width="1.5">'
             f'<animate attributeName="opacity" values=".7;0" dur="2.6s" repeatCount="indefinite"/>'
             f'<animate attributeName="stroke-width" values="1.5;10" dur="2.6s" repeatCount="indefinite"/></rect>')
    cy = 160
    b.append(f'<g stroke="url(#brand)" stroke-width="2" fill="none" stroke-linecap="round">'
             f'<ellipse cx="{px}" cy="{cy}" rx="18" ry="6"/>'
             f'<path d="M{px-18},{cy} v24 a18,6 0 0 0 36,0 v-24"/>'
             f'<path d="M{px-18},{cy+12} a18,6 0 0 0 36,0"/></g>')
    # output nodes: chart / sparkle / window
    icons = [
        f'<path d="M{ox-6},{rows[0]+5} v-5 M{ox},{rows[0]+5} v-10 M{ox+6},{rows[0]+5} v-7"/>',
        f'<path d="M{ox},{rows[1]-7} q1.5,5.5 7,7 q-5.5,1.5 -7,7 q-1.5,-5.5 -7,-7 q5.5,-1.5 7,-7z"/>',
        f'<rect x="{ox-7}" y="{rows[2]-6}" width="14" height="12" rx="2"/><path d="M{ox-7},{rows[2]-2} h14"/>',
    ]
    for y, ic in zip(rows, icons):
        b.append(f'<rect x="{ox-14}" y="{y-14}" width="28" height="28" rx="8" fill="{BG}" stroke="{VIOLET}" stroke-opacity=".45"/>'
                 f'<g stroke="{VIOLET}" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round">{ic}</g>')

    write("header.svg", svg(W, H, "".join(b), css, f"{NAME_FIRST} {NAME_LAST} — {ROLE}"))


# ----------------------------------------------------------------- terminal
def terminal():
    W, fs, lh = 1000, 15, 30
    top = 84
    H = top + lh * (len(TERMINAL) + 1) - 6
    cw = fs * MONO_W
    b = [f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="14" fill="{BG2}" stroke="{BORDER}"/>',
         f'<path d="M1 42 H{W-1}" stroke="{BORDER}"/>']
    for i, c in enumerate(("#FF5F57", "#FEBC2E", "#28C840")):
        b.append(f'<circle cx="{24 + i*20}" cy="21" r="6" fill="{c}"/>')
    b.append(f'<text x="{W/2}" y="25.5" text-anchor="middle" class="mono" font-size="12" fill="{DIM}">amine@paris — ~/about</text>')

    t, x = 0.5, 28
    for i, (kind, val) in enumerate(TERMINAL):
        y = top + i * lh
        if kind == "cmd":
            n = len(val)
            widths = ";".join(f"{k*cw:.1f}" for k in range(n + 1))
            dur = 0.07 * n
            b.append(f'<g opacity="0"><animate attributeName="opacity" to="1" begin="{t:.2f}s" dur="0.01s" fill="freeze"/>'
                     f'<text x="{x}" y="{y}" class="mono" font-size="{fs}" fill="{CYAN}">❯</text></g>')
            cid = f"c{i}"
            b.append(f'<clipPath id="{cid}"><rect x="{x+22}" y="{y-fs}" width="0" height="{fs+6}">'
                     f'<animate attributeName="width" values="{widths}" calcMode="discrete" begin="{t+0.15:.2f}s" dur="{dur:.2f}s" fill="freeze"/></rect></clipPath>')
            b.append(f'<text x="{x+22}" y="{y}" class="mono" font-size="{fs}" fill="{TEXT}" clip-path="url(#{cid})">{escape(val)}</text>')
            t += 0.15 + dur + 0.25
        else:
            spans = "".join(f'<tspan fill="{c}">{escape(s)}</tspan>' for c, s in val)
            b.append(f'<g opacity="0"><animate attributeName="opacity" to="1" begin="{t:.2f}s" dur="0.35s" fill="freeze"/>'
                     f'<text x="{x+22}" y="{y}" class="mono" font-size="{fs}" xml:space="preserve">{spans}</text></g>')
            t += 0.45
    y = top + len(TERMINAL) * lh
    b.append(f'<g opacity="0"><animate attributeName="opacity" to="1" begin="{t:.2f}s" dur="0.01s" fill="freeze"/>'
             f'<text x="{x}" y="{y}" class="mono" font-size="{fs}" fill="{CYAN}">❯</text>'
             f'<rect x="{x+22}" y="{y-fs+2}" width="9" height="{fs+2}" rx="1.5" fill="{INDIGO}">'
             f'<animate attributeName="opacity" values="1;0;1" keyTimes="0;.5;1" calcMode="discrete" dur="1s" repeatCount="indefinite"/></rect></g>')
    write("about.svg", svg(W, H, "".join(b), title="whoami — Data & AI engineer"))


# ----------------------------------------------------------------- stack
def stack():
    """Bento grid: 4 tiles, each with an animated mini-visual + skill chips."""
    import math
    W, gap = 1000, 16
    R1, R2 = 232, 212
    H = R1 + gap + R2
    fs, ph, pgap, rgap = 12, 25, 7, 7
    css = """
.draw{stroke-dasharray:1;stroke-dashoffset:0;animation:draw 7s ease-in-out infinite}
@keyframes draw{0%{stroke-dashoffset:1}28%{stroke-dashoffset:0}100%{stroke-dashoffset:0}}
.bar{transform-box:fill-box;transform-origin:50% 100%;animation:grow 6s cubic-bezier(.2,.7,.2,1) infinite}
@keyframes grow{0%{transform:scaleY(.04)}22%{transform:scaleY(1)}86%{transform:scaleY(1)}100%{transform:scaleY(.04)}}
"""
    defs, body = [], []

    def chips(items, x, y, maxw, col):
        out, cx, cy = [], x, y
        for it in items:
            w = mono_width(it, fs) + 20
            if cx > x and cx + w > x + maxw:
                cx, cy = x, cy + ph + rgap
            out.append(f'<rect x="{cx:.1f}" y="{cy}" width="{w:.1f}" height="{ph}" rx="6.5" fill="{col}" fill-opacity=".08" stroke="{col}" stroke-opacity=".32"/>'
                       f'<text x="{cx + w/2:.1f}" y="{cy + 16.8:.1f}" text-anchor="middle" class="mono" font-size="{fs}" fill="#CBD5E4">{escape(it)}</text>')
            cx += w + pgap
        return "".join(out)

    def tile(key, num, x0, y0, w, h, glow_xy):
        title, sub, col, _ = STACK[key]
        gid = f"gl-{key}"
        defs.append(f'<radialGradient id="{gid}" cx="{glow_xy[0]}" cy="{glow_xy[1]}" r="{max(w, h)*0.7:.0f}" gradientUnits="userSpaceOnUse">'
                    f'<stop stop-color="{col}" stop-opacity=".16"/><stop offset="1" stop-color="{col}" stop-opacity="0"/></radialGradient>')
        return (f'<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="16" fill="{BG2}" stroke="{BORDER}"/>'
                f'<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="16" fill="url(#{gid})"/>'
                f'<circle cx="24" cy="35" r="4" fill="{col}"/>'
                f'<text x="36" y="40.5" class="sans" font-size="17" font-weight="700" fill="{TEXT}">{escape(title)}</text>'
                f'<text x="20" y="64" class="mono" font-size="11.5" fill="{DIM}">{escape(sub)}</text>'
                f'<text x="{w-20}" y="40" text-anchor="end" class="mono" font-size="11" fill="{col}" fill-opacity=".8">{num}</text>')

    # ---- A: data engineering — lakehouse layers with data falling through
    wA = 580
    _, _, col, items = STACK["data"]
    g = [tile("data", "01", 0, 0, wA, R1, (wA - 120, 110))]
    g.append(chips(items, 20, 118, 300, col))
    cx, hw, hh, t = 452, 98, 25, 9
    layers = [(70, "raw", "#1B2540", CYAN, .35), (124, "refined", "#1D2350", INDIGO, .45), (178, "curated", "#291F52", VIOLET, .6)]
    for i, (cy, lab, fill, c, so) in reversed(list(enumerate(layers))):
        g.append(f'<path d="M{cx-hw},{cy} L{cx},{cy+hh} L{cx},{cy+hh+t} L{cx-hw},{cy+t} Z" fill="{fill}" fill-opacity=".9" stroke="{c}" stroke-opacity="{so*.6:.2f}"/>'
                 f'<path d="M{cx},{cy+hh} L{cx+hw},{cy} L{cx+hw},{cy+t} L{cx},{cy+hh+t} Z" fill="{fill}" fill-opacity=".7" stroke="{c}" stroke-opacity="{so*.6:.2f}"/>'
                 f'<path d="M{cx-hw},{cy} L{cx},{cy-hh} L{cx+hw},{cy} L{cx},{cy+hh} Z" fill="{fill}" fill-opacity=".75" stroke="{c}" stroke-opacity="{so}">'
                 f'<animate attributeName="stroke-opacity" values="{so};1;{so}" dur="2.4s" begin="{0.5 + i*0.55:.2f}s" repeatCount="indefinite"/></path>'
                 f'<text x="{cx}" y="{cy+4}" text-anchor="middle" class="mono" font-size="10" letter-spacing="2.5" fill="{c}" fill-opacity=".85">{lab.upper()}</text>')
    for k, dx in enumerate((-46, -16, 16, 46)):
        for j in range(2):
            b = k * 0.6 + j * 1.2
            g.append(f'<circle cx="{cx+dx}" cy="22" r="2.6" fill="{CYAN}" opacity="0">'
                     f'<animate attributeName="cy" values="22;{layers[0][0]};{layers[1][0]};{layers[2][0]};218" keyTimes="0;.25;.5;.75;1" dur="2.4s" begin="{b:.2f}s" repeatCount="indefinite"/>'
                     f'<animate attributeName="fill" values="{CYAN};{CYAN};{INDIGO};{VIOLET};{VIOLET}" keyTimes="0;.25;.5;.75;1" dur="2.4s" begin="{b:.2f}s" repeatCount="indefinite"/>'
                     f'<animate attributeName="opacity" values="0;1;1;1;0" keyTimes="0;.15;.5;.85;1" dur="2.4s" begin="{b:.2f}s" repeatCount="indefinite"/></circle>')
    body.append(f'<g transform="translate(0,0)">{"".join(g)}</g>')

    # ---- B: AI & ML — forecast chart (history drawn, then forecast + band)
    xB, wB = wA + gap, W - wA - gap
    _, _, col, items = STACK["ai"]
    g = [tile("ai", "02", xB, 0, wB, R1, (wB - 60, 40))]
    x1, x2, xn, yt, yb = 20, wB - 20, 260, 80, 140
    n = 44
    pts = []
    for i in range(n + 1):
        u = i / n
        v = 0.38 + 0.32 * u + 0.16 * math.sin(u * 14) + 0.05 * math.sin(u * 37)
        pts.append((x1 + u * (x2 - x1), yb - v * (yb - yt)))
    hist = [p for p in pts if p[0] <= xn + 0.01]
    fc = [p for p in pts if p[0] >= hist[-1][0] - 0.01]
    poly = lambda ps: " ".join(f"{x:.1f},{y:.1f}" for x, y in ps)
    band = [(x, y - 4 - 22 * (x - xn) / (x2 - xn)) for x, y in fc] + [(x, y + 4 + 22 * (x - xn) / (x2 - xn)) for x, y in reversed(fc)]
    for k in range(4):
        yy = yt + k * (yb - yt) / 3
        g.append(f'<path d="M{x1} {yy:.1f} H{x2}" stroke="{GRID}" stroke-dasharray="2 4"/>')
    defs.append(f'<clipPath id="fcclip"><rect x="{xB + hist[-1][0]:.1f}" y="0" width="0" height="{R1}">'
                f'<animate attributeName="width" values="0;0;{x2 - xn + 6};{x2 - xn + 6}" keyTimes="0;.28;.42;1" dur="7s" repeatCount="indefinite"/></rect></clipPath>')
    defs.append(f'<linearGradient id="histg" x1="{x1}" x2="{xn}" y1="0" y2="0" gradientUnits="userSpaceOnUse"><stop stop-color="{CYAN}"/><stop offset="1" stop-color="{INDIGO}"/></linearGradient>')
    g.append(f'<path d="M{xn} {yt - 8} V{yb + 2}" stroke="{DIM}" stroke-dasharray="3 3"/>'
             f'<text x="{xn + 5}" y="{yt - 1}" class="mono" font-size="9.5" fill="{DIM}">now</text>')
    g.append(f'<g clip-path="url(#fcclip)" transform="translate({-xB},0)"><g transform="translate({xB},0)">'
             f'<polygon points="{poly(band)}" fill="{VIOLET}" fill-opacity=".14"/>'
             f'<polyline points="{poly(fc)}" stroke="{VIOLET}" stroke-width="2" stroke-dasharray="4 4" stroke-linecap="round"/>'
             f'<circle cx="{fc[-1][0]:.1f}" cy="{fc[-1][1]:.1f}" r="3.5" fill="{VIOLET}"/></g></g>')
    g.append(f'<polyline class="draw" pathLength="1" points="{poly(hist)}" stroke="url(#histg)" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/>')
    g.append(chips(items, 20, 160, wB - 40, col))
    body.append(f'<g transform="translate({xB},0)">{"".join(g)}</g>')

    # ---- C: Cloud & DevOps — CI/CD pipeline lighting up stage by stage
    yC, wC = R1 + gap, 404
    _, _, col, items = STACK["cloud"]
    g = [tile("cloud", "03", 0, yC, wC, R2, (wC - 60, 30))]
    stages = ["commit", "build", "test", "deploy"]
    xs = [44 + i * (wC - 88) / 3 for i in range(4)]
    yy = 98
    g.append(f'<path d="M{xs[0]} {yy} H{xs[-1]}" stroke="#25304A" stroke-width="2"/>')
    g.append(f'<path d="M{xs[0]} {yy} H{xs[-1]}" stroke="{col}" stroke-width="2" stroke-dasharray="{xs[-1]-xs[0]:.0f}" stroke-dashoffset="{xs[-1]-xs[0]:.0f}">'
             f'<animate attributeName="stroke-dashoffset" values="{xs[-1]-xs[0]:.0f};0;0;{xs[-1]-xs[0]:.0f}" keyTimes="0;.6;.92;1" dur="4.5s" repeatCount="indefinite"/></path>')
    for i, (x, lab) in enumerate(zip(xs, stages)):
        tk = i / 3 * 0.6
        g.append(f'<circle cx="{x:.1f}" cy="{yy}" r="10" fill="{BG}" stroke="#2A3550" stroke-width="1.5"/>'
                 f'<g opacity="0"><animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;{tk:.3f};{tk + .03:.3f};.92;1" dur="4.5s" repeatCount="indefinite"/>'
                 f'<circle cx="{x:.1f}" cy="{yy}" r="10" fill="{col}"/>'
                 f'<path d="M{x-4:.1f},{yy} l2.8,2.8 l5.2,-5.6" stroke="{BG}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></g>'
                 f'<text x="{x:.1f}" y="{yy + 27}" text-anchor="middle" class="mono" font-size="9.5" letter-spacing="1" fill="{DIM}">{lab}</text>')
    g.append(chips(items, 20, 144, wC - 40, col))
    body.append(f'<g transform="translate(0,{yC})">{"".join(g)}</g>')

    # ---- D: BI & Automation — growing bar chart + trend line
    xD, wD = wC + gap, W - wC - gap
    _, _, col, items = STACK["bi"]
    g = [tile("bi", "04", xD, yC, wD, R2, (wD - 120, 110))]
    defs.append(f'<linearGradient id="barg" x1="0" y1="0" x2="0" y2="1"><stop stop-color="{AMBER}"/><stop offset="1" stop-color="{ROSE}" stop-opacity=".55"/></linearGradient>')
    vals = [.32, .45, .38, .55, .5, .66, .6, .74, .7, .84, .8, .95]
    bx0, bw, bg_, base, mh = 318, 13, 8, 186, 118
    tops = []
    for i, v in enumerate(vals):
        x = bx0 + i * (bw + bg_)
        hgt = v * mh
        tops.append((x + bw / 2, base - hgt - 8))
        g.append(f'<rect class="bar" style="animation-delay:{i*0.07:.2f}s" x="{x}" y="{base - hgt:.1f}" width="{bw}" height="{hgt:.1f}" rx="3" fill="url(#barg)"/>')
    g.append(f'<path d="M{bx0 - 6} {base + .5} H{bx0 + len(vals)*(bw+bg_)}" stroke="#2A3550"/>')
    g.append(f'<polyline class="draw" pathLength="1" style="animation-delay:.6s" points="{poly(tops)}" stroke="{TEXT}" stroke-opacity=".7" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"/>')
    # mini automation flow: trigger -> ai -> action, a packet travelling along it
    ny, ns = 106, 30
    nxs = [44, 146, 248]
    defs.append(f'<path id="flow" d="M{nxs[0] + ns/2} {ny} C{nxs[0] + 60} {ny - 22} {nxs[1] - 60} {ny - 22} {nxs[1] - ns/2} {ny} '
                f'M{nxs[1] + ns/2} {ny} C{nxs[1] + 60} {ny + 22} {nxs[2] - 60} {ny + 22} {nxs[2] - ns/2} {ny}"/>')
    g.append(f'<use href="#flow" xlink:href="#flow" stroke="#2A3550" stroke-width="1.5" fill="none"/>')
    glyphs = [
        lambda x, y: f'<path d="M{x+1},{y-7} L{x-4},{y+1} H{x} L{x-1},{y+7} L{x+4},{y-1} H{x} Z"/>',
        lambda x, y: f'<path d="M{x},{y-7} q1.4,5.6 7,7 q-5.6,1.4 -7,7 q-1.4,-5.6 -7,-7 q5.6,-1.4 7,-7z"/>',
        lambda x, y: f'<path d="M{x-5},{y} l3.5,3.5 l6.5,-7"/>',
    ]
    for i, (x, lab) in enumerate(zip(nxs, ("trigger", "ai", "action"))):
        g.append(f'<rect x="{x - ns/2}" y="{ny - ns/2}" width="{ns}" height="{ns}" rx="9" fill="{BG}" stroke="{col}" stroke-opacity=".45"/>'
                 f'<g stroke="{col}" stroke-width="1.6" fill="none" stroke-linecap="round" stroke-linejoin="round">{glyphs[i](x, ny)}</g>'
                 f'<text x="{x}" y="{ny + 34}" text-anchor="middle" class="mono" font-size="9.5" letter-spacing="1" fill="{DIM}">{lab}</text>')
    g.append(f'<circle r="3" fill="{AMBER}" filter="url(#bglow)"><animateMotion dur="2.8s" repeatCount="indefinite" keyPoints="0;1" keyTimes="0;1">'
             f'<mpath href="#flow" xlink:href="#flow"/></animateMotion></circle>')
    defs.append('<filter id="bglow" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="2.5" result="b"/>'
                '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    g.append(chips(items, 20, 162, 280, col))
    body.append(f'<g transform="translate({xD},{yC})">{"".join(g)}</g>')

    content = f'<defs>{"".join(defs)}</defs>{"".join(body)}'
    write("stack.svg", svg(W, H, content, css, "Tech stack: data engineering, AI & machine learning, cloud & DevOps, BI & automation"))


# ----------------------------------------------------------------- project cards
def cards():
    W, H, GAP = 480, 196, 14  # GAP: transparent space under each card (row spacing)
    for slug, name, tag, col, desc in PROJECTS:
        tw = mono_width(tag.upper(), 10.5, 1.4) + 22
        b = [f'<defs><radialGradient id="r" cx="{W}" cy="0" r="260" gradientUnits="userSpaceOnUse">'
             f'<stop stop-color="{col}" stop-opacity=".16"/><stop offset="1" stop-color="{col}" stop-opacity="0"/></radialGradient></defs>',
             f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="16" fill="{BG2}" stroke="{BORDER}"/>',
             f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="16" fill="url(#r)"/>',
             f'<rect x="24" y="24" width="{tw:.1f}" height="24" rx="12" fill="{col}" fill-opacity=".1" stroke="{col}" stroke-opacity=".35"/>',
             f'<text x="{24+tw/2:.1f}" y="40" text-anchor="middle" class="mono" font-size="10.5" letter-spacing="1.4" fill="{col}">{escape(tag.upper())}</text>',
             f'<g stroke="{MUTED}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" fill="none">'
             f'<path d="M{W-42},{46} L{W-28},{32} M{W-38},{32} H{W-28} V{42}"/></g>',
             f'<text x="24" y="98" class="sans" font-size="25" font-weight="700" letter-spacing="-.4" fill="{TEXT}">{escape(name)}</text>']
        for i, line in enumerate(desc):
            b.append(f'<text x="24" y="{128 + i*22}" class="sans" font-size="15" fill="{MUTED}">{escape(line)}</text>')
        b.append(f'<circle cx="30" cy="{H-26}" r="5" fill="#3572A5"/>'
                 f'<text x="42" y="{H-21.5}" class="mono" font-size="12" fill="{DIM}">Python</text>')
        write(f"card-{slug}.svg", svg(W, H + GAP, "".join(b), title=f"{name} — {' '.join(desc)}"))


# ----------------------------------------------------------------- section titles
def titles():
    W, H = 1000, 44
    for slug, num, label, col in SECTIONS:
        fs, ls = 13, 3
        num_w = mono_width(num + " ", fs, ls)
        lab = label.upper()
        end = 2 + num_w + mono_width(lab, fs, ls) + 14
        b = [f'<defs><linearGradient id="l" x1="{end:.0f}" x2="{W}" y1="0" y2="0" gradientUnits="userSpaceOnUse">'
             f'<stop stop-color="{col}" stop-opacity=".6"/><stop offset="1" stop-color="{col}" stop-opacity="0"/></linearGradient></defs>',
             f'<text x="2" y="27" class="mono" font-size="{fs}" letter-spacing="{ls}" font-weight="700">'
             f'<tspan fill="{col}">{num} </tspan><tspan fill="{NEUTRAL}">{escape(lab)}</tspan></text>',
             f'<path d="M{end:.0f} 22.5 H{W}" stroke="url(#l)" stroke-width="1.2"/>']
        write(f"title-{slug}.svg", svg(W, H, "".join(b), title=label))


# ----------------------------------------------------------------- buttons
def buttons():
    H, fs = 44, 13
    for slug, label, col in BUTTONS:
        W = mono_width(label, fs, .5) + 76
        b = [f'<rect x=".75" y=".75" width="{W-1.5:.1f}" height="{H-1.5}" rx="{(H-1.5)/2}" fill="{BG2}" stroke="{BORDER}" stroke-width="1.5"/>',
             f'<circle cx="24" cy="22" r="4" fill="{col}"/>',
             f'<text x="38" y="26.5" class="mono" font-size="{fs}" letter-spacing=".5" fill="{TEXT}">{escape(label)}</text>',
             f'<g stroke="{col}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" fill="none">'
             f'<path d="M{W-30:.1f},27 L{W-21:.1f},18 M{W-28:.1f},18 H{W-21:.1f} V25"/></g>']
        write(f"btn-{slug}.svg", svg(round(W), H, "".join(b), title=label))


if __name__ == "__main__":
    header(); terminal(); stack(); cards(); titles(); buttons()
