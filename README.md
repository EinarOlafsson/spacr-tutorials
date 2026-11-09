# spaCR tutorials

Scripts, lesson sources and the lesson library player for the spaCR tutorial
course at <https://einarolafsson.github.io/spacr/tutorials/>.

## Where things live

| What | Where |
| --- | --- |
| Lesson scripts, capture and publishing tools, lesson sources, production records, tooling tests | this repository, `tools/tutorials/` |
| Player code, lesson and caption catalogs | this repository, `docs/source/_extra/tutorials/` |
| Posters, narration, example downloads, release-candidate media | Hugging Face dataset [`einarolafsson/spacr-tutorials`](https://huggingface.co/datasets/einarolafsson/spacr-tutorials), under `tree/<path in spaCR>` |
| The pin spaCR builds against | `docs/media_revision.json` in [spaCR](https://github.com/EinarOlafsson/spacr), groups `tutorials` and `tutorial_archive`; a copy is in `media/tutorial_media_pin.json` |

The paths here are the paths these files have in the spaCR repository, so a
file can be compared with, or copied back to, its place there.

## Building media

The tutorial tools write new media to the staging folder named by
`SPACR_TUTORIALS_STAGING` (default `~/spacr-tutorials-staging`), at
`hf/tree/<path in spaCR>`. Publishing uploads the changed files and moves the
pin, from a spaCR checkout:

```
python tools/fetch_docs_media.py publish --group tutorials --source "$SPACR_TUTORIALS_STAGING/hf/tree"
python tools/fetch_docs_media.py publish --group tutorial_archive --source "$SPACR_TUTORIALS_STAGING/hf/tree"
```

A docs build fetches the pinned posters and example downloads with
`python tools/fetch_docs_media.py fetch --group tutorials`.

## Tests

The tooling tests are in `tools/tutorials/tests/`. The ones in
`tools/tutorials/tests/spacr_recording/` check the recording tools against
real spaCR widgets and need a spaCR checkout for its `spacr` package and test
fixtures:

```
SPACR_CHECKOUT=/path/to/spacr QT_QPA_PLATFORM=offscreen python -m pytest tools/tutorials/tests/spacr_recording
```

## Licence

The spaCR software is under the licence in the spaCR repository. The generated
tutorial media is covered by `docs/source/_extra/tutorials/TUTORIAL_MEDIA_NOTICE.md`.
