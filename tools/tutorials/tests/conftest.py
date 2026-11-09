"""Find the spaCR checkout that the tutorial tooling tests read from.

The lesson index, workflow, media-budget and caption-translation tools stayed
in spaCR (the docs build and the app read them), so several tests here import
them from a spaCR checkout: the one named by ``SPACR_CHECKOUT``, or else the
one whose ``spacr`` package is importable. Its ``tools`` folder goes at the END
of ``sys.path``, so a tool of the same name in this repository still wins, and
``SPACR_CHECKOUT`` is set for tests that load a spaCR tool by path (and
``SPACR_REPO``, unless already set, for the publishing tools).
"""
import os
import sys
from pathlib import Path


def _spacr_checkout():
    """The spaCR checkout to read, or None when there is none."""
    named = os.environ.get("SPACR_CHECKOUT")
    if named:
        return Path(named).expanduser().resolve()
    try:
        import spacr
    except ImportError:
        return None
    root = Path(spacr.__file__).resolve().parents[1]
    return root if (root / "tools").is_dir() else None


CHECKOUT = _spacr_checkout()
if CHECKOUT is not None:
    os.environ["SPACR_CHECKOUT"] = str(CHECKOUT)
    # authoring/tools/publish_tutorials.py stops at import without a spaCR checkout to publish from
    os.environ.setdefault("SPACR_REPO", str(CHECKOUT))
    if str(CHECKOUT / "tools") not in sys.path:
        sys.path.append(str(CHECKOUT / "tools"))
