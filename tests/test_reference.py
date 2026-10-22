"""A reference-test pattern, using explicitly hand-calculated example data."""

import json
from pathlib import Path

import pytest

from pyrverse_port import center


def test_center_against_demonstration_fixture() -> None:
    path = Path(__file__).parent / "reference" / "center.json"
    fixture = json.loads(path.read_text(encoding="utf-8"))
    actual = center(fixture["input"])
    assert len(actual) == len(fixture["expected"])
    assert actual == pytest.approx(
        fixture["expected"], abs=fixture["atol"], rel=fixture["rtol"]
    )
