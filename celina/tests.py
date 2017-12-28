from unittest.mock import patch
from django.test import TestCase
from .tasks import add_history, add_history_bulk

class AddHistoryTestCase(TestCase):

    @patch('celina.tasks.History.objects.create')
    def test_success(self, history_create):
        add_history()
        history_create.assert_called()
        assert(history_create.call_count == 100)

    @patch('celina.tasks.History.objects.bulk_create')
    @patch('celina.tasks.History.objects.create')
    def test_success_bulk(self, history_create, bulk):
        add_history_bulk()
        history_create.assert_not_called()
        bulk.assert_called_once()
