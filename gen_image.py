#!/usr/bin/env python3
"""Draw the 21 Nov 2026 world-news front page, 1024x1024 PNG, offline, deterministic."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (18, 18, 18)
RED = (178, 34, 34)
DARKRED = (120, 20, 20)
GREY = (90, 90, 90)
RULE = (60, 60, 60)
BLUE = (20, 60, 120)
GREEN = (20, 110, 50)

FD = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = FD + "DejaVuSerif-Bold.ttf"
SERIF = FD + "DejaVuSerif.ttf"
SANS_B = FD + "DejaVuSans-Bold.ttf"
SANS = FD + "DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns list of lines that fit `width` px."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, width, text, fnt, fill=INK, leading=None):
    """Draw wrapped paragraph; returns y after last line."""
    if leading is None:
        leading = fnt.size + 5
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def headline(draw, x, y, width, text, fnt, fill=INK, leading=None):
    return para(draw, x, y, width, text, fnt, fill=fill, leading=leading)


def hrule(draw, x, y, width, fill=RULE, w=2):
    draw.line([(x, y), (x + width, y)], fill=fill, width=w)


def kicker(draw, x, y, text, color=RED):
    f = font(SANS_B, 17)
    draw.text((x, y), text.upper(), font=f, fill=color)
    return y + 24


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
M = 36                      # margin
CW = W - 2 * M              # content width

# ---------- masthead ----------
y = 16
d.text((M, y), "THE WORLD TODAY", font=font(SERIF_B, 62), fill=INK)
y += 74
hrule(d, M, y, CW, fill=INK, w=4)
y += 8
d.text((M, y), "SATURDAY 21 NOVEMBER 2026", font=font(SANS_B, 19), fill=INK)
_dt = "NEW YORK  •  LONDON  •  DELHI"
d.text((W - M - d.textlength(_dt, font=font(SANS_B, 19)), y), _dt, font=font(SANS_B, 19), fill=INK)
y += 26
hrule(d, M, y, CW, fill=INK, w=4)
y += 10

# ---------- lead story: AI rout ----------
y = kicker(d, M, y, "Markets  •  Lead story")
y = headline(d, M, y, CW, "AI ROUT ON WALL STREET", font(SERIF_B, 48), leading=52)
y += 6
y = headline(d, M, y, CW, "S&P 500 sinks 3.7% into correction as Nvidia plunges 14%",
             font(SERIF, 25), leading=30)
y += 8
# body + chart side by side
body_w = 560
body = ("A bruising sell-off in artificial-intelligence stocks dragged the S&P 500 "
        "down 3.7% to 6,910 on Friday, its seventh straight loss, while the Nasdaq "
        "tumbled 5.3% and wiped out its gains for the year. Nvidia fell 14% on "
        "reports of an SEC accounting probe and the departure of chief executive "
        "Jensen Huang; Anthropic slid 9% a day after its record IPO. The Dow "
        "dropped 950 points; all three indexes are now in correction territory.")
by = y
y = para(d, M, y, body_w, body, font(SERIF, 18), leading=24)
d.text((M, y + 4), "—  NEW YORK, 20 NOV", font=font(SANS_B, 15), fill=GREY)

# mini bar chart, right of body
cx, cy = M + 600, by
d.text((cx, cy), "FRIDAY'S FALLS", font=font(SANS_B, 16), fill=GREY)
cy += 26
bars = [("S&P 500", "-3.7%", 3.7), ("Nasdaq", "-5.3%", 5.3),
        ("Dow", "-1.9%", 1.9), ("Nvidia", "-14.0%", 14.0)]
for name, pct, val in bars:
    d.text((cx, cy), name, font=font(SANS_B, 16), fill=INK)
    bx = cx + 92
    bw = int(val / 14.0 * 190)
    d.rectangle([bx, cy + 2, bx + bw, cy + 18], fill=RED)
    d.text((bx + bw + 8, cy), pct, font=font(SANS_B, 16), fill=DARKRED)
    cy += 30
d.text((cx, cy + 2), "Nvidia is down by a third in two weeks.",
       font=font(SANS, 15), fill=GREY)
y = max(y + 24, cy + 30)
hrule(d, M, y, CW, fill=RULE, w=2)
y += 14

# ---------- row: ICJ (left) + Cyclone Akvan (right) ----------
col_w = (CW - 24) // 2
x2 = M + col_w + 24
y0 = y
y = kicker(d, M, y, "Justice  •  The Hague")
y = headline(d, M, y, col_w, "WORLD COURT: MYANMAR COMMITTED GENOCIDE",
             font(SERIF_B, 28), leading=32)
y += 4
y = para(d, M, y, col_w,
         "The International Court of Justice ruled that Myanmar's military carried "
         "out state-sponsored genocide against the Rohingya — mass executions, "
         "widespread sexual violence and the burning of hundreds of villages in "
         "2016–18. It is the first time the court has held a state responsible "
         "for genocide. Myanmar called the ruling 'unfair'.",
         font(SERIF, 17), leading=22)

y2 = kicker(d, x2, y0, "Weather  •  India")
y2 = headline(d, x2, y2, col_w, "CYCLONE AKVAN SLAMS ODISHA COAST",
              font(SERIF_B, 28), leading=32)
y2 += 4
y2 = para(d, x2, y2, col_w,
          "Cyclone Akvan crossed the Odisha and Andhra Pradesh coasts near "
          "Gopalpur with strong winds and heavy rain, after some 300,000 people "
          "were moved to safety. The storm is weakening as it moves inland.",
          font(SERIF, 17), leading=22)
y = max(y, y2) + 8
hrule(d, M, y, CW, fill=RULE, w=2)
y += 14

# ---------- row: three small panels ----------
pw = (CW - 48) // 3
panels = [
    ("Diplomacy  •  Shenzhen", BLUE,
     "SUMMIT ENDS WITH FEW RESULTS",
     "The first Trump–Xi–Putin trilateral summit closed with little concrete "
     "to show on nuclear arms, energy or the wars."),
    ("Climate  •  Turkey", GREEN,
     "COP31 TALKS ENTER FINAL STRETCH",
     "Negotiators in Turkey pushed into the final stage of the UN climate "
     "summit, with fossil fuels and finance still the sticking points."),
    ("Conflict  •  Ukraine", DARKRED,
     "RUSSIA HITS KRYVYI RIH; EU SENDS €1BN AID",
     "Two killed and 42 hurt in a strike on Kryvyi Rih. The EU adopted €1 "
     "billion in military aid; Britain pledged 1,000 more drones."),
]
y0 = y
ys = []
for i, (kick, col, head, body) in enumerate(panels):
    px = M + i * (pw + 24)
    yy = kicker(d, px, y0, kick, color=col)
    yy = headline(d, px, yy, pw, head, font(SERIF_B, 20), leading=24)
    yy += 4
    yy = para(d, px, yy, pw, body, font(SERIF, 15), leading=20)
    ys.append(yy)
y = max(ys) + 8
hrule(d, M, y, CW, fill=RULE, w=2)
y += 8

# ---------- ticker strip ----------
tick = ("CRICKET  India 159/1 in Wellington Test  •  MARKETS  NSE now the world's "
        "5th-largest exchange; Sensex +898  •  CHESS  Carlsen forfeits rapid games  •  "
        "NEPAL  PM Shah visits India 22–23 Nov  •  CHEETAH  four cubs born at Kuno")
strip_h = 62
d.rectangle([M, y, W - M, y + strip_h], fill=INK)
d.text((M + 12, y + 8), "THE DAY IN BRIEF", font=font(SANS_B, 15), fill=(255, 210, 90))
para(d, M + 12, y + 30, CW - 24, tick, font(SANS, 15), fill=(240, 240, 240), leading=20)
y += strip_h + 8
hrule(d, M, y, CW, fill=INK, w=3)
y += 8
d.text((M, y), "THE WORLD TODAY  •  SATURDAY 21 NOVEMBER 2026  •  ALL THE NEWS THAT FITS ON ONE PAGE",
       font=font(SANS_B, 13), fill=GREY)

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
