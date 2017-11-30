import logging, mock, os, sys, unittest
from ably import AblyRest
from ably.util.exceptions import AblyAuthException, AblyException
from ably.rest.channel import Channel
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_path + '/../') 
from data.ablyservice import AblyService
import unittest

class TestAblyService(unittest.TestCase):
    """ Test Class for AblyService """

    def test_init_throw_exception(self):
        """ Test ensures invalid API Key will throw an Ably Authentication Exception """
        logging.disable(logging.ERROR)
        with self.assertRaises(AblyAuthException):
            AblyService('123')

    def test_init_success(self):
        """ Test ensures proper api key format will instantiate an AblyRest Object """
        ablyservice = AblyService('zEkI4A.ndGQtw:kDKYDEpWrryXn67W')
        self.assertIsInstance(ablyservice._client, AblyRest)

    def test_publish_throw_exception(self):
        """ Test ensures publish throws an Ably Exception on invalid input """
        logging.disable(logging.ERROR)
        with self.assertRaises(AblyException):
            ablyservice = AblyService('zEkI4A.ndGQtw:kDKYDEpWrryXn67W')
            ablyservice.publish('order.mocked', {1, 2, 3}, '300')

    @mock.patch('data.ablyservice.Channels.get')
    def test_publish_success(self, channels_method):
        """ Test ensures that publish is triggered with correct argument """
        ablyservice = AblyService('123:123')
        ablyservice.publish('a', 'b', 'c')
        channels_method.assert_called_with('a')

if __name__ == '__main__':
    unittest.main()