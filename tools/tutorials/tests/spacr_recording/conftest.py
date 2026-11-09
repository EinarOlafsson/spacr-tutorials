"""Shared setup for the recording tests that moved here from spaCR (item 756).

These tests check the tutorial recording tools in this repository against real
spaCR widgets, so they need a spaCR checkout: its ``spacr`` package and its
``tests`` fixtures (``qtbot`` setup, ``qt_theme_applied``, the isolated
preferences). Point ``SPACR_CHECKOUT`` at one, or put it on ``PYTHONPATH``::

    SPACR_CHECKOUT=~/spacr python -m pytest tools/tutorials/tests/spacr_recording

The fixtures are imported here, not through ``pytest_plugins``, so they apply
only to this folder and the rest of the tutorial tests are unchanged.
"""
import os
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[4]
CHECKOUT = os.environ.get("SPACR_CHECKOUT")
for path in filter(None, (CHECKOUT, str(REPO))):
    if path not in sys.path:
        sys.path.insert(0, path)

try:
    from tests.conftest import *  # noqa: F401,F403
    from tests.qt.conftest import *  # noqa: F401,F403
except ModuleNotFoundError as error:
    raise pytest.UsageError(
        "These tests need a spaCR checkout for its test fixtures: set SPACR_CHECKOUT "
        f"to it or put it on PYTHONPATH ({error})") from error
# The star import also copies spaCR's suite-wide plugin list, which pytest refuses in a folder conftest
# when the whole tutorial suite runs; these tests need its fixtures, not those plugins.
globals().pop("pytest_plugins", None)
