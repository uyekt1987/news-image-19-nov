#!/usr/bin/env python3
"""Draw the 19 Nov 2026 world-news infographic (1024x1024, <1 MiB).

Same newspaper layout as the 18 Nov entry: WORLD NEWS masthead, red date
line, 2x3 grid of story panels with vector-style illustrations, footer.
Stories verified against real 19 Nov 2026 news (Reuters, Le Monde, AJU,
horizonapp, oneturn.news, openchronicle).
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (246, 241, 231)
NAVY = (27, 42, 74)
RED = (185, 28, 28)
GRAY = (85, 85, 85)
PANEL_FILL = (255, 255, 255)
PANEL_BORDER = (168, 162, 154)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
F_BOLD = lambda s: ImageFont.truetype(FONT_DIR + "DejaVuSans-Bold.ttf", s)
F_REG = lambda s: ImageFont.truetype(FONT_DIR + "DejaVuSans.ttf", s)
F_SERIF_BOLD = lambda s: ImageFont.truetype(FONT_DIR + "DejaVuSerif-Bold.ttf", s)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)


def text_cx(cx, y, s, font, fill):
    w = d.textlength(s, font=font)
    d.text((cx - w / 2, y), s, font=font, fill=fill)


def wrap(s, font, max_w):
    words, lines, cur = s.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=font) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def star(cx, cy, r_out, r_in, n=5, rot=-90):
    pts = []
    for i in range(2 * n):
        r = r_out if i % 2 == 0 else r_in
        a = math.radians(rot + i * 180 / n)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def flag_us(x, y, w=110, h=66):
    stripe = h / 13
    for i in range(13):
        if i % 2 == 0:
            d.rectangle([x, y + i * stripe, x + w, y + (i + 1) * stripe], fill=(178, 34, 52))
    canton_w, canton_h = w * 0.4, stripe * 7
    d.rectangle([x, y, x + canton_w, y + canton_h], fill=(30, 58, 95))
    for r in range(4):
        for c in range(5):
            sx = x + 6 + c * 8.5
            sy = y + 5 + r * 8
            d.ellipse([sx, sy, sx + 3, sy + 3], fill=(255, 255, 255))


def flag_cn(x, y, w=110, h=66):
    d.rectangle([x, y, x + w, y + h], fill=(222, 41, 16))
    d.polygon(star(x + 18, y + 18, 13, 5.5), fill=(255, 222, 0))
    for sx, sy in [(x + 42, y + 10), (x + 50, y + 18), (x + 50, y + 30), (x + 42, y + 38)]:
        d.polygon(star(sx, sy, 5, 2.2), fill=(255, 222, 0))


def flag_ru(x, y, w=110, h=66):
    d.rectangle([x, y, x + w, y + h / 3], fill=(255, 255, 255))
    d.rectangle([x, y + h / 3, x + w, y + 2 * h / 3], fill=(0, 57, 166))
    d.rectangle([x, y + 2 * h / 3, x + w, y + h], fill=(213, 0, 50))


def burst(cx, cy, r_out, r_in, n=12, fill=(255, 140, 0)):
    pts = []
    for i in range(2 * n):
        r = r_out if i % 2 == 0 else r_in
        a = math.radians(i * 180 / n)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    d.polygon(pts, fill=fill)


# ---- masthead ----
text_cx(W / 2, 14, "WORLD NEWS", F_BOLD(116), NAVY)
d.rectangle([24, 142, W - 24, 147], fill=RED)
text_cx(W / 2, 158, "Thursday, 19 November 2026", F_SERIF_BOLD(46), RED)
d.rectangle([24, 216, W - 24, 221], fill=RED)

# ---- panels ----
PX, PY, PW, PH, GX, GY = 24, 232, 480, 240, 16, 12

STORIES = [
    dict(kicker="SUMMIT", color=(180, 83, 9), ill_bg=(239, 232, 214),
         head="Trump, Xi & Putin hold first trilateral summit",
         sub="Nuclear arms on the table \u2022 Shenzhen, China"),
    dict(kicker="UKRAINE", color=(29, 78, 216), ill_bg=(220, 235, 245),
         head="Ukraine hits Kerch Bridge for a third time this week",
         sub="Traffic suspended \u2022 EU offers \u20ac45bn loan"),
    dict(kicker="THE GULF", color=(185, 28, 28), ill_bg=(220, 235, 245),
         head="Iran strikes Gulf states again \u2014 Hormuz oil in peril",
         sub="IEA: worst threat to energy security yet"),
    dict(kicker="JUSTICE", color=(15, 118, 110), ill_bg=(227, 236, 247),
         head="World court rules on Rohingya genocide case",
         sub="Gambia v. Myanmar \u2022 730,000 fled in 2017"),
    dict(kicker="BANGLADESH", color=(159, 18, 57), ill_bg=(253, 232, 232),
         head="Yunus's home torched as unrest hits 28 districts",
         sub="Political violence spreads across Bangladesh"),
    dict(kicker="TECH", color=(22, 101, 52), ill_bg=(232, 240, 248),
         head="Anthropic's $79.4bn IPO sets a record on debut",
         sub="AI firm's debut is the biggest ever"),
]


def draw_summit(ix, iy):
    # three flags on poles + gold handshake arc
    for i, fn in enumerate((flag_us, flag_cn, flag_ru)):
        fx = ix + 62 + i * 128
        d.line([fx, iy + 10, fx, iy + 98], fill=(60, 50, 40), width=3)
        fn(fx, iy + 14)
    d.arc([ix + 150, iy + 74, ix + 326, iy + 116], 200, 340, fill=(180, 83, 9), width=5)


def draw_ukraine(ix, iy):
    d.rectangle([ix, iy + 82, ix + 476, iy + 113], fill=(74, 127, 181))
    d.line([ix + 20, iy + 66, ix + 456, iy + 66], fill=(40, 40, 40), width=6)
    d.arc([ix + 40, iy + 22, ix + 190, iy + 92], 180, 360, fill=(40, 40, 40), width=5)
    # broken second arch: two stubs + gap
    d.arc([ix + 250, iy + 22, ix + 400, iy + 92], 180, 270, fill=(40, 40, 40), width=5)
    d.arc([ix + 250, iy + 22, ix + 400, iy + 92], 315, 360, fill=(40, 40, 40), width=5)
    for cx, cy, r in [(330, 30, 13), (352, 20, 10), (308, 18, 9)]:
        d.ellipse([ix + cx - r, iy + cy - r, ix + cx + r, iy + cy + r],
                  fill=(120, 120, 120))
    for px in (60, 140, 215, 290, 365, 440):
        d.line([ix + px, iy + 66, ix + px, iy + 82], fill=(40, 40, 40), width=4)


def draw_gulf(ix, iy):
    d.rectangle([ix, iy + 82, ix + 476, iy + 113], fill=(74, 127, 181))
    d.polygon([(ix + 120, iy + 82), (ix + 180, iy + 52), (ix + 250, iy + 52),
               (ix + 300, iy + 82)], fill=(96, 140, 70))
    burst(ix + 215, iy + 46, 30, 14, fill=(255, 140, 0))
    burst(ix + 215, iy + 46, 16, 8, fill=(255, 210, 0))
    # missile streaking up-right
    d.line([ix + 300, iy + 58, ix + 428, iy + 14], fill=(40, 40, 40), width=4)
    d.polygon([(ix + 428, iy + 14), (ix + 442, iy + 6), (ix + 434, iy + 26)],
              fill=(40, 40, 40))


def draw_justice(ix, iy):
    # courthouse: pediment (apex up) + 3 columns + steps
    d.polygon([(ix + 130, iy + 52), (ix + 346, iy + 52), (ix + 238, iy + 16)],
              fill=(30, 58, 95))
    for cx in (168, 238, 308):
        d.rectangle([ix + cx - 13, iy + 56, ix + cx + 13, iy + 96], fill=(30, 58, 95))
    d.rectangle([ix + 130, iy + 96, ix + 346, iy + 104], fill=(30, 58, 95))
    d.rectangle([ix + 118, iy + 104, ix + 358, iy + 110], fill=(90, 110, 140))


def draw_bangladesh(ix, iy):
    # house with flames
    d.rectangle([ix + 168, iy + 62, ix + 308, iy + 104], fill=(90, 70, 60))
    d.polygon([(ix + 152, iy + 64), (ix + 238, iy + 26), (ix + 324, iy + 64)],
              fill=(120, 60, 50))
    d.rectangle([ix + 222, iy + 78, ix + 254, iy + 104], fill=(246, 241, 231))
    # flames just above the roof
    for (cx, cy, s) in [(200, 20, 16), (238, 13, 18), (276, 20, 16)]:
        d.polygon([(ix + cx, iy + cy - s), (ix + cx + s * 0.55, iy + cy + s * 0.4),
                   (ix + cx + s * 0.2, iy + cy + s * 0.7),
                   (ix + cx - s * 0.2, iy + cy + s * 0.7),
                   (ix + cx - s * 0.55, iy + cy + s * 0.4)],
                  fill=(249, 115, 22))
    for (cx, cy, s) in [(200, 24, 9), (238, 18, 10), (276, 24, 9)]:
        d.polygon([(ix + cx, iy + cy - s), (ix + cx + s * 0.55, iy + cy + s * 0.4),
                   (ix + cx, iy + cy + s * 0.7),
                   (ix + cx - s * 0.55, iy + cy + s * 0.4)], fill=(220, 38, 38))


def draw_tech(ix, iy):
    d.text((ix + 28, iy + 18), "$79.4B", font=F_BOLD(66), fill=NAVY)
    d.text((ix + 30, iy + 82), "RECORD IPO", font=F_BOLD(26), fill=(22, 101, 52))
    pts = [(ix + 320, iy + 92), (ix + 350, iy + 70), (ix + 380, iy + 78),
           (ix + 410, iy + 44), (ix + 444, iy + 20)]
    d.line(pts, fill=(22, 101, 52), width=6, joint="curve")
    d.polygon([(ix + 444, iy + 20), (ix + 424, iy + 18), (ix + 442, iy + 38)],
              fill=(22, 101, 52))


ILL = [draw_summit, draw_ukraine, draw_gulf, draw_justice, draw_bangladesh, draw_tech]

for i, st in enumerate(STORIES):
    col, row = i % 2, i // 2
    x0 = PX + col * (PW + GX)
    y0 = PY + row * (PH + GY)
    # panel fill + top rule + border
    d.rectangle([x0, y0, x0 + PW, y0 + PH], fill=PANEL_FILL)
    d.rectangle([x0, y0, x0 + PW, y0 + 5], fill=st["color"])
    d.rectangle([x0, y0, x0 + PW, y0 + PH], outline=PANEL_BORDER, width=2)
    # illustration
    ix, iy = x0 + 2, y0 + 5
    d.rectangle([ix, iy, ix + 476, iy + 113], fill=st["ill_bg"])
    ILL[i](ix, iy)
    # kicker
    d.text((x0 + 14, y0 + 126), st["kicker"], font=F_BOLD(21), fill=st["color"])
    # headline (max 2 lines)
    font = F_BOLD(27)
    lines = wrap(st["head"], font, PW - 28)
    assert len(lines) <= 2, (st["kicker"], lines)
    for j, ln in enumerate(lines):
        d.text((x0 + 14, y0 + 152 + j * 32), ln, font=font, fill=(20, 20, 20))
    # sub-line (shrink to fit)
    sfont = F_REG(19)
    while d.textlength(st["sub"], font=sfont) > PW - 28 and sfont.size > 14:
        sfont = F_REG(sfont.size - 1)
    d.text((x0 + 14, y0 + 216), st["sub"], font=sfont, fill=GRAY)

# ---- footer ----
d.rectangle([24, 972, W - 24, 973], fill=(120, 120, 120))
text_cx(W / 2, 984, "Six stories that shaped Thursday, 19 November 2026",
        F_BOLD(25), NAVY)

img.save("/home/hatch/workspace/makefun/news-image-19nov/entry.png", optimize=True)
print("saved, bytes:", len(open("/home/hatch/workspace/makefun/news-image-19nov/entry.png", "rb").read()))
