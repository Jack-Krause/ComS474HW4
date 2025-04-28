import argparse
import torch.nn as nn


def get_args():
    parser = argparse.ArgumentParser(description='Args for training networks')
    parser.add_argument('-seed', type=int, default=1, help='random seed')
    parser.add_argument('-num_epochs', type=int, default=20, help='num epochs')
    parser.add_argument('-batch', type=int, default=8, help='batch size')
    parser.add_argument('-lr', type=float, default=0.01, help='learning rate')
    parser.add_argument('-drop', type=float, default=0.3, help='drop rate')
    args, _ = parser.parse_known_args()
    return args


class Net(nn.Module):
    def __init__(self, args):
        super(Net, self).__init__()
        ### YOUR CODE HERE
        self.flatten = nn.Flatten()
        n_classes = 10
        
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(3*32*32, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, n_classes),
        )
        ### END YOUR CODE

    def forward(self, x):
        '''
        Input x: a batch of images (batch size x 3 x 32 x 32)
        Return the predictions of each image (batch size x 10)
        '''
        ### YOUR CODE HERE
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits
        ### END YOUR CODE
