

import random
import numpy as np
from scipy import misc
import handwriting_test1

class Testing(object):




    def __init__(self, biases, weights, drawn_image):
        """The list ``sizes`` contains the number of neurons in the
        respective layers of the network.  For example, if the list
        was [2, 3, 1] then it would be a three-layer network, with the
        first layer containing 2 neurons, the second layer 3 neurons,
        and the third layer 1 neuron. """
        self.biases = biases
        self.weights = weights
        """self.drawn_image = test_data[number][0]"""
        self.drawn_image = misc.imread("drawn_img.png")
        print self.drawn_image[0]


    def test(self):
        self.image = np.reshape(self.drawn_image, (784, 1))
        self.image1 =[]
        for x in self.image:
                self.image1.append(float(x)/255)
        self.image1 = np.reshape(self.image1, (784, 1))
        print self.image1
        """self.image2 = np.reshape(self.image1,(28,28))
        print self.image1"""
        print ('I guess it is {0}'.format(np.argmax(self.feedforward(self.image1))))


        """print ('I guess it is {0}'.format(x))"""



    def feedforward(self, a):
        """Return the output of the network if ``a`` is input."""
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a)+b)
            """ numpy.dot is the multiplication of w and a"""
        return a






def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))


def sigmoid_prime(z):
    """Derivative of the sigmoid function."""
    return sigmoid(z)*(1-sigmoid(z))
