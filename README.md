# DSA-Prep 🧠

A structured repository containing Data Structures and Algorithms implementations, problem-solving patterns, and interview preparation material — built in Python.

> **Goal:** Develop strong algorithmic thinking, problem-solving skills, and mastery of fundamental CS concepts through consistent practice.

---

## Philosophy

> Understanding patterns is more valuable than memorizing solutions.

Every problem solved answers:
- **Why** does this solution work?
- **What** pattern is being used?
- **When** should this approach be applied again?
- **What** are the time and space trade-offs?

---

## Repository Structure

```
DSA-Prep
│
├── Arrays_PrefixSum/
├── Two_Pointers/
├── Sliding_Window/
├── Hashing/
│
├── Stack/
├── Queue/
├── Linked_List/
├── Binary_Search/
│
├── Recursion/
├── Trees/
├── BST/
│
├── Heap/
├── Graphs/
├── Union_Find/
├── Trie/
│
├── Backtracking/
├── Greedy/
├── Dynamic_Programming/
│
└── Resources/
```

---

## Curriculum Progress

### Phase 1 — Foundation
| Topic | Status | Problems Solved |
|-------|--------|----------------|
| Arrays & Prefix Sum | ✅ Completed | 5 |
| Two Pointers | 🔄 In Progress | — |
| Sliding Window | ⬜ Pending | — |
| Hashing | ⬜ Pending | — |

### Phase 2 — Linear Structures
| Topic | Status | Problems Solved |
|-------|--------|----------------|
| Stack | ⬜ Pending | — |
| Queue & Deque | ⬜ Pending | — |
| Linked List | ⬜ Pending | — |
| Binary Search | ⬜ Pending | — |

### Phase 3 — Recursion & Trees
| Topic | Status | Problems Solved |
|-------|--------|----------------|
| Recursion & Call Stack | ⬜ Pending | — |
| Binary Trees DFS | ⬜ Pending | — |
| Binary Trees BFS | ⬜ Pending | — |
| BST | ⬜ Pending | — |

### Phase 4 — Advanced
| Topic | Status | Problems Solved |
|-------|--------|----------------|
| Heaps | ⬜ Pending | — |
| Graphs | ⬜ Pending | — |
| Union Find | ⬜ Pending | — |
| Trie | ⬜ Pending | — |

### Phase 5 — Hard
| Topic | Status | Problems Solved |
|-------|--------|----------------|
| Backtracking | ⬜ Pending | — |
| Monotonic Stack | ⬜ Pending | — |
| Greedy | ⬜ Pending | — |
| Dynamic Programming | ⬜ Pending | — |

---

## Problems Solved

### Topic 01 — Arrays & Prefix Sum ✅

| # | Problem | Difficulty | Time | Space | Notes |
|---|---------|------------|------|-------|-------|
| 1480 | [Running Sum of 1D Array](https://leetcode.com/problems/running-sum-of-1d-array/) | Easy | O(n) | O(n) | Classic prefix sum |
| 724 | [Find Pivot Index](https://leetcode.com/problems/find-pivot-index/) | Easy | O(n) | O(1) | Left sum = total − left − nums[i] |
| 485 | [Max Consecutive Ones](https://leetcode.com/problems/max-consecutive-ones/) | Easy | O(n) | O(1) | Counter reset pattern |
| 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | O(n) | O(n) | Prefix × suffix pass |
| 560 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | Medium | O(n) | O(n) | Prefix sum + hash map |

---

## Problem Format

Every solution file follows this structure:

```python
# Problem:    LeetCode 560 - Subarray Sum Equals K
# Approach:   Prefix Sum + Hash Map
# Time:       O(n)
# Space:      O(n)
# Key Insight: If prefix[j] - prefix[i] == k, then subarray [i+1..j] sums to k.
#              Store prefix sum frequencies in a hash map for O(1) lookups.

def subarray_sum(nums, k):
    count = 0
    prefix = 0
    freq = {0: 1}

    for n in nums:
        prefix += n
        count += freq.get(prefix - k, 0)
        freq[prefix] = freq.get(prefix, 0) + 1

    return count
```

---

## Key Insights Learned

- **Prefix sum = discrete CDF** — cumulative information stored for range queries
- **Old answer builds new answer** — the core idea behind DP thinking
- **Frequency map = counting occurrences** — hash maps turn O(n²) into O(n)
- **Separate loops add, nested loops multiply** — complexity intuition
- **O(1) space = no new array**, just variables
- **`return` exits immediately** — use it to avoid unnecessary work

---

## Complexity Standards

Every solution is analyzed for:
- **Time Complexity**
- **Space Complexity**
- **Scalability**
- **Possible Optimizations**

Preference is given to optimal, interview-ready solutions.

---

## Branching Strategy

```
main
├── feature/arrays-prefix-sum    ✅
├── feature/two-pointers         🔄
├── feature/sliding-window
└── ...
```

---

## Commit Convention

```
solved <problem-number> - <problem-name> | O(?) time O(?) space
```

Example:
```
solved 560 - Subarray Sum Equals K | O(n) time O(n) space
```

---

## Author

**Rohith Rajan V** — 2nd Year CS Student

- 🐙 GitHub: [RR-1902](https://github.com/RR-1902)
- 💼 LinkedIn: [rohith-rajan-v](https://linkedin.com/in/rohith-rajan-v)
- 🌐 Portfolio: [rohithrajanv.netlify.app](https://rohithrajanv.netlify.app)