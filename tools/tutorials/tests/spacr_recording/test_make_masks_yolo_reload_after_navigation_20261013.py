"""The lesson 14 YOLO tour driver waits for the field it navigated to.

The capture host stopped the YOLO tour with "Navigation did not reload the
exact saved annotations". The host clicks with real input, which can return
before the click is handled, and the driver read the field before Prev had
landed. The editor side (Make Masks reloads the exact saved boxes) is pinned
in spaCR by tests/qt/test_make_masks_yolo_reload_after_navigation_20261013.py;
this half, which reads the recording driver, moved here with the driver.
"""
from __future__ import annotations

import ast
from pathlib import Path

DRIVER = Path(__file__).resolve().parents[4] / "tools" / "tutorials" / "capture_make_masks.py"


def test_the_driver_waits_for_the_field_a_navigation_asked_for():
    """``ready`` takes the expected field, and both navigations pass one."""
    tree = ast.parse(DRIVER.read_text(encoding="utf-8"))
    tour = next(node for node in tree.body
                if isinstance(node, ast.FunctionDef) and node.name == "record_yolo_boxes")
    ready = next(node for node in ast.walk(tour)
                 if isinstance(node, ast.FunctionDef) and node.name == "ready")
    assert [arg.arg for arg in ready.args.args] == ["expected"]
    calls = [node for node in ast.walk(tour)
             if isinstance(node, ast.Call) and getattr(node.func, "id", None) == "ready"]
    assert sum(1 for call in calls if call.args) == 2
