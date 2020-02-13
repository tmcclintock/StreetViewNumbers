import numpy as np

import tensorflow as tf
import tensorflow.keras as tfk
import tensorflow.keras.layers as tfkl
import tensorflow.keras.models as tfkm

class SVN(tfkm.Sequential):
    def __init__(self):
        super(SVN, self).__init__()

        #Shapes of the input images
        M, N = 32, 32
        self.dims = [M, N]
        
        self.add_network()
        return

    def add_network(self):
        M, N = self.dims
        self.add(tfkl.Conv2D(32, (3, 3), activation='relu', input_shape=(M, N, 3)))
        self.add(tfkl.MaxPooling2D((2, 2)))
        self.add(tfkl.Conv2D(64, (3, 3), activation='relu'))
        self.add(tfkl.MaxPooling2D((2, 2)))
        self.add(tfkl.Conv2D(64, (3, 3), activation='relu'))
        return
