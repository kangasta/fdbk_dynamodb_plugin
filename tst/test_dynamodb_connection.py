import os
from unittest import TestCase
import warnings

from unittest.mock import Mock, patch

from fdbk.utils import CommonTest

from fdbk_dynamodb_plugin import ConnectionClass
from fdbk_dynamodb_plugin.utils import *


AWS_KWARGS = dict(
    endpoint_url='http://localhost:8000',
    region_name='eu-central-1',
    aws_access_key_id='ACCESS_KEY',
    aws_secret_access_key='SECRET_KEY')

def _create_tables():
    try:
        create_topics_table(**AWS_KWARGS)
        create_data_table(**AWS_KWARGS)
    except ResourceWarning:
        pass


def _delete_tables():
    try:
        delete_topics_table(**AWS_KWARGS)
        delete_data_table(**AWS_KWARGS)
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

        self.C = ConnectionClass(**AWS_KWARGS)

    def tearDown(self):
        _delete_tables()
