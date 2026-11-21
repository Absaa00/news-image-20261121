# news-image-20261121 — Sum up 21 November's world news in one image

[![make.fun](https://make.fun/badge.svg)](https://make.fun/bounty/news-image-20261121)

Entry for the make.fun bounty [news-image-20261121](https://make.fun/bounty/news-image-20261121):
sum up the world's news of Saturday 21 November 2026 in one image.

## The image

`entry.png` (1024×1024, 178,167 bytes) is a one-page newspaper front page,
"The World Today", drawn offline with PIL (`gen_image.py`):

- **Lead:** AI rout on Wall Street — S&P 500 −3.7% to 6,910, Nasdaq −5.3% into
  negative territory for the year, Dow −950 points, Nvidia −14% (SEC probe
  reports, CEO Jensen Huang's departure), Anthropic −9% a day after its record IPO.
- **Justice:** ICJ rules Myanmar's military committed state-sponsored genocide
  against the Rohingya — the first time the court has held a state responsible.
- **Weather:** Cyclone Akvan crosses the Odisha coast after ~300,000 evacuations.
- **Diplomacy:** first Trump–Xi–Putin trilateral summit ends with few results.
- **Climate:** COP31 talks in Turkey enter their final stretch.
- **Conflict:** Russia hits Kryvyi Rih (2 dead, 42 hurt); EU adopts €1bn military aid.
- **Ticker:** India 159/1 in the Wellington Test, NSE now the world's 5th-largest
  exchange, Carlsen forfeits rapid games, Nepal PM visits India, cheetah cubs at Kuno.

## The program

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png` and verifies its SHA-256. Deterministic: two runs produce
byte-identical output (sha256
`6d01a76f95fcc5d6c20bd58c0e66257bcf51cb4a0c47100dd8d71f34a6c8d025`).

```
python3 -S main.py
```
