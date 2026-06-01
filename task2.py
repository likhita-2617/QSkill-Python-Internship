import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# 1. LOAD THE DATASET
df = pd.read_csv('house_data.csv')
print("--- House Dataset Loaded ---")
print(df)
print("\n")

# 2. PREPROCESS: SEPARATE FEATURES (X) AND TARGET (y)
# X contains columns used to predict. y is what we want to predict.
X = df[['Size_SqFt', 'Rooms', 'Location_Score']]
y = df['Price']

# Split data: 75% for training the model, 25% for testing if it's smart
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 3. TRAIN THE LINEAR REGRESSION MODEL
model = LinearRegression()
model.fit(X_train, y_train) # Training happens here!
print("Model training complete.\n")

# 4. EVALUATE THE MODEL
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"Model Error (Mean Absolute Error): ${mae:.2f}")
print(f"Model Accuracy Score (R2 Score): {r2:.2f}")
print("\n")

# 5. MAKE A CUSTOM PREDICTION
# Let's predict the price of a custom house: 1700 sqft, 3 rooms, location score of 7
custom_house = [[1700, 3, 7]]
predicted_price = model.predict(custom_house)

print("--- Making a Live Prediction ---")
print(f"Features: 1700 SqFt, 3 Rooms, Location Rating: 7/10")
print(f"Predicted House Value: ${predicted_price[0]:,.2f}")