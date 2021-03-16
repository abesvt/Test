'''
Created on Mar 16, 2021

@author: AB
'''
import unittest
from lib import startApp
import os
import logging


class Test(unittest.TestCase):
    testpath = "C:\\cribl\\assignment\\"
    
    def setUp(self):
        
        logging.basicConfig(filename=self.testpath + 'test.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')
        
        startApp("target", self.testpath)
        startApp("splitter", self.testpath)
        startApp("agent", self.testpath)
        pass


    def tearDown(self):
        pass


    def test_verifyEventsCount(self):
        eventsfile = self.testpath + "events.log"
        if os.path.exists(eventsfile):
            self.assertTrue(True, "Event file generated")
            logging.warning("Event file generated ")
        else: 
            logging.error("Events file is not generated")
        
        count = 0
        fileObj = open(eventsfile, "r")
        fileread = fileObj.read()
        events = fileread.split("This is event number ")
        for event in events:
            event = event.replace("\n","")
            if event.isnumeric(): count += 1
        fileObj.close()
        logging.warning("Events count validation. Actual events count is: " + count.__str__())
        self.assertEqual(count, 1000000, "Events count validation failed! Actual events count is: " + count.__str__())
        


if __name__ == "__main__":
    unittest.main()