// news-image-20261119 entry — "World News: Thursday, 19 November 2026".
//
// Node 22, standard library only. The finished 1024x1024 PNG lives beside
// this file as entry.png; the program just copies it into the output
// directory, so a run needs no network and always writes identical bytes.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

// Determinism note: the output is a byte-for-byte copy of the bundled
// entry.png — no timestamps, no randomness, no rendering at run time — so
// running the program twice produces identical files, and the file the
// judge grades is exactly the file in this repo.
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true }); // creates /output when missing; no-op when it exists
copyFileSync(
  join(dirname(fileURLToPath(import.meta.url)), 'entry.png'),
  join(outDir, 'entry.png'),
);
