import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Sample phishing dataset (replace with real data)
data = {
    "url_length": [10, 20, 30, 100, 120, 15, 35, 150, 200, 8],
    "num_dots": [1, 2, 3, 5, 0, 2, 4, 1, 0, 1],
    "num_slashes": [1, 3, 5, 7, 9, 2, 4, 6, 8, 1],
    "num_digits": [2, 5, 0, 3, 7, 1, 8, 9, 4, 0],
    "https": [1, 1, 0, 1, 0, 1, 1, 0, 1, 0],  # 1 = https, 0 = http
    "label": [0, 0, 1, 1, 1, 0, 1, 1, 1, 0]  # 0 = Safe, 1 = Phishing
}

df = pd.DataFrame(data)

# Split data into features and labels
X = df.drop(columns=["label"])
y = df["label"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "phishing_model.pkl")

print("Model trained and saved as phishing_model.pkl")
