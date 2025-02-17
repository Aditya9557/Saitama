from collections import deque

# Initialize queue, visited set, and target
queue = deque()
visited = set()
target = 10  # Example target value, replace with your actual target
cap1, cap2 = 5, 3  # Example capacities, replace with your actual values

# Add initial state to the queue
queue.append((0, 0))  # Assuming starting state is (0, 0)

while queue:
    x, y = queue.popleft()

    # Check if target is reached
    if x == target or y == target:
        print("Goal Found:", x, y)
        break  # Exit the loop when the goal is found

    # Skip if the state is already visited
    if (x, y) in visited:
        continue

    # Mark the current state as visited
    visited.add((x, y))
    print("Visited:", x, y)

    # Generate new states and add them to the queue
    queue.extend([
        (cap1, y),  # Fill the first container to its capacity
        (x, cap2),  # Fill the second container to its capacity
        (0, y),     # Empty the first container
        (x, 0),     # Empty the second container
        (x - min(x, cap2 - y), y + min(x, cap2 - y)),  # Pour from x to y
        (x + min(y, cap1 - x), y - min(y, cap1 - x))   # Pour from y to x
    ])
