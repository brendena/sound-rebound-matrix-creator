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
    def __init__(self, getQueue, setQueue):
        multiprocessing.Process.__init__(self)
        self.queueGetNotificationColor = getQueue
        self.queueSetAudio = getQueue = setQueue


        
    def run(self) :

        while(True):
            
            for i in range(10):
                print ("micArray_demp " + str(i))
                if(self.queueGetNotificationColor.empty()):
                    process = subprocess.Popen(
                        ['./micarray/build/micarray_dump', "12", "15", "40"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                else:
                    noifColor = self.queueGetNotificationColor.get()
                    process = subprocess.Popen(
                        ['./micarray/build/micarray_dump', noifColor["red"], noifColor["blue"], noifColor["green"]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                audio, err = process.communicate()
                #converts the string of mfcc values to
                # a list of mfcc values
                convert = audio.decode("utf-8") 
                convert = eval(''.join(['[',   convert, ']']))

                self.queueSetAudio.put(convert)
            break;
            
            
class consumer(multiprocessing.Process):
    def __init__(self, getQueue, setQueue  ):
        multiprocessing.Process.__init__(self)
        self.queueGetAudio = getQueue
        self.queueSetNotificationColor = setQueue


    def run(self):           
        while True:
            time.sleep(1.2)
            if (self.queueGetAudio.empty()):
                print("the queue is empty")
                break;
                
            else :
                item = self.queueGetAudio.get()
                self.queueSetNotificationColor.put({'red': "34",'blue':"14", 'green':"5"})
                print(item)
                
if __name__ == '__main__':
    toClassifiers = multiprocessing.Queue()
    toRaspberryPieQueue = multiprocessing.Queue()
    process_producer = producer(toClassifiers, toRaspberryPieQueue)
    process_consumer = consumer( toRaspberryPieQueue, toClassifiers)
    process_producer.start()
    process_consumer.start()
    process_producer.join()
    process_consumer.join()

