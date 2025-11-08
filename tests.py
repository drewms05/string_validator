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


if __name__ == '__main__':
    unittest.main()
