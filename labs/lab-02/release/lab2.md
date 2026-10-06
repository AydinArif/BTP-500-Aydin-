# Lab 2

## Part A: In-Class Discussion

### Group members

List the members of your group member below:
- Aydin Arif
- Eren Kilinc
- The Duy Vu
- Rohith Haridas

**1. What they do:** Each one takes a list and a key and returns how many pairs of items add up to the key. For `[1,2,3,4,5]` and key 6 it returns 2, from (1,5) and (2,4).

**2. Ranking (gut feeling):** three, two, one. `one` has nested loops, `three` is just dictionary lookups.

**3. Timing (n=1000):** one = 0.0233s, two = 0.0002s, three = 0.00013s. Ranking matched. The surprise was how much slower `one` is.

**4. Analysis:**
- `one`: n(n-1)/2 comparisons, so O(n^2).
- `two`: sort is O(n log n), the loop is O(n), so O(n log n).
- `three`: n inserts and n lookups at O(1) each, so O(n).

**5. Increasing data:**

| n | one | two | three |
|---|---|---|---|
| 1000 | 0.0233 | 0.00020 | 0.00013 |
| 2000 | 0.0919 | 0.00044 | 0.00029 |
| 3000 | 0.2056 | 0.00064 | 0.00053 |
| 4000 | 0.3676 | 0.00093 | 0.00068 |

Doubling n makes `one` about 4 times slower, which fits O(n^2). The other two grow close to linearly. This matches my analysis.
