import os, sys, unittest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../')
from messagingdispatcher.search.esclient import ElasticSearchDocumentModel

class TestElasticSearch(unittest.TestCase):
    def setUp(self):
        self._new_doc = ElasticSearchDocumentModel(index='order', 
                                                   doc_type='default', 
                                                   doc_id='1', 
                                                   body={
                                                        "id": 14,
                                                        "customer_id": 35,
                                                        "order_status_id": 1,
                                                        "order_status_name": "Pending",
                                                        "pickup_date_time": "2015-11-28 16:30",
                                                        "driver_id": 0,
                                                        "driver_name": ""
                                                    })

     def test_document_model(self):
         self.assertEqual(self._new_doc.index, 'order')
         self.assertEqual(self._new_doc.doc_type, 'default')
         self.assertEqual(self._new_doc.doc_id, '1')