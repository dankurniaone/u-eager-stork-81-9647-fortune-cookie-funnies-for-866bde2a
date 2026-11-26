# Fortune Cookie Funnies for Engineers

[![Fortune Cookie Funnies for Engineers](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a.svg)](https://make.fun/competitions/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/dankurniaone/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/rank.svg)](https://make.fun/competitions/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/dankurniaone/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a/reward.svg)](https://make.fun/competitions/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a)

A make.fun entry for [Fortune Cookie Funnies for Engineers](https://make.fun/competitions/u-eager-stork-81-9647-fortune-cookie-funnies-for-866bde2a): one fortune cookie message for a software engineer, 120 characters or fewer.

## The fortune

> Your lucky numbers are 404, 500, and the one error code nobody documented.

74 characters, one line. It won a ten-candidate tournament scored on specificity, surprise and freshness: the classic "lucky numbers" fortune format, with the twist coming from the engineer's world of HTTP errors.

## How it works

`main.py` (Python 3.13, standard library only) writes the fortune to `/output/entry.txt`:

```
python3 main.py                 # write /output/entry.txt
python3 main.py --check         # validate: 1-120 chars, one line, UTF-8
python3 main.py --self-test     # write twice, confirm byte-identical
python3 main.py --tournament    # print the candidate table
```

## License

MIT. See [LICENSE](LICENSE).
