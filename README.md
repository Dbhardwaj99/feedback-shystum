import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 3.5, 4, 5.5, 6])

model = LinearRegression()

model.fit(X, y)

predictions = model.predict(X)

plt.scatter(X, y, color='blue', label='Data')

plt.plot(X, predictions, color='red', label='Regression Curve')

plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression')
plt.legend()
plt.show()
