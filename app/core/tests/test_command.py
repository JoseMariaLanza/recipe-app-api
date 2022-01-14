from unittest.mock import patch
# Allows to call the command in our source code
from django.core.management import call_command
# OperationalError that Django throws when the DB is unavailable
from django.db.utils import OperationalError
from django.test import TestCase


class Commandtests(TestCase):

    def test_wait_for_db_ready(self):
        """Test waiting for db when db is available"""
        # Simulating the behavior of Django when the db is available
        # The management command try and retrieve the db connection from Django
        # Then it's going to check when we want to try retrieve an OperationError
        # or not
        # Overriding the behavior of the ConnectionHandler
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            # Side effect
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
