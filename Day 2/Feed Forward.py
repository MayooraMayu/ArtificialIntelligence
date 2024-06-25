import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import numpy as np

# Generate dummy data
np.random.seed(0)
X = np.random.rand(100, 10)  # 100 samples, 10 features each
y = np.random.randint(2, size=(100, 1))  # 100 samples, binary labels (0 or 1)

# Define the model
model = Sequential()
model.add(Dense(32, input_dim=10, activation='relu'))  # Input layer and first hidden layer
model.add(Dense(1, activation='sigmoid'))  # Output layer

# Compile the model
model.compile(loss='binary_crossentropy', optimizer=Adam(learning_rate=0.001), metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=10, batch_size=10)

# Evaluate the model
loss, accuracy = model.evaluate(X, y)
print(f'Loss: {loss}, Accuracy: {accuracy}')

# Predict
predictions = model.predict(X)
print(predictions)
