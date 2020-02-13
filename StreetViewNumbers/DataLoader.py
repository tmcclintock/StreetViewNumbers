import numpy as np
from scipy.io import loadmat

class DataLoader(object):
    def __init__(
            self,
            input_path = "/Users/tmcclintock/Github/StreetViewNumbers/data/"):
        self._input_path = input_path

    def load_training_data(self, fname = "train_32x32.mat"):
        training_dataset = loadmat(
            self._input_path + fname)
        train_X = training_dataset['X']
        train_y = np.squeeze(training_dataset['y'])
        train_X = np.moveaxis(train_X, -1, 0) / 255.
        return train_X, train_y

    def load_testing_data(self, fname = "test_32x32.mat"):
        test_dataset = loadmat(
            self._input_path + fname)
        test_X = test_dataset['X']
        test_y = np.squeeze(test_dataset['y'])
        test_X = np.moveaxis(test_X, -1, 0) / 255.
        return test_X, test_y
