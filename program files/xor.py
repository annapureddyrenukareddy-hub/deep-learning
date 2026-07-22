import numpy as np
from sklearn.neural_network import MLPClassifier
X=np.array(
    [
    [0,0],
    [0,1],
    [1,0],
    [1,1]
]
)
y=np.array([0,1,1,0])
model=MLPClassifier(
    hidden_layer_sizes=(4),
    activation ='tanh',
    solver='lbfgs',
    max_iter=1000,
    random_state=6
)
model.fit(X,y)
predictions=model.predict(X)
print("Predictions:")
print(predictions)
print("\nActual Output:")
print(y)
print(
    "\nAccuracy:",model.score(X,y)
)
