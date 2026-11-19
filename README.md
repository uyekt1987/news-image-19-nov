# World News — Thursday, 19 November 2026

[![news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/uyekt1987/news-image-19-nov/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard)
[![reward](https://make.fun/badge/news-image-20261119/uyekt1987/news-image-19-nov/reward.svg)](https://make.fun/bounty/news-image-20261119)

A one-page newspaper-style infographic summarising the world news of
**Thursday, 19 November 2026** — six stories that shaped the day, drawn as
clean vector-style panels (no AI-generated imagery, so every word stays sharp
and legible):

1. **Summit** — Trump, Xi Jinping and Vladimir Putin hold their first
   trilateral summit in Shenzhen, on the sidelines of APEC; nuclear arms
   control is on the table.
2. **Ukraine** — Ukraine hits the Kerch Bridge to Crimea for a third time
   in a week; traffic is suspended and the EU offers a €45bn loan.
3. **The Gulf** — Iran strikes Gulf states again after the U.S. hit Qeshm
   Island; the IEA warns the Hormuz crisis is the worst threat to energy
   security yet.
4. **Justice** — The International Court of Justice rules on the Rohingya
   genocide case (Gambia v. Myanmar); 730,000 fled in 2017.
5. **Bangladesh** — Muhammad Yunus's ancestral home is torched as political
   unrest hits 28 districts.
6. **Tech** — Anthropic's $79.4bn IPO sets a record on its stock-market debut.

## How it works

`main.ts` (Node 22, standard library only) copies the finished
`entry.png` (1024×1024, under 1 MiB) into the output directory
(`MAKEFUN_OUTPUT_DIR`, default `/output`). No network access, no rendering
at run time — two runs produce byte-identical output.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## License

MIT — see [LICENSE](LICENSE).
