#! /usr/bin/env python

import os
import subprocess
import multiprocessing
import time

# Setup
path = os.path.realpath(__file__).rstrip(os.path.basename(__file__))


'''
this is the final example
of using it with my neural network.
Know all i have to do is 
save values to the class and then we can
get rolling.
'''
class producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue


        
    def run(self) :

        while(True):
            
            for i in range(10):
                print ("Touch MATRIX Creator IR Sensor")
                process = subprocess.Popen(
                    ['./micarray/build/micarray_dump'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                audio, err = process.communicate()
                #converts the string of mfcc values to
                # a list of mfcc values
                convert = audio.decode("utf-8") 
                convert = eval(''.join(['[',   convert, ']']))

                self.queue.put(convert)
            break;
            
            
class consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue


    def run(self):           
        while True:
            time.sleep(1.2)
            if (self.queue.empty()):
                print("the queue is empty")
                break;
                
            else :
                item = self.queue.get()
                print(item)
                
if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process_producer = producer(queue)
    process_consumer = consumer(queue)
    process_producer.start()
    process_consumer.start()
    process_producer.join()
    process_consumer.join()

