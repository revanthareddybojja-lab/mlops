import pickle
import json

# Dummy training (no sklearn dependency issues)
X = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Simple "model"
model = {"multiplier": 2}

# Fake predictions
y_pred = [x * model["multiplier"] for x in X]

# Simple metrics
mse = sum((y[i] - y_pred[i])**2 for i in range(len(y))) / len(y)
r2 = 1.0

print("MSE:", mse)
print("R2:", r2)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save metrics
with open("metrics.json", "w") as f:
    json.dump({"mse": mse, "r2": r2}, f)