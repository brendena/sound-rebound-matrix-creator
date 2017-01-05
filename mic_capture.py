#! /usr/bin/env python

import os
import subprocess

# Setup
path = os.path.realpath(__file__).rstrip(os.path.basename(__file__))





def start():
    print "Touch MATRIX Creator IR Sensor"
    process = subprocess.Popen(
        ['./micarray/build/micarray_dump'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    audio, err = process.communicate()

    rf = open(path + 'recording.wav', 'w')
    rf.write(audio)
    rf.close()



if __name__ == "__main__":
    print "This is a MATRIX Creator demo - not ready for production"  
    start()
