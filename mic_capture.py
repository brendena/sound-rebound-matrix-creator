#! /usr/bin/env python

import os
import subprocess

# Setup
path = os.path.realpath(__file__).rstrip(os.path.basename(__file__))


queue = []


def start():
    print ("Touch MATRIX Creator IR Sensor")
    process = subprocess.Popen(
        ['./micarray/build/micarray_dump'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    audio, err = process.communicate()
    print(audio)
    #converts the string of mfcc values to
    # a list of mfcc values
    convert = eval('[' + audio +']')
    print(convert)
    queue.append(convert)
    #rf = open(path + 'recording.wav', 'w')
    #rf.write(audio)
    #rf.close()



if __name__ == "__main__":
    for i in range(2):
        print ("This is a MATRIX Creator demo - not ready for production" )
        start()
    print(queue)
