import numpy as np


class Linear:
    def __init__(self, in_features, out_features):
        """
        Initialize the weights and biases with zeros
        W shape: (out_features, in_features)
        b shape: (out_features,)  # Changed from (out_features, 1) to match PyTorch
        """
        # DO NOT MODIFY
        self.W = np.zeros((out_features, in_features))
        self.b = np.zeros(out_features)

    def init_weights(self, W, b):
        """
        Initialize the weights and biases with the given values.
        """
        # DO NOT MODIFY
        self.W = W
        self.b = b

    def forward(self, A):
        """
        :param A: Input to the linear layer with shape (*, in_features)
        :return: Output Z with shape (*, out_features)

        Handles arbitrary batch dimensions like PyTorch
        """

        # Store input for backward pass
        self.A = A

        Z = A @ self.W.T + self.b

        return Z

    def backward(self, dLdZ):
        """
        :param dLdZ: Gradient of loss wrt output Z (*, out_features)
        :return: Gradient of loss wrt input A (*, in_features)
        """

        batch_size = np.prod(dLdZ.shape[:-1])
        dLdZ_fl = dLdZ.reshape(batch_size, dLdZ.shape[-1])
        A_fl = self.A.reshape(batch_size, self.A.shape[-1])

        # Compute gradients (refer to the equations in the writeup)
        # self.dLdA = NotImplementedError
        self.dLdW = dLdZ_fl.T @ A_fl
        self.dLdb = np.sum(dLdZ, axis=tuple(range(dLdZ.ndim - 1)))
        self.dLdA = dLdZ @ self.W

        # Return gradient of loss wrt input
        return self.dLdA
