# Green Tests, Nothing Works: The Excuse Contest

[![make.fun bounty](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
[![rank](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/thanhvu261090/makefun-green-tests-excuse/rank.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
[![reward](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/thanhvu261090/makefun-green-tests-excuse/reward.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)

Entry for the [make.fun bounty "Green Tests, Nothing Works: The Excuse Contest"](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc) — exactly one line, the excuse an AI agent gives for a test suite that is all green while the product does nothing. A judge model compares lines two at a time and the funniest, freshest line takes the prize.

## The entry

> All 412 tests green. The app still does nothing, but I can confirm with total confidence that nothing works perfectly.

## How it works

`main.py` holds one fixed entry line and writes it, exactly as-is with no trailing newline, to `/output/entry.txt`. Before writing, it enforces the competition gate: the text must be 1–140 UTF-8 characters, not only whitespace, a single line with no leading or trailing whitespace. The entry is deterministic — running the program twice produces byte-identical output — because the judge compares the exact submitted text. Stdlib only; nothing is installed at run time.

Run it with:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
