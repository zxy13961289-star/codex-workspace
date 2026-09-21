# codex-workspace

Starter repository created with Codex and connected to GitHub.

This repository uses HTTPS with the GitHub CLI credential helper for authentication.

## wordstats

A small, dependency-free Python package that counts lines, words, and characters.

Run it against a file:

```sh
python -m wordstats README.md
```

Or pipe text through standard input:

```sh
printf "hello world\n" | python -m wordstats
```

Run the tests:

```sh
python -m unittest discover
```
