import sys
import json
import subprocess
import os
from pathlib import Path
from typing import *

PathLike = Union[str, Path]
script_dir = Path(__file__).parent
solutions_dir = str(os.path.join(script_dir, "solutions"))
data_dir = str(os.path.join(script_dir, "data"))
python = 'python'


def json_lines(path: PathLike) -> List[object]:
    with open(path) as f:
        return [json.loads(line) for line in f]


def run_to_json_lines(args: List[str]) -> List[object]:
    proc = subprocess.run(args, capture_output=True, text=True, check=True)
    return [json.loads(line) for line in proc.stdout.splitlines()]


def test_inverted_index():
    def conv(objs: List[object]):
        return {
            term: set(doc_ids)
            for term, doc_ids in objs
        }

    expected = conv(json_lines(
        str(os.path.join(solutions_dir, "inverted_index.json"))))
    actual = conv(run_to_json_lines(
        [python, str(os.path.join(script_dir, 'inverted_index.py')), str(os.path.join(data_dir, 'books.json'))]))

    assert expected == actual


def test_join():
    expected = json_lines(str(os.path.join(solutions_dir, 'join.json')))
    actual = run_to_json_lines(
        [python, str(os.path.join(script_dir, 'join.py')), str(os.path.join(data_dir, 'records.json'))])

    assert len(expected) == len(actual)

    expected_set = set(map(tuple, expected))
    actual_set = set(map(tuple, actual))

    assert len(expected_set) == len(expected)
    assert len(actual_set) == len(actual)
    assert expected_set == actual_set


def test_friend_count():
    def conv(items: List[object]):
        return {
            person: friend_count
            for person, friend_count in items
        }

    expected = conv(json_lines(
        str(os.path.join(solutions_dir, 'friend_count.json'))))
    actual = conv(run_to_json_lines(
        [python, str(os.path.join(script_dir, 'friend_count.py')), str(os.path.join(data_dir, 'friends.json'))]))

    assert expected == actual


def test_asymmetric_friendships():
    def conv(items: List[object]):
        return {(a, b) for a, b in items}

    expected = conv(json_lines(
        str(os.path.join(solutions_dir, 'asymmetric_friendships.json'))))
    actual = conv(run_to_json_lines(
        [python, str(os.path.join(script_dir, 'assymmentric_friendships.py')), str(os.path.join(data_dir, 'friends.json'))]))

    assert expected == actual


def test_multiply():
    expected = set(map(tuple, json_lines(
        str(os.path.join(solutions_dir, 'multiply.json')))))
    actual = set(map(tuple, run_to_json_lines(
        [python, str(os.path.join(script_dir, 'multiply.py')), str(os.path.join(data_dir, 'matrix.json'))])))

    assert expected == actual
