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

