
# K-Nearest Neighbors (KNN) Classification

 This project demonstrates how the **K-Nearest Neighbors (KNN)** algorithm can be used to classify a new data point based on the classes of its nearest neighboring points.


 The program uses a small set of training data containing:

 - A point name
- X and Y coordinates
- A class label (`A` or `B`)

 The new point to classify is:

```
Q = (4, 4)
```

 The program calculates the **Euclidean distance** between `Q` and every training point, sorts the points by distance, and then predicts the class using majority voting for different values of `K`.

  📊 Training Data

 | Point | Coordinates | Class |
| --- | --- | --- |
| P1 | (4, 3) | B |
| P2 | (3, 3) | A |
| P3 | (5, 5) | A |
| P4 | (2, 4) | A |
| P5 | (8, 8) | B |
| P6 | (7, 2) | B |

New point:

```
Q = (4, 4)
```

 🧮 Euclidean Distance

 The Euclidean distance between two points is calculated using:

```
distance = √((x₂ - x₁)² + (y₂ - y₁)²)
```

 For example, the distance between `Q = (4, 4)` and `P1 = (4, 3)` is:

```
√((4 - 4)² + (3 - 4)²)
= √1
= 1
```

 🔢 KNN Classification

 The program performs classification using three different values of `K`:

 - `K = 1`
- `K = 3`
- `K = 5`

 For each value of `K`, the program:

 1. Selects the `K` closest points.
2. Gets their class labels.
3. Counts the occurrences of each class.
4. Uses majority voting to determine the predicted class.

 ## 📈 Expected Distances

 The points are ordered from closest to farthest approximately as follows:

 | Point | Distance | Class |
| --- | --- | --- |
| P1 | 1.000 | B |
| P2 | 1.414 | A |
| P3 | 1.414 | A |
| P4 | 2.000 | A |
| P6 | 3.606 | B |
| P5 | 5.657 | B |

## 🎯 Expected Predictions

 ### K = 1

 Nearest neighbour:

```
P1
```

 Class:

```
B
```

 **Predicted Class: B**

 ### K = 3

 Nearest neighbours:

```
P1, P2, P3
```

 Classes:

```
B, A, A
```

 Majority class:

```
A
```

 **Predicted Class: A**

 ### K = 5

 Nearest neighbours:

```
P1, P2, P3, P4, P6
```

 Classes:

```
B, A, A, A, B
```

 Majority class:

```
A
```

 **Predicted Class: A**

 ## 🛠️ Requirements

 - Python 3.x
- No external libraries are required.

 The program uses Python's built-in:

```
math
```

 and

```
collections.Counter
```

 modules.

 ## ▶️ How to Run

 Save the code in a file such as:

```
knn.py
```

 Then run:

```
python knn.py
```

 ## 📋 Example Output

```
Distances from Q = (4, 4)
--------------------------------
P1 -> Distance = 1.0 , Class = B
P2 -> Distance = 1.414 , Class = A
P3 -> Distance = 1.414 , Class = A
P4 -> Distance = 2.0 , Class = A
P6 -> Distance = 3.606 , Class = B
P5 -> Distance = 5.657 , Class = B

KNN Classification
-------------------
K = 1
Nearest neighbours: ['P1']
Classes: ['B']
Predicted Class: B

K = 3
Nearest neighbours: ['P1', 'P2', 'P3']
Classes: ['B', 'A', 'A']
Predicted Class: A

K = 5
Nearest neighbours: ['P1', 'P2', 'P3', 'P4', 'P6']
Classes: ['B', 'A', 'A', 'A', 'B']
Predicted Class: A
```

 ## 📚 Concepts Demonstrated

 This project demonstrates:

 - K-Nearest Neighbors (KNN)
- Euclidean distance
- Distance-based sorting
- Nearest-neighbour selection
- Majority voting
- Classification
- Effect of different `K` values

 ## 💡 Conclusion

 The classification result depends on the value of `K`.

 For this dataset:

```
K = 1  → B
K = 3  → A
K = 5  → A
```

 This shows why choosing an appropriate value of `K` is important when using the KNN algorithm.

 You can save this directly as **`README.md`** in your project folder.
