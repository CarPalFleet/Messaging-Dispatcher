import os, pymysql, sys, unittest
from boto3 import resource
from botocore.exceptions import ClientError
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../')
from data.basedb import DBModelMixin
from data.relationaldb import RelationalDB
import unittest

class TestDynamoDB(unittest.TestCase):
    """ Test Class for RelationalDB """

    def setUp(self):
        self._relational_db = RelationalDB("users",
                                           DBModelMixin,
                                           "aldryndbinstance.cluwsec6wqyi.ap-southeast-1.rds.amazonaws.com",
                                           "testingdb",
                                           "aldryn",
                                           "mypassword")

        self._connection = pymysql.connect(host="aldryndbinstance.cluwsec6wqyi.ap-southeast-1.rds.amazonaws.com",
                                           user="aldryn",
                                           password="mypassword",
                                           db="testingdb",
                                           cursorclass=pymysql.cursors.DictCursor)

    def tearDown(self):
        self._connection.close()

    def create_db_model_mixin(self, name):
        db_model = DBModelMixin()
        db_model.name = name
        return db_model

    def test_add_success(self):
        # Create record to insert
        db_model = self.create_db_model_mixin('Aardvark')

        # Trigger add in RelationalDB
        self._relational_db.add(db_model)

        # Check that there is only one inserted record
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users WHERE name = '{}'".format(db_model.name))

        self.assertEqual(1, cursor.rowcount)

        # Clear Users Table
        cursor.execute("TRUNCATE users")

    def test_add_throw_type_error(self):
        # Trigger add in RelationalDB with invalid allowed type
        with self.assertRaises(TypeError):
            self._relational_db.add([1, 2, 3])

    def test_add_throw_exception(self):
        # Create record to insert with empty object of the allowed type
        with self.assertRaises(Exception):
            self._relational_db.add(DBModelMixin())

if __name__ == '__main__':
    unittest.main()