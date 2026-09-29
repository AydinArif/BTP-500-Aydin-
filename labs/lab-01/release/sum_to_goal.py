# implement here your sum_to_goal function as instructed.

def sum_to_goal(numbers_list, goal):
  n = len(numbers_list)
  for i in range(n):
    for j in range(i + 1, n):
      if numbers_list[i] + numbers_list[j] == goal:
        return numbers_list[i] * numbers_list[j]
  
  return None
