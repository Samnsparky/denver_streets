import unittest
import datetime
import json, os
import os, sys
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parent_dir)
import app
from lib import importer

fixtures_dir = os.getcwd() + "/tests/fixtures"
database = app.database
models = app.models

class ImporterTests(unittest.TestCase):
    def setUp(self):
        # set up test db
        self.closure_json = open(fixtures_dir + '/importer_test_fixtures.txt').read()
        database.init_db()

    def tearDown(self):
        database.drop_db()

    def testImportClosures(self):
        importer.import_closures(self.closure_json)
        self.assertEquals(len(database.session.query(models.Closure).all()), 6)

    # Start time and end time should be 00:00:00 to 11:59:59
    def testImportClosureTime(self):
        importer.import_closures(self.closure_json)
        closure = database.session.query(models.Closure).all()[0]
        self.assertEquals(closure.start_time, datetime.time(0, 0, 0))
        self.assertEquals(closure.end_time, datetime.time(23, 59, 59))

if __name__ == '__main__':
    unittest.main()
