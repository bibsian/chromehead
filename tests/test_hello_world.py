import pytest

from handler import handle 

def test_driver():
    r = handle(event={"headless": False}, context=None)
    assert r["statusCode"] == 200
