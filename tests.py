# Nicholas Bryant (bryantn2@oregonstate.edu)
# Nelson Swindell (swindeln@oregonstate.edu)
# Drew Schlabach (schlabad@oregonstate.edu)
# CS 361 Assignment 8
# 11/17/25
# This programs tests the functionality of main.py

import unittest
import zmq

# Make sure main.py is running before testing!

class TestStringValidator(unittest.TestCase):

    def test1(self):
        """
        Verifies string without any parameters.
        """
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect('tcp://localhost:1234')
        input = {'input': 'This is a string to be tested'}
        expected = ['String is valid']
        socket.send_json(input)
        results = socket.recv_json()
        self.assertEqual(results, expected)
    
    def test2(self):
        """
        Verifies substring check where substring is part of input string.
        """
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect('tcp://localhost:1234')
        input = {'input': 'This is a string to be tested', 'substring': 'to'}
        expected = ['String is valid']
        socket.send_json(input)
        results = socket.recv_json()
        self.assertEqual(results, expected)

    def test3(self):
        """
        Verifies substring check where substring is part of input string.
        """
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect('tcp://localhost:1234')
        input = {'input': 'This is a string to be tested', 'substring': 'four'}
        expected = ['String is not valid', '\'four\' not in string']
        socket.send_json(input)
        results = socket.recv_json()
        self.assertEqual(results, expected)

    def test4(self):
        """
        Verifies substring check where substring equal to input string.
        """
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect('tcp://localhost:1234')
        input = {'input': 'This is a string to be tested', 'substring': 'This is a string to be tested'}
        expected = ['String is valid']
        socket.send_json(input)
        results = socket.recv_json()
        self.assertEqual(results, expected)

    def test5(self):
        """
        Verifies substring check where substring is empty.
        """
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect('tcp://localhost:1234')
        input = {'input': 'This is a string to be tested', 'substring': ''}
        expected = ['String is not valid', '\'\' not in string']
        socket.send_json(input)
        results = socket.recv_json()
        self.assertEqual(results, expected)

    def test6(self):
        """
        Verifies substring check where substring is longer than input string.
        """
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect('tcp://localhost:1234')
        input = {'input': 'This is a string to be tested', 'substring': 'This is a string to be tested This is a string to be tested'}
        expected = ['String is not valid', '\'This is a string to be tested This is a string to be tested\' not in string']
        socket.send_json(input)
        results = socket.recv_json()
        self.assertEqual(results, expected)

    def test7(self):
        """
        Verifies substring check where substring and input string are empty.
        """
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect('tcp://localhost:1234')
        input = {'input': '', 'substring': ''}
        expected = ['No string provided']
        socket.send_json(input)
        results = socket.recv_json()
        self.assertEqual(results, expected)

    def test8(self):
        """
        Verifies numeric check where the string is strictly numeric.
        """
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect('tcp://localhost:1234')
        input = {'input': '752378524035', 'numeric': 'check'}
        expected = ['String is valid']
        socket.send_json(input)
        results = socket.recv_json()
        self.assertEqual(results, expected)

    def test9(self):
        """
        Verifies numeric check where the string is not strictly numeric.
        """
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect('tcp://localhost:1234')
        input = {'input': '09853085g', 'numeric': 'check'}
        expected = ['String is not valid', 'String is not strictly numeric']
        socket.send_json(input)
        results = socket.recv_json()
        self.assertEqual(results, expected)

    def test10(self):
        """
        Verifies length check where the string is shorter than the minimum.
        """
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect('tcp://localhost:1234')
        input = {'input': '12345', 'min': '6'}
        expected = ['String is not valid', 'String does not meet length requirements']
        socket.send_json(input)
        results = socket.recv_json()
        self.assertEqual(results, expected)

    def test11(self):
        """
        Verifies length check where the string is longer than the maximum.
        """
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect('tcp://localhost:1234')
        input = {'input': '12345', 'max': '4'}
        expected = ['String is not valid', 'String does not meet length requirements']
        socket.send_json(input)
        results = socket.recv_json()
        self.assertEqual(results, expected)

    def test12(self):
        """
        Verifies length check where the string is in between the minimum and the maximum.
        """
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect('tcp://localhost:1234')
        input = {'input': '12345', 'min': '4', 'max': '6'}
        expected = ['String is valid']
        socket.send_json(input)
        results = socket.recv_json()
        self.assertEqual(results, expected)

    def test13(self):
        """
        Verifies length check where the string is the same length as the minimum.
        """
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect('tcp://localhost:1234')
        input = {'input': '12345', 'min': '5'}
        expected = ['String is valid']
        socket.send_json(input)
        results = socket.recv_json()
        self.assertEqual(results, expected)

    def test14(self):
        """
        Verifies length check where the string is the same length as the maximum.
        """
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect('tcp://localhost:1234')
        input = {'input': '12345', 'max': '5'}
        expected = ['String is valid']
        socket.send_json(input)
        results = socket.recv_json()
        self.assertEqual(results, expected)

    def test15(self):
        """
        Verifies length check where the string is the same length as the minimum and the maximum.
        """
        context = zmq.Context()
        socket = context.socket(zmq.REQ)
        socket.connect('tcp://localhost:1234')
        input = {'input': '12345', 'min': '5', 'max': '5'}
        expected = ['String is valid']
        socket.send_json(input)
        results = socket.recv_json()
        self.assertEqual(results, expected)


if __name__ == '__main__':
    unittest.main()
