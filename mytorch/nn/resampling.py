import numpy as np


class Upsample1d():

    def __init__(self, upsampling_factor):
        self.upsampling_factor = upsampling_factor

    def forward(self, A):
        """
        Argument:
            A (np.array): (batch_size, in_channels, input_width)
        Return:
            Z (np.array): (batch_size, in_channels, output_width)
        """
        batch_size, in_channels, input_width = A.shape
        output_width = self.upsampling_factor * (input_width - 1) + 1

        scaled = np.zeros((batch_size, in_channels, output_width))

        scaled[:, :, ::self.upsampling_factor]=A
        Z = scaled  # TODO

        return Z

    def backward(self, dLdZ):
        """
        Argument:
            dLdZ (np.array): (batch_size, in_channels, output_width)
        Return:
            dLdA (np.array): (batch_size, in_channels, input_width)
        """
        updated = dLdZ[:, :, ::self.upsampling_factor]
        dLdA = updated

        return dLdA


class Downsample1d():

    def __init__(self, downsampling_factor):
        self.downsampling_factor = downsampling_factor

    def forward(self, A):
        """
        Argument:
            A (np.array): (batch_size, in_channels, input_width)
        Return:
            Z (np.array): (batch_size, in_channels, output_width)
        """
        self.input_width=A.shape[2]
        Z =A[:, :, ::self.downsampling_factor]  # TODO

        return Z

    def backward(self, dLdZ):
        """
        Argument:
            dLdZ (np.array): (batch_size, in_channels, output_width)
        Return:
            dLdA (np.array): (batch_size, in_channels, input_width)
        """
        batch_size, in_channels, output_width=dLdZ.shape

        dLdA = np.zeros((batch_size, in_channels, self.input_width)) # TODO

        dLdA[:, :, ::self.downsampling_factor]=dLdZ
        return dLdA


class Upsample2d():

    def __init__(self, upsampling_factor):
        self.upsampling_factor = upsampling_factor

    def forward(self, A):
        """
        Argument:
            A (np.array): (batch_size, in_channels, input_height, input_width)
        Return:
            Z (np.array): (batch_size, in_channels, output_height, output_width)
        """
        output_height=self.upsampling_factor*(A.shape[2]-1)+1
        output_width=self.upsampling_factor*(A.shape[3]-1)+1
        Z = np.zeros((A.shape[0], A.shape[1], output_height, output_width)) # TODO

        Z[:, :, ::self.upsampling_factor, ::self.upsampling_factor]=A
        return Z

    def backward(self, dLdZ):
        """
        Argument:
            dLdZ (np.array): (batch_size, in_channels, output_height, output_width)
        Return:
            dLdA (np.array): (batch_size, in_channels, input_height, input_width)
        """

        dLdA = dLdZ[:, :, ::self.upsampling_factor, ::self.upsampling_factor] # TODO

        return dLdA


class Downsample2d():

    def __init__(self, downsampling_factor):
        self.downsampling_factor = downsampling_factor

    def forward(self, A):
        """
        Argument:
            A (np.array): (batch_size, in_channels, input_height, input_width)
        Return:
            Z (np.array): (batch_size, in_channels, output_height, output_width)
        """
        self.input_width=A.shape[3]
        self.input_height=A.shape[2]
        Z = A[:, :, ::self.downsampling_factor, ::self.downsampling_factor]  # TODO

        return Z

    def backward(self, dLdZ):
        """
        Argument:
            dLdZ (np.array): (batch_size, in_channels, output_height, output_width)
        Return:
            dLdA (np.array): (batch_size, in_channels, input_height, input_width)
        """
        (batch_size, in_channels, output_height, output_width)=dLdZ.shape
        dLdA = np.zeros((batch_size, in_channels, self.input_height, self.input_width))# TODO

        dLdA[:, :, ::self.downsampling_factor, ::self.downsampling_factor]=dLdZ
        return dLdA
