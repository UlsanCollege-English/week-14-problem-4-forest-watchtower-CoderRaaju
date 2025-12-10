import pathlib
import sys

import pytest

THIS_FILE = pathlib.Path(__file__).resolve()
HW_DIR = THIS_FILE.parents[1]
if str(HW_DIR) not in sys.path:
    sys.path.append(str(HW_DIR))

from main import TreeNode, is_balanced  # noqa: E402


def test_empty_tree_is_balanced():
    assert is_balanced(None) is True


def test_single_node():
    root = TreeNode(1)
    assert is_balanced(root) is True


def test_perfect_tree():
    #      1
    #     / \
    #    2   3
    #   / \ / \
    #  4  5 6  7
    root = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, TreeNode(6), TreeNode(7)),
    )
    assert is_balanced(root) is True


def test_left_heavy_unbalanced():
    # 1
    # /
    # 2
    # /
    # 3
    root = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert is_balanced(root) is False


def test_right_heavy_unbalanced():
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    assert is_balanced(root) is False


def test_almost_balanced():
    #      1
    #     / \
    #    2   3
    #   /
    #  4
    root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    assert is_balanced(root) is True


def test_complex_balanced_and_unbalanced_subtrees():
    # Left subtree balanced, right subtree not
    left = TreeNode(2, TreeNode(4), TreeNode(5))
    right = TreeNode(3, None, TreeNode(6, None, TreeNode(7, None, TreeNode(8))))
    root = TreeNode(1, left, right)
    assert is_balanced(root) is False