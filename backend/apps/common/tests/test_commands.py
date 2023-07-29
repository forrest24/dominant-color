from unittest.mock import patch

from psycopg2 import OperationalError

from django.core.management import call_command
from django.test import SimpleTestCase


class CommandTests(SimpleTestCase):

    @patch('apps.common.management.commands.wait_for_db.Command.check')
    def test_wait_for_db(self, check_mock):
        check_mock.return_value = True
        call_command('wait_for_db')
        check_mock.assert_called_once()

    @patch('apps.common.management.commands.wait_for_db.Command.check')
    def test_wait_for_db_delay(self, check_mock):
        check_mock.side_effect = [OperationalError] * 2 + [True]
        call_command('wait_for_db')
        self.assertEquals(check_mock.call_count, 3)
