"""Gera o papel de parede SVG original "Aero Sky" (céu, nuvens, cidade de vidro,
colinas, lagoa e bolhas). A semente é fixa: a imagem sai sempre igual."""

import random

W, H = 1920, 1080


def _cloud(cx: float, cy: float, s: float, opacity: float) -> str:
    puffs = [(-120, 10, 70), (-60, -30, 85), (20, -50, 100), (100, -20, 80),
             (160, 15, 60), (40, 20, 90), (-20, 25, 75)]
    circles = "".join(
        f'<circle cx="{cx + dx * s:.1f}" cy="{cy + dy * s:.1f}" r="{r * s:.1f}"/>'
        for dx, dy, r in puffs
    )
    return f'<g fill="url(#cloud)" opacity="{opacity}" filter="url(#soft)">{circles}</g>'


def _bubble(cx: float, cy: float, r: float, opacity: float) -> str:
    return (
        f'<g opacity="{opacity}">'
        f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="url(#bubble)"/>'
        f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="none" stroke="#FFFFFF" '
        f'stroke-opacity=".55" stroke-width="{max(1.0, r * .04):.1f}"/>'
        f'<ellipse cx="{cx - r * .35:.1f}" cy="{cy - r * .42:.1f}" rx="{r * .38:.1f}" '
        f'ry="{r * .2:.1f}" fill="url(#shine)" transform="rotate(-30 {cx - r * .35:.1f} {cy - r * .42:.1f})"/>'
        f'<circle cx="{cx + r * .45:.1f}" cy="{cy + r * .5:.1f}" r="{r * .08:.1f}" fill="#FFFFFF" opacity=".7"/>'
        f'</g>'
    )


def _towers(rng: random.Random) -> str:
    out = []
    x = 1180
    while x < 1780:
        w = rng.randint(34, 70)
        h = rng.randint(120, 330)
        top = 715 - h
        out.append(f'<rect x="{x}" y="{top}" width="{w}" height="{h}" rx="3" fill="url(#glass)"/>')
        out.append(f'<rect x="{x + w * .15:.1f}" y="{top + 6}" width="{w * .18:.1f}" height="{h - 12}" '
                   f'fill="#FFFFFF" opacity=".35"/>')
        if rng.random() < .35:  # antena
            out.append(f'<rect x="{x + w / 2 - 1.5:.1f}" y="{top - 40}" width="3" height="40" fill="#CFEFFF" opacity=".7"/>')
        x += w + rng.randint(4, 22)
    # torre redonda estilizada
    out.append('<ellipse cx="1470" cy="330" rx="34" ry="34" fill="url(#glass)"/>')
    out.append('<rect x="1462" y="360" width="16" height="355" fill="url(#glass)"/>')
    return f'<g opacity=".6">{"".join(out)}</g>'


def _grass(rng: random.Random) -> str:
    blades = []
    for _ in range(420):
        x = rng.uniform(-20, W + 20)
        base = H + 5
        h = rng.uniform(30, 110) * (1.25 if (x < 500 or x > 1500) else .8)
        lean = rng.uniform(-28, 28)
        w = rng.uniform(4, 9)
        tip_x, tip_y = x + lean, base - h
        blades.append(
            f'<path d="M{x - w:.1f} {base} Q{x + lean * .3:.1f} {base - h * .6:.1f} {tip_x:.1f} {tip_y:.1f} '
            f'Q{x + lean * .3 + w * .4:.1f} {base - h * .55:.1f} {x + w:.1f} {base}Z"/>'
        )
    return f'<g fill="url(#blade)" opacity=".9">{"".join(blades)}</g>'


def build_svg() -> str:
    rng = random.Random(2007)

    clouds = "".join([
        _cloud(260, 210, 1.1, .95), _cloud(820, 120, .8, .85), _cloud(1180, 300, 1.25, .9),
        _cloud(1720, 250, .9, .8), _cloud(520, 420, .7, .7), _cloud(1580, 520, .6, .65),
        _cloud(60, 520, .6, .6),
    ])

    bubbles = "".join(
        _bubble(cx, cy, r, op) for cx, cy, r, op in [
            (140, 760, 70, .9), (260, 620, 34, .85), (90, 470, 22, .8), (380, 820, 46, .8),
            (330, 500, 14, .7), (1840, 700, 60, .85), (1720, 860, 38, .8), (1880, 480, 26, .75),
            (1640, 640, 16, .7), (980, 860, 28, .6), (700, 300, 18, .55), (1060, 560, 12, .55),
        ]
    )

    sparkles = "".join(
        f'<circle cx="{rng.uniform(0, W):.0f}" cy="{rng.uniform(40, 700):.0f}" '
        f'r="{rng.uniform(1.5, 4):.1f}" fill="#FFFFFF" opacity="{rng.uniform(.3, .8):.2f}"/>'
        for _ in range(45)
    )

    rays = "".join(
        f'<polygon points="1500,150 {x1},{H} {x2},{H}" fill="url(#ray)" opacity="{op}"/>'
        for x1, x2, op in [(-200, 120, .5), (300, 520, .4), (760, 900, .35), (1150, 1250, .3), (1900, 2100, .3)]
    )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice">
