import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, model_selection


def main():
    X, y = datasets.fetch_openml('mnist_784', return_X_y=True, data_home='./mnist')
    X = np.array(X, dtype='float32')
    y = np.array(y, dtype='uint8')

    X_train, X_test = model_selection.train_test_split(X, train_size=60000, shuffle=False)
    y_train, y_test = model_selection.train_test_split(y, train_size=60000, shuffle=False)

    C_train = np.cov(X_train.T, bias=1)
    _, eigvec = np.linalg.eigh(C_train)
    Z_train = X_train @ eigvec[:, -2:]

    plt.figure()
    for i in range(10):
        idx = np.where(y_train == i)
        plt.scatter(Z_train[idx, 0], Z_train[idx, 1], s=0.7, label=str(i))
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
