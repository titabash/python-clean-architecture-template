import sys
import os
sys.path.append(f"{os.path.dirname(__file__)}/../src")
"""
Write your module
Ex. import hoge
"""
from batch import main_cmd  # noqa: E402


def test_is_mainCmd():
    assert main_cmd() == "Hello, Python Api!"
