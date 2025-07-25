import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Generate synthetic data: 1000 transactions, each with 5 features
np.random.seed(42)

X = np.random.rand(1000, 5) * 1000  # e.g., gas, value, time diff, frequency, wallet age
y = np.random.randint(0, 2, 1000)   # 0 = normal, 1 = malicious

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create a Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train model
model.fit(X_train, y_train)

# Save model to file
joblib.dump(model, "model/transaction_model.joblib")

print("Model trained and saved at: model/transaction_model.joblib")
