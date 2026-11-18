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

STACK = [
    ("Data Engineering", CYAN, ["Python", "SQL", "Spark", "Kafka", "ClickHouse", "PostgreSQL"]),
    ("Machine Learning", VIOLET, ["pandas", "scikit-learn", "LightGBM", "LLMs", "Forecasting"]),
    ("Analytics & BI", AMBER, ["Power BI", "Power Query", "Excel", "Streamlit", "Plotly"]),
    ("Cloud & Automation", EMERALD, ["Azure", "Fabric", "Docker", "FastAPI", "n8n", "Git"]),
]

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
    W, gap = 1000, 16
    cw = (W - gap * 3) / 4
    fs, ph, pgap, rgap, pad = 12.5, 26, 8, 10, 20
    layouts, max_rows = [], 0
    for _, _, items in STACK:
        rows, cur, xw = [], [], 0
        for it in items:
            w = mono_width(it, fs) + 22
            if cur and xw + pgap + w > cw - 2 * pad:
                rows.append(cur); cur, xw = [], 0
            cur.append((it, w)); xw += (pgap if len(cur) > 1 else 0) + w
        rows.append(cur)
        layouts.append(rows); max_rows = max(max_rows, len(rows))
    H = 74 + max_rows * (ph + rgap) + 10
    b = []
    for ci, ((title, col, _), rows) in enumerate(zip(STACK, layouts)):
        x0 = ci * (cw + gap)
        b.append(f'<rect x="{x0+.5:.1f}" y=".5" width="{cw-1:.1f}" height="{H-1}" rx="14" fill="{BG2}" stroke="{BORDER}"/>')
        b.append(f'<rect x="{x0+pad:.1f}" y="0" width="36" height="2.5" rx="1.25" fill="{col}"/>')
        b.append(f'<text x="{x0+pad:.1f}" y="40" class="sans" font-size="15.5" font-weight="700" fill="{TEXT}">{escape(title)}</text>')
        b.append(f'<text x="{x0+cw-pad:.1f}" y="40" text-anchor="end" class="mono" font-size="11" fill="{DIM}">0{ci+1}</text>')
        for ri, row in enumerate(rows):
            y = 60 + ri * (ph + rgap)
            x = x0 + pad
            for it, w in row:
                b.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{ph}" rx="7" fill="{col}" fill-opacity=".08" stroke="{col}" stroke-opacity=".3"/>'
                         f'<text x="{x+w/2:.1f}" y="{y+17.5}" text-anchor="middle" class="mono" font-size="{fs}" fill="{TEXT}">{escape(it)}</text>')
                x += w + pgap
    write("stack.svg", svg(W, H, "".join(b), title="Tech stack"))


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
