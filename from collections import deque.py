from collections import deque

queue = deque()
visit = set()

queue.append(initial_state)
visit.add(initial_state)

while queue != []:
  state = queue.popleft()

  if state == goal_state:
    # do something
    break

  for next_state in get_next_states(state):
    queue.append(next_state)
    visit.add(next_state)
  


def backtracking(root, path):
  if root == "base-case":
    return False
  
  # assume the current node is the correct
  path.append(root)

  # if the current node is the goal, return True
  if root == "goal":
    return True

  # explore decisions 
  decisions = [ "decision1", "decision2" ] # e.g. [ root."left", root."right" ]

  for decision in decisions:
    return backtracking(decision, path)

  # if no decision is invalid, remove the current node from the path
  path.pop()

  return False