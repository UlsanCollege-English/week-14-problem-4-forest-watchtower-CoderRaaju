class TreeNode:
    """
    Simple binary tree node: value, left, right.
    """

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_balanced(root):
    """
    Return True if the binary tree rooted at `root` is height-balanced.

    Empty tree (root is None) is considered balanced.
    """

    def check(node):
        # Returns (is_balanced, height)
        if node is None:
            return True, 0

        left_bal, left_h = check(node.left)
        if not left_bal:
            return False, 0

        right_bal, right_h = check(node.right)
        if not right_bal:
            return False, 0

        # Check height difference
        if abs(left_h - right_h) > 1:
            return False, 0

        # Balanced: height = 1 + max child height
        return True, 1 + max(left_h, right_h)

    balanced, _ = check(root)
    return balanced