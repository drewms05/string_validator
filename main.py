# Nicholas Bryant (bryantn2@oregonstate.edu)
# Nelson Swindell (swindeln@oregonstate.edu)
# Drew Schlabach (schlabad@oregonstate.edu)
# CS 361 Assignment 8
# 11/17/25
# This programs takes a string as input and
# checks it against a series of input parameters.

import zmq


def find_substring(input):
    """
    Find a substring within a string.

    Returns True if substring is present in string,
    otherwise returns False.
    """
    # Handle empty substring
    if input['substring'] == '':
        return False

    # Check for substring in string
    if input['substring'] in input['input']:
        return True
    else:
        return False


def numeric_check(input):
    """
    Check if a string is strictly numeric.

    Returns True if the string can be converted
    to an integer value, otherwise returns False.
    """
    # Attempt to convert the string to an int
    for character in input['input']:
        try:
            int(character)
        except ValueError:
            return False


def length_check(input):
    """
    Check if a string in below or above a given min and max value.

    Returns True if the length of the string is larger than
    a given min, and/or smaller than a given max, otherwise returns False.
    """
    try:
        # Check the string length against min and/or max
        str_len = len(input['input'])
        min = int(input['min']) if 'min' in input else None
        max = int(input['max']) if 'max' in input else None
        if ('min' in input and min > str_len) or ('max' in input and max < str_len):
            return False
        else:
            return True
    except KeyError:
        return False


def check_input(input, method, message, results):
    """
    Perform a check on the input string.

    Runs a different check depending on the given
    method, and appends a failure message to results if necessary.
    """
    result = method(input)
    if result is False:
        results.append(message)


def create_socket():
    """
    Create a ZeroMQ socket that the client can connect to.
    """
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind('tcp://localhost:1234')
    return socket


def send_results(socket, results):
    """
    Send the results to the client through a ZeroMQ connection.
    """
    # Insert an error message at the beginning of results
    # if any of the checks failed
    if len(results) > 0:
        results.insert(0, 'String is not valid')
        socket.send_json(results)
    # Insert a success message at the beginning of results
    # if none of the checks failed
    else:
        results.append('String is valid')
        socket.send_json(results)


def perform_checks(input, results):
    """
    Perform the necessary checks on the input string.
    """
    # Perform substring check
    if 'substring' in input:
        check_input(input, find_substring,
                    f'\'{input['substring']}\' not in string', results)
    # Perform numeric check
    if 'numeric' in input:
        check_input(input, numeric_check,
                    'String is not strictly numeric', results)
    # Perform length check
    if 'min' in input or 'max' in input:
        check_input(input, length_check,
                    'String does not meet length requirements', results)


def main():
    """
    Wait for input and return output.
    """
    socket = create_socket()

    # Continuously check for input
    while True:

        # Receive input
        input = socket.recv_json()
        results = []

        # Quit early if no string is provided
        if input['input'] == '':
            results.append('No string provided')
            socket.send_json(results)
            continue

        # Perform checks
        perform_checks(input, results)

        # Finalize the results
        send_results(socket, results)


if __name__ == '__main__':
    main()
