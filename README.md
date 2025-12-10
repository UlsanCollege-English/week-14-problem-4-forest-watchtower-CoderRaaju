[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/2WRIEoU5)
# HW04 — Forest Watchtower (Balanced Tree Check)

## Story

A national park uses a **binary tree** to model watchtowers:

- Each node is a watchtower.
- Left/right children are watchtowers deeper in the forest.

For safety, the park wants a **balanced** network of watchtowers: no tower should have one side of the forest much "deeper" than the other.

Your job: given the root of a binary tree, determine whether the tree is **height-balanced**.

---

## Technical Description

In `main.py`, implement:

```python
class TreeNode
is_balanced(root) -> bool
```

### TreeNode Structure

Use this constructor:

```python
TreeNode(value, left=None, right=None)
```

Attributes:

- `value`: any data
- `left`: `TreeNode` or `None`
- `right`: `TreeNode` or `None`

### Definition of “Balanced”

A binary tree is **height-balanced** if, for every node:

- `abs(height(left_subtree) - height(right_subtree)) <= 1`

An empty tree (`root is None`) counts as **balanced**.

### Constraints

- Time complexity: **O(N)** where N is the number of nodes
  - You should not recompute heights from scratch for each node
- Space complexity: **O(H)** where H is the height of the tree (due to recursion)

---

## 8 Steps of Coding (minimal prompts)

From now on, you are responsible for driving the steps yourself:

- Step 1–2: Make sure you understand "height" and "balanced" and restate the task
- Step 3–4: Identify inputs/outputs and plan a helper strategy (you will likely need a recursion that returns both "height" and "balanced?")
- Step 5–6: Write pseudocode, then implement it
- Step 7–8: Debug with small trees and consider complexity

You should still **explicitly do all 8 steps**, but you do **not** have detailed prompts.

---

## Hints

1. Recursive helpers often return more than one piece of information, e.g. `(is_balanced, height)`
2. You can use a special value (like `-1`) to signal "already unbalanced, stop further work"
3. Remember to treat `None` as height 0 and balanced `True`

---

## How to Run Tests Locally

From the project root:

```bash
python -m pytest -q
```

Pytest will discover `hw04/tests/test_hw04.py`.

---
## FAQ

**Q1: What is "height" of a tree?**

Here we use: height of an empty tree is 0; height of a leaf node is 1.

**Q2: Do I have to use recursion?**

Recursion is the natural fit, but an iterative solution is also fine as long as it meets the complexity.

**Q3: Why is recomputing heights slowly bad?**

A naive solution that recomputes heights for every node can become O(N²) for skewed trees.

**Q4: What if the tree is empty?**

Return `True`. An empty forest is trivially balanced.

**Q5: What if only one side is deep?**

If the difference in heights at any node is greater than 1, the whole tree is unbalanced ⇒ return `False`.

**Q6: How does this connect to interviews?**

Balanced tree checks are a classic pattern for combining "result + extra info" from a recursive function.

**Q7: Can I change the TreeNode constructor?**

No. Tests assume `TreeNode(value, left=None, right=None)` as in `main.py`.
