import json
from elasticsearch import Elasticsearch as ES

class ElasticSearchDocumentModel(object):
    def __init__(self, index, doc_type, doc_id, body):
        self.index = index
        self.doc_type = doc_type
        self.doc_id = doc_id
        self.body = body

    @property
    def index(self):
        return self.index

    @property
    def doc_type(self):
        return self.doc_type
    
    @property
    def doc_id(self):
        return self.doc_id

    @property
    def body(self):
        return self.body

    def to_json(self):
        self.__dict__

    def to_str(self):
        json.dumps(self.__dict__)

class Search(obejct):
    def __init__(self):
        pass

    def put_document(self, doc):
        raise NotImplementedError

class ElasticSearch(Search):
    def __init__(self, host):
        self._client = ES(hosts=[host], use_ssl=True, ca_certs=certifi.where())

    def put_document(self, doc):
        self._client.create(index=doc.index,
                            doc_type=doc.doc_type,
                            id=doc.doc_id,
                            body=doc.body)