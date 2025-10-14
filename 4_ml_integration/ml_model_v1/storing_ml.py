#-------------------------------------------------------------------------------

# Serialization → Converting an ML model (a Python object) into a storable or transferable format (like .pkl, .joblib, or .onnx).
# Deserialization → Loading that saved model back into memory to use for prediction or retraining.

# Why We Need It
# --------------
# a. You train a model once, but you want to reuse it later without retraining.
# b. Needed for deployment — API servers or other systems can load and serve the model.
# c. Enables model sharing across environments or teams.
# d. Makes your experiment reproducible.
# e. Saves computation time and resources.

#------------------------------------------------------------------------------- 
 
import pickle
import joblib
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# For ONNX
import onnx
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

# For TensorFlow / Keras
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Prepare Sample Data
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Train a Scikit-learn Model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)
print("✅ Scikit-learn model trained successfully!")


# 1️.Pickle Serialization & Deserialization

print("\n--- Pickle ---")

# Serialize
with open("model_pickle.pkl", "wb") as f:
    pickle.dump(model, f)

# Deserialize
with open("model_pickle.pkl", "rb") as f:
    loaded_pickle_model = pickle.load(f)

print("Pickle Prediction:", loaded_pickle_model.predict(X_test[:3]))



# 2️. Joblib Serialization & Deserialization
print("\n--- Joblib ---")

joblib.dump(model, "model_joblib.joblib")
loaded_joblib_model = joblib.load("model_joblib.joblib")

print("Joblib Prediction:", loaded_joblib_model.predict(X_test[:3]))


# 3️. ONNX Serialization & Deserialization
print("\n--- ONNX ---")

# Convert sklearn model to ONNX format
initial_type = [('float_input', FloatTensorType([None, X.shape[1]]))]
onnx_model = convert_sklearn(model, initial_types=initial_type)
onnx.save_model(onnx_model, "model.onnx")

# Load ONNX model back
loaded_onnx_model = onnx.load("model.onnx")
onnx.checker.check_model(loaded_onnx_model)
print("ONNX model exported and verified successfully!")



# 4️.TensorFlow / Keras Model Serialization
print("\n--- TensorFlow / Keras ---")

# Build simple neural network
keras_model = Sequential([
    Dense(16, activation='relu', input_shape=(X.shape[1],)),
    Dense(3, activation='softmax')
])
keras_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
keras_model.fit(X_train, y_train, epochs=5, verbose=0)

# Save model in two ways:
# (a) H5 format
keras_model.save("keras_model.h5")

# (b) TensorFlow SavedModel format
keras_model.save("tf_saved_model", save_format="tf")

# Load models back
loaded_h5_model = tf.keras.models.load_model("keras_model.h5")
loaded_tf_model = tf.keras.models.load_model("tf_saved_model")

# Verify prediction
print("Keras (H5) Prediction:", loaded_h5_model.predict(X_test[:3]))
print("Keras (SavedModel) Prediction:", loaded_tf_model.predict(X_test[:3]))


print("\n All models serialized & deserialized successfully!")
