## Part A: Code and Discuss

### `sum_to_goal` function
1. Each member of the group writes the implementation of the following function on a piece of paper:

```python
def sum_to_goal(numbers_list, goal):     
```
2. My guess for this functions time complexity was O(n<sup>2</sup>). After writing the function, my first instinct was just to picture what the function has to do. It finds a pair, every number basically needs to be checked against every other number in the list.This was a case of nested loops, so I figured it'd end up being two loops, and the time complexity of a function with nested loops are normally O(n<sup>2</sup>).

3. Yes, my friend's solution was similar to mine and the time complexity I calculated from his function was the same as mine which is O(n<sup>2</sup>)

4. Discussed our results in a group

5. Results
   - Yes it did, as we both had nested loops in our solution.
   - All of our group members had similar solution so the run time was basically the same to be honest.
```python
def sum_to_goal(numbers_list, goal):
    n = len(numbers_list)
 
    for i in range(n):
        for j in range(i + 1, n):
            if numbers_list[i] + numbers_list[j] == goal:
                return numbers_list[i] * numbers_list[j]
 
    return None
```
```text
Analysis:
T(n) = 2 + 1 + 2n + 4·[n(n − 1)/2] + 1
     = 4 + 2n + 2n(n − 1)
     = 4 + 2n + 2n² − 2n
     = 2n² + 4
```
   - I would basically time the function on lists of increasing size, doubling the size each run, using a goal value that guarantees no match (so it always hits the worst case). If it's really O(n²), runtime should roughly quadruple each time the size doubles.
   - Answers in `sum_to_goal.py` and `sum_to_goal_tester.py`

### fibonacci function

5. My function
```python
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)
```
Analysis:
```text
T(n) = T(n-1) + T(n-2) + c
Recursive,
from here we conclude O(n²)
```

   - No, I had thought my answer as O(n) and someone my team members got O(n²) but I didn't. The complexity was really O(2<sup>n</sup>)
   - I would test it by increasing values of n and check whether runtime grows linearly or explodes much faster
   - Done in `fibonacci.py` and `fibonacci_tester.py`

## Part B: Analysis

### Function 1

```python
def function1(n):
	total = 0   # 1 op (assignment)

	for i in range(n):  # 1 op (range call)
		x = i + 1        # 2 op (n times)
		total += x * x   # 3 op (n times)

	return total        # 1 op (return func)
```

```text
T(n) = 1 + 1 + n·(2 + 3) + 1 = 5n + 3 
∴ O(n)
```

### Function 2

```python
def function2(n):
	return (n * (n + 1) * (2 * n + 1)) // 6   # 7 op (return + multiplication + addition and division)
```

```text
T(n) = 1 + 1 + 1 + 1 + 1 + 1 + 1 = 7
∴ O(1)
```

### Function 3

```python
def function3(list):        
	n = len(list)  # 2 op (assignment + len func) 
	for i in range(n - 1):   # 2 op (range and subtraction, runs (n-1) times)
		for j in range(n - 1 - i):  # 3 op (range and 2 subtraction, runs (n-1-i) times
			if list[j] > list[j + 1]:  # 4 op (indexing, comparison and addition)
				tmp = list[j]  # 2 op (assignment and indexing)
				list[j] = list[j + 1]  # 4 op (indexing, comparison and addition)
				list[j + 1] = tmp  # 3 op (indexing, addition and assignment)
```

```text
T(n) = 2 + 2 + 3(n-1) + 13·[n(n-1)/2] = (13/2)n² − (7/2)n + 1 
∴ O(n²)
```
## Team Members

1. Aydin Arif
2. Eren Kilinc
3. Thuong Tuyen Tran

Sadly I do not remember our group number.
