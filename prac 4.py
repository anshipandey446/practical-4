import math
from collections import Counter

# Training data
points = [
    ("P1", (4, 3), "B"),
    ("P2", (3, 3), "A"),
    ("P3", (5, 5), "A"),
    ("P4", (2, 4), "A"),
    ("P5", (8, 8), "B"),
    ("P6", (7, 2), "B")
]

# New point
Q = (4, 4)

# Calculate Euclidean distances
distances = []

for name, point, label in points:
    distance = math.sqrt((point[0] - Q[0])**2 + (point[1] - Q[1])**2)
    distances.append((distance, name, label))

# Sort by distance
distances.sort()

# Print distances
print("Distances from Q =", Q)
print("--------------------------------")

for distance, name, label in distances:
    print(name, "-> Distance =", round(distance, 3), 
          ", Class =", label)

# Classification for different K values
print("\nKNN Classification")
print("-------------------")

for k in [1, 3, 5]:
    nearest = distances[:k]
    
    # Get classes of nearest neighbours
    classes = [label for distance, name, label in nearest]
    
    # Majority vote
    prediction = Counter(classes).most_common(1)[0][0]
    
    print("K =", k)
    print("Nearest neighbours:", [name for distance, name, label in nearest])
    print("Classes:", classes)
    print("Predicted Class:", prediction)
    print()
