import pandas as pd
import random
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

random.seed(42)

data = [
    {
        "weight": random.randint(130, 220),
        "length": round(random.uniform(6, 9), 1),
        "fruit": "apple"
    }
    for _ in range(50)
]

data += [
    {
        "weight": random.randint(90, 180),
        "length": round(random.uniform(12, 20), 1),
        "fruit": "banana"
    }
    for _ in range(50)
]

df = pd.DataFrame(data)
df.to_csv("fruits.csv", index=False)

X = df[["weight", "length"]]
y = df["fruit"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2%}")
print(classification_report(y_test, y_pred))

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

colors = {"apple": "red", "banana": "gold"}

for fruit, color in colors.items():
    subset = X_train[y_train == fruit]
    axes[0].scatter(subset["weight"], subset["length"],
                    c=color, label=fruit, alpha=0.7, edgecolors="k", s=70)
axes[0].set_title(f"Train ({len(X_train)} samples)")
axes[0].set_xlabel("Weight (g)")
axes[0].set_ylabel("Length (cm)")
axes[0].legend()
axes[0].grid(alpha=0.3)

for fruit, color in colors.items():
    subset = X_test[y_test == fruit]
    axes[1].scatter(subset["weight"], subset["length"],
                    c=color, label=fruit, alpha=0.7, edgecolors="k",
                    marker="^", s=90)
axes[1].set_title(f"Test ({len(X_test)} samples)")
axes[1].set_xlabel("Weight (g)")
axes[1].set_ylabel("Length (cm)")
axes[1].legend()
axes[1].grid(alpha=0.3)

plt.tight_layout()
plt.show()

x_min, x_max = X["weight"].min() - 10, X["weight"].max() + 10
y_min, y_max = X["length"].min() - 1, X["length"].max() + 1

xx, yy = np.meshgrid(
    np.arange(x_min, x_max, 0.5),
    np.arange(y_min, y_max, 0.05)
)

grid = np.c_[xx.ravel(), yy.ravel()]
grid_scaled = scaler.transform(grid)
Z = model.predict(grid_scaled)
Z = (Z == "banana").astype(int).reshape(xx.shape)

plt.figure(figsize=(10, 6))
plt.contourf(xx, yy, Z, alpha=0.2,
             cmap=ListedColormap(["red", "gold"]))

for fruit, color, marker in [("apple", "red", "o"), ("banana", "gold", "s")]:
    subset = df[df["fruit"] == fruit]
    plt.scatter(subset["weight"], subset["length"],
                c=color, label=fruit, edgecolors="k",
                marker=marker, s=60, alpha=0.8)

plt.xlabel("Weight (g)")
plt.ylabel("Length (cm)")
plt.title("KNN Decision Boundary (k=5)")
plt.legend()
plt.grid(alpha=0.3)
plt.show()



new_fruits = pd.DataFrame({
    "weight": [110, 160, 200, 140],
    "length": [15.0, 8.0, 18.5, 7.5],
})

new_fruits_scaled = scaler.transform(new_fruits)

probs = model.predict_proba(new_fruits_scaled)
preds = model.predict(new_fruits_scaled)

new_fruits["prediction"] = preds
new_fruits["prob_apple"]  = probs[:, list(model.classes_).index("apple")]
new_fruits["prob_banana"] = probs[:, list(model.classes_).index("banana")]

print(new_fruits.to_string(index=False))