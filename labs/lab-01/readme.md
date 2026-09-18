# Lab 1

This assessment contains materials that may be subject to copyright and other intellectual property rights. 

Modification, distribution or reposting of this document is strictly prohibited. Learners found reposting this document or its solution anywhere will be subject to the college’s Academic Integrity policy.



## Due

This lab is due at the end of the day that is before your next lab:
- section `NAA`: Monday, Sep 28 2026, @ 23:59
- section `NBB`: Thursday, Oct 1 2026, @ 23:59


## Objectives

- Learn how to do analysis.
- Make connections between analytical run times and actual performance.

## Setup

See Instructions in [lab #0](../lab-00/readme.md) to set up your repository.

## Part A: Code and Discuss

Students who are more than 15 minutes late at the lab, cannot get credit for this part (this part will be considered incomplete for them).

Form a group 3-4 members.

**For coding, you are not allowed to use any library functions for this lab unless it is explicitely stated in the specification.**

### `sum_to_goal` function

1. Each member of the group writes the implementation of the following function on a piece of paper:

  ```python
  def sum_to_goal(numbers_list, goal)
  ```

  This function is passed a list of unique numbers (assume parameters are valid) and it will find the two numbers in the list that sum up to the `goal` value. The function returns the product of the two numbers (the *product* is the result of multiplying the two numbers together).  If there are no two numbers whose sum is the `goal`, this function returns `None`.

2. Estimate your own function's time complexity.  You do not need to do a full analysis but make a guess. Write your guess on the paper.

3. Trade your functions within your group so that each person is looking at someone else's code and perform a full analysis of the function with respect to the size of the list.

4. Discuss your results in the group.

5. Report your results in the file `lab1.md`:
    - Did your teammate's analysis match what you thought your function's runtime was?
    - Was there any version in the group that had a different complexity?  Which version looks like it would run the fastest?
    - Rewrite the function in `lab1.md` file in your repository, what was your guess for complexity, and what was your teammates conclusion.  You can write exactly what you wrote on paper or you can alter it based on your discussions with your teammates.  If you made a change (outside of correcting syntax), why did you do it?
    - Describe in English how would you test whether the complexity analysis was correct or not?
    - Write the function in `sum_to_goal.py` and a small Python program in `sum_to_goal_tester.py` to test it and demonstrate that the function behaves correctly (use the `unittest` library); your tester should check the output for at least 5 different inputs. Look in *Lab #0* to see how to write a tester in Python.

### `fibonacci` function

1. Each member of the group writes the implementation of the following function on a piece of paper:

  ```python
  def fibonacci(n)
  ```

  This function receives as parameter (assume valid) and returns the $n^{th}$ fibonacci number in the fibonacci sequence. The fibonacci sequence is defined as following:

  Let $F_i$ represent the $i^{th}$ fibonacci number in the sequence; then

  - $F_0 = 0$
  - $F_1 = 1$
  - $F_2 = 1$
  - $F_3 = 2$
  - $F_4 = 3$
  - $F_5 = 5$
  - $F_6 = 8$
  - $F_7 = 13$
  - $F_8 = 21$
  - $F_9 = 34$
  ...
  - $F_n = F_{n-1} + F_{n-2}$

2. Estimate your own function's time complexity.  You do not need to do a full analysis but make a guess. Write your guess on the paper.

3. Trade your functions within your group so that each person is looking at someone else's code and perform a full analysis of the function with respect to the size of the list.

4. Discuss your results in the group.

5. Report your results in the file `lab1.md`:
  - Did your teammate's analysis match what you thought your function's runtime was?
  - Was there any version in the group that had a different complexity?  Which version looks like it would run the fastest?
  - Rewrite the function in `lab1.md` file in your repository, what was your guess for complexity, and what was your teammates conclusion.  You can write exactly what you wrote on paper or you can alter it based on your discussions with your teammates.  If you made a change (outside of correcting syntax), why did you do it?
  - Describe in English how would you test whether the complexity analysis was correct or not?
  - Write the function in `fibonacci.py` and a small Python program in `fibonacci_tester.py` to test it and demonstrate that the function behaves correctly (use the `unittest` library); your tester should check the output for at least 5 different inputs. Look in *Lab #0* to see how to write a tester in Python.



## Part B: Analysis

Perform an analysis of the functions shown below. Write your analysis in file `lab1.md`.

Count the number of operations for the worst case scenario, calculate your $T(n)$ and state the complexity in *Big-O* notation.

In your analysis you must precisely identify:
- how does the worst case scenario looks like (is there a worst case scenario?).
- how many operations are on every line (and which operations are you counting).
- if there is a loop, how many times the loop is running.


### Function 1

Analyze the following function with respect to the parameter `n` (a positive integer).

```python
def function1(n):
	total = 0

	for i in range(n):
		x = i + 1
		total += x * x

	return total
```

### Function 2

Analyze the following function with respect to the parameter `n` (a positive integer).

```python
def function2(n):
	return (n * (n + 1) * (2 * n + 1)) // 6
```

### Function 3 (challenging)

Analyze the following with respect to the length of the list received as parameter (a list of numbers).  The provided Python code uses two library functions: [`range()`](https://docs.python.org/3.12/library/functions.html#func-range) and [`len()`](https://docs.python.org/3/library/functions.html#len). We search in the documentation ([len](https://pythoncomplexity.com/builtins/list/) and [range](https://pythoncomplexity.com/builtins/range/)), and we find that both functions have a complexity of $O(1)$ (this means that both functions have constant complexity); use $1$ as the number of operations for them in your analysis.

```python
def function3(list):
	n = len(list)
	for i in range(n - 1):
		for j in range(n - 1 - i):
			if list[j] > list[j + 1]:
				tmp = list[j]
				list[j] = list[j + 1]
				list[j + 1] = tmp
```

## Submitting your lab

In the `release` folder, you will find some empty files where you must write your solution.

In order to get a mark for this lab, you must submit:

- two discussion reports as required in part A, together with your implementations of the functions and their testers in Python.
- a complete analysis of every function in part B.

Place all your work for this lab into the folder `lab-01` in your GitHub repository, unless otherwise indicated. When you are happy with the state of your files, submit a link to your repo's `lab-01` folder into BlackBoard.


## Lab Rubric:

| Criteria       | Poor - 0 mark       | Fair - 1 mark  | Good - 2 marks|
|----------------|---------------------|----------------|---------------|
| Lab Completion | No part is complete | One part is complete, but the other one is missing or is lacking key steps. | Both parts are complete. |





