# using the example from
# http://pytorch.org/tutorials/beginner/examples_nn/two_layer_net_optim.html
# to solve this 
from torch.utils.data import Dataset, DataLoader
from torch.autograd import Variable
import torch
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math

def load_dataset(txt_filepath):
    """Loads a toy dataset from a text file.
    
    Args:
        txt_filepath: file path to the text file containing the dataset
    Returns:
        data: NxD ndarray, where N is the number of samples in the dataset and D is the dimension of each sample 
        target: N-dimensional vector, where N is the number of samples in the dataset
    """
    coords_x,coords_y,labels = np.loadtxt(txt_filepath).T
    data = np.array([coords_x,coords_y]).T
    # labels should starts from 0
    target = labels - 1 
    return data, target


def visualize_toy_dataset(data, target):
    """Plots a 2D toy dataset with 3 classes.
    
    Args:
        data: NxD ndarray, where N is the number of samples in the dataset and D is the dimension of each sample 
        target: N-dimensional vector, where N is the number of samples in the dataset
    """
    n = data.shape[0]
    for i in range(0, n):
        if target[i] == 0:
            plt.plot(data[i, 0], data[i, 1], 'ro')
        elif target[i] == 1:
            plt.plot(data[i, 0], data[i, 1], 'go')
        else:
            plt.plot(data[i, 0], data[i, 1], 'bo')


def create_grid_coords(N=50):
    """ Creates a 2D grid centered on the origin with edge length 2.

    Note: Using the generated grid as input to your network, you can visualize the learned class boundaries.
    For plotting you can use imshow(...) from matplotlib.

    Returns:
        N^2x2 ndarray, where each row correspondes to a pair of coordinates in 2d space
    """
    xx=-(1-2*np.array(range(0,N))/float(N-1))
    grid_x, grid_y=np.meshgrid(xx,xx)
    grid=np.stack([grid_x.flatten(), grid_y.flatten()], axis=1)
    return grid

class ToyDataset(Dataset):
    """ A toy dataset class which implements the abstract class torch.utils.data.Dataset .
    (for reference see http://pytorch.org/docs/master/data.html#torch.utils.data.Dataset)
    """
    def __init__(self, filename):
        self.data, self.target = load_dataset(filename)
        print("Imported", filename + ", containing", self.__len__(), "datapoints")

    def __getitem__(self, index):
        return self.data[index], self.target[index]

    def __len__(self):
        return len(self.data)
    
    def visualize(self):
        return visualize_toy_dataset(self.data, self.target)

def lossfunction(pred, real):
    # http://pytorch.org/docs/master/nn.html#loss-functions
    loss = torch.nn.L1Loss(size_average=False)
    
    return loss(pred, real)

def train(dataSet):
    
    # batch size 
    N = dataSet.__len__()

    # input dimension
    D_in = len(dataSet.data[0])

    # hidden dimension
    H = dataSet.__len__()

    # output dimension.
    D_out = 1
    
    x = Variable(torch.FloatTensor(dataSet.data))
    y = Variable(torch.FloatTensor(dataSet.target), requires_grad=False)

    # Use the nn package to define our model and loss function.
    model = torch.nn.Sequential(
        torch.nn.Linear(D_in, H),
        torch.nn.ReLU(),
        torch.nn.Linear(H, D_out),
    )

    # Use the optim package to define an Optimizer that will update the weights of
    # the model for us. Here we will use Adam; the optim package contains many other
    # optimization algoriths. The first argument to the Adam constructor tells the
    # optimizer which Variables it should update.
    learning_rate = 2e-2
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    
    # do it for 100 epochs
    for t in range(1, 101):
        
        # Forward pass: compute predicted y by passing x to the model.
        y_pred = model(x)

        loss = lossfunction(y_pred, y)
        if not (t % 10):
            print("Step: {0:03d}".format(t), "Loss:", round(loss.data[0], 2))

        # Before the backward pass, use the optimizer object to zero all of the
        # gradients for the variables it will update (which are the learnable weights
        # of the model)
        optimizer.zero_grad()

        # Backward pass: compute gradient of the loss with respect to model
        # parameters
        loss.backward()

        # Calling the step function on an Optimizer makes an update to its
        # parameters
        optimizer.step()
    
    return model

def test(dataSet, model):
    x = Variable(torch.FloatTensor(dataSet.data))
    y = Variable(torch.FloatTensor(dataSet.target), requires_grad=False)

    # compute predicted y by passing the test data to the model.
    y_test = model(x)

    loss = lossfunction(y_test, y)
#     visualize_toy_dataset(dataSet.data, y_test)
#     visualize_toy_dataset(dataSet.data, y)
    print("Test loss:", round(loss.data[0], 2))

tripleDS = ToyDataset("triple_junction_data_training.txt")
tripleDS.visualize()
tripleDSModel = train(tripleDS)

tripleDSTest = ToyDataset("triple_junction_data_test.txt")
# tripleDSTest.visualize()
test(tripleDSTest, tripleDSModel)

spiralDS = ToyDataset("spiral_data_training.txt")
spiralDS.visualize()
spiralDSModel = train(spiralDS)

spiralDSTest = ToyDataset("spiral_data_test.txt")
# spiralDSTest.visualize()
test(spiralDSTest, spiralDSModel)