<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#0A5DAE"/>
    <stop offset=".38" stop-color="#2A8FDB"/>
    <stop offset=".66" stop-color="#7FCBF3"/>
    <stop offset=".78" stop-color="#D6F0FC"/>
  </linearGradient>
  <radialGradient id="sun" cx="1500" cy="150" r="620" gradientUnits="userSpaceOnUse">
    <stop offset="0" stop-color="#FFFFFF" stop-opacity="1"/>
    <stop offset=".12" stop-color="#FFFDE8" stop-opacity=".85"/>
    <stop offset=".45" stop-color="#FFFFFF" stop-opacity=".18"/>
    <stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="ray" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#FFFFFF" stop-opacity=".35"/>
    <stop offset=".7" stop-color="#FFFFFF" stop-opacity="0"/>
  </linearGradient>
  <radialGradient id="cloud" cx=".45" cy=".3" r=".8">
    <stop offset="0" stop-color="#FFFFFF"/>
    <stop offset=".7" stop-color="#F2FAFF"/>
    <stop offset="1" stop-color="#CFE8F7"/>
  </radialGradient>
  <filter id="soft" x="-20%" y="-40%" width="140%" height="180%"><feGaussianBlur stdDeviation="5"/></filter>
  <filter id="haze" x="-10%" y="-50%" width="120%" height="200%"><feGaussianBlur stdDeviation="14"/></filter>
  <linearGradient id="glass" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#E4F6FF"/>
    <stop offset=".5" stop-color="#9ED6F2"/>
    <stop offset="1" stop-color="#6FB6E0"/>
  </linearGradient>
  <linearGradient id="hillFar" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#B6E88A"/>
    <stop offset="1" stop-color="#6CC06A"/>
  </linearGradient>
  <linearGradient id="hill" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#B4F06E"/>
    <stop offset=".35" stop-color="#6BC84A"/>
    <stop offset="1" stop-color="#2E8A36"/>
  </linearGradient>
  <linearGradient id="hillNear" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#8EDB55"/>
    <stop offset="1" stop-color="#1F6E2E"/>
  </linearGradient>
  <linearGradient id="water" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#BFEBFF"/>
    <stop offset=".5" stop-color="#4FB8EE"/>
    <stop offset="1" stop-color="#1A7FC4"/>
  </linearGradient>
  <linearGradient id="blade" x1="0" y1="1" x2="0" y2="0">
    <stop offset="0" stop-color="#1E6B2C"/>
    <stop offset=".6" stop-color="#4DB040"/>
    <stop offset="1" stop-color="#B9F27A"/>
  </linearGradient>
  <radialGradient id="bubble" cx=".5" cy=".5" r=".5">
    <stop offset="0" stop-color="#FFFFFF" stop-opacity="0"/>
    <stop offset=".7" stop-color="#E6FAFF" stop-opacity=".08"/>
    <stop offset=".92" stop-color="#BFF2FF" stop-opacity=".35"/>
    <stop offset="1" stop-color="#FFFFFF" stop-opacity=".6"/>
  </radialGradient>
  <linearGradient id="shine" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#FFFFFF" stop-opacity=".95"/>
    <stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/>
  </linearGradient>
</defs>
<rect width="{W}" height="{H}" fill="url(#sky)"/>
<rect width="{W}" height="{H}" fill="url(#sun)"/>
{rays}
{clouds}
<rect x="-150" y="620" width="{W + 300}" height="120" fill="#EAF8FF" opacity=".55" filter="url(#haze)"/>
{_towers(rng)}
<path d="M0 760 C220 700 420 690 640 720 S1060 690 1300 715 S1720 700 1920 730 V1000 H0Z" fill="url(#hillFar)" opacity=".85"/>
<path d="M560 820 C760 790 1080 790 1300 815 C1200 850 760 855 560 820Z" fill="url(#water)"/>
<path d="M640 812 H1180 M700 824 H1120 M780 836 H1040" stroke="#FFFFFF" stroke-opacity=".55" stroke-width="2" stroke-linecap="round"/>
<path d="M0 800 C260 740 470 760 620 830 C760 900 520 980 0 980Z" fill="url(#hill)"/>
<path d="M1920 790 C1660 740 1400 770 1260 840 C1120 910 1400 990 1920 990Z" fill="url(#hill)"/>
<path d="M0 805 C260 748 460 768 600 828" stroke="#E4FFC2" stroke-opacity=".7" stroke-width="5" fill="none" filter="url(#soft)"/>
<path d="M1920 796 C1660 748 1420 776 1280 838" stroke="#E4FFC2" stroke-opacity=".6" stroke-width="5" fill="none" filter="url(#soft)"/>
<path d="M0 930 C400 870 800 880 1100 910 S1700 880 1920 900 V{H} H0Z" fill="url(#hillNear)"/>
{_grass(rng)}
{sparkles}
{bubbles}
</svg>
'''
