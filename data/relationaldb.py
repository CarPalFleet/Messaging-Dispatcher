import json
import os, sys
import pymysql
current_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_path + '/../')
from basedb import BaseDB

class RelationalDB(BaseDB):
    def __init__(self, host_name, database_name, username, password, table_name):
        self._connection = pymysql.connect(host=host_name,
                                          user=username,
                                          password=password,
                                          db=database_name,
                                          cursorclass=pymysql.cursors.DictCursor)

        self._table = table_name

    def add(self, item):
        try:
            sql = "INSERT INTO {} ({}) VALUES('{}')".format("users", 
                                                            ",".join(item.keys()), 
                                                            "', '".join(item.values()))
                                                                
            self._connection.cursor().execute(sql)
            self._connection.commit();
        except Exception as e:
            raise e
        
    def add_batch(self, items):
        pass
        
    def get(self, key, value):
        pass
        
    def get_all(self, filter_key=None, filter_value=None, partial_match=False):
        pass

    def update(self, key, value, update_key, update_value):
        pass

    def delete(self, key, value):
        pass

    def purge(self):
        pass
