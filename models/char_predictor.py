import numpy as np
import sys

sys.path.append("mytorch")
from gru_cell import *
from nn.linear import *


class CharacterPredictor(object):
    """CharacterPredictor class.

    This is the neural net that will run one timestep of the input
    You only need to implement the forward method of this class.
    This is to test that your GRU Cell implementation is correct when used as a GRU.

    """

    def __init__(self, input_dim, hidden_dim, num_classes):
        super(CharacterPredictor, self).__init__()
        """The network consists of a GRU Cell and a linear layer."""
        self.gru = GRUCell(input_dim, hidden_dim)  # TODO
        self.projection = Linear(hidden_dim, num_classes)  # TODO
        self.num_classes = num_classes  # TODO
        self.hidden_dim = hidden_dim  # TODO
        self.projection.W = np.random.rand(num_classes, hidden_dim)

    def init_rnn_weights(
            self, Wrx, Wzx, Wnx, Wrh, Wzh, Wnh, brx, bzx, bnx, brh, bzh, bnh
    ):
        # DO NOT MODIFY
        self.gru.init_weights(
            Wrx, Wzx, Wnx, Wrh, Wzh, Wnh, brx, bzx, bnx, brh, bzh, bnh
        )

    def __call__(self, x, h):
        return self.forward(x, h)

    def forward(self, x, h):
        """CharacterPredictor forward.

        A pass through one time step of the input

        Input
        -----
        x: (feature_dim)
            observation at current time-step.

        h: (hidden_dim)
            hidden-state at previous time-step.
        
        Returns
        -------
        logits: (num_classes)
            hidden state at current time-step.

        hnext: (hidden_dim)
            hidden state at current time-step.

        """
        hnext = self.gru(x, h)  # TODO
        # self.projection expects input in the form of batch_size * input_dimension
        # Therefore, reshape the input of self.projection as (1,-1)
        proj = hnext.reshape((1, -1))
        logits = self.projection(proj)  # TODO
        logits = logits.reshape(-1, )  # uncomment once code implemented
        return logits, hnext


def inference(net, inputs):
    """CharacterPredictor inference.

    An instance of the class defined above runs through a sequence of inputs to
    generate the logits for all the timesteps.

    Input
    -----
    net:
        An instance of CharacterPredictor.

    inputs: (seq_len, feature_dim)
            a sequence of inputs of dimensions.

    Returns
    -------
    logits: (seq_len, num_classes)
            one per time step of input..

    """

    # This code should not take more than 10 lines.
    (seq_len, feature_dim) = inputs.shape
    logits = np.zeros((seq_len, net.num_classes))
    h_prev_t = np.zeros((net.hidden_dim, 1))
    for t in range(seq_len):
        logits[t, :], hnext = net(inputs[t], h_prev_t)
        h_prev_t = hnext

    return logits
