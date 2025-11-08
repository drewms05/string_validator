# Nicholas Bryant (bryantn2@oregonstate.edu)
# Nelson Swindell (swindeln@oregonstate.edu)
# Drew Schlabach (schlabad@oregonstate.edu)
# CS 361 Assignment 8
# 11/17/25
# This programs takes a string as input and
# checks it against a series of input parameters.

import zmq

def find_substring(input):
    if input['substring'] in input['input']:
        return True
    else:
        return False

def main():

    # Create socket
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind('tcp://localhost:1234')

    # Continuously check for input
    while True:

        # Recevie input
        input = None
        input = socket.recv_json()
        results = []

        # Perform substring check
        if input['substring']:
            result = find_substring(input)
            if result is False:
                results.append(f'\'{input['substring']}\' not in string')

        # Finalize the results
        if len(results) > 0:
            results.insert(0, 'String is not valid')
            socket.send_json(results)
        else:
            results.append('String is valid')
            socket.send_json(results)

    

if __name__ == '__main__':
    main()
