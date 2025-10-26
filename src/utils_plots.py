import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def scatter_with_trend(df, x_col="Experience", y_col="Salary"):
    fig, ax = plt.subplots()
    ax.scatter(df[x_col], df[y_col])

    X = df[x_col].values.reshape(-1, 1)
    y = df[y_col].values
    lr = LinearRegression().fit(X, y)
    x_line = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
    y_line = lr.predict(x_line)
    ax.plot(x_line, y_line)

    ax.set_xlabel("Experience (years)")
    ax.set_ylabel("Salary")
    ax.set_title("Experience vs Salary (with trend)")
    return fig
