import os, sys, unittest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../')
from messagingdispatcher.datastream.kinesis import Kinesis
from messagingdispatcher.config import CONFIG

class TestKinesis(unittest.TestCase):
    def setUp(self):
        self._kinesis = Kinesis()

    def test_put_data(self):
       self._kinesis.put_record(stream_name='carpal-dashboard', 
                                 data=b'test', 
                                 key='1')

    def test_get_data(self):
        # self._kinesis.get_records(stream_name='carpal-dashboard', 
        #                           data=b'test', 
        #                           key='1')
        print(self._kinesis.get_records(stream_name='carpal-dashboard'))
