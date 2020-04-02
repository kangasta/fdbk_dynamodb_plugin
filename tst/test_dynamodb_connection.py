import os
from unittest import TestCase
import warnings

from unittest.mock import Mock, patch

from fdbk.utils import CommonTest

from fdbk_dynamodb_plugin import ConnectionClass
from fdbk_dynamodb_plugin.utils import *


ENDPOINT_URL = 'http://localhost:8000'


def _create_tables():
    try:
        create_topics_table(endpoint_url=ENDPOINT_URL)
        create_data_table(endpoint_url=ENDPOINT_URL)
    except ResourceWarning:
        pass


def _delete_tables():
    try:
        delete_topics_table(endpoint_url=ENDPOINT_URL)
        delete_data_table(endpoint_url=ENDPOINT_URL)
    except ResourceWarning:
        pass


class DictConnectionCommonTest(CommonTest, TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

        try:
            _create_tables()
        except Exception:
            _delete_tables()
            _create_tables()

        self.C = ConnectionClass(endpoint_url=ENDPOINT_URL)

    def tearDown(self):
        _delete_tables()
