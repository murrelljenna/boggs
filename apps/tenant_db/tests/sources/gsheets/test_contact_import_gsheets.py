from django.test import Client

from apps.tenant_db.models import Gsheets_Contact

from hypothesis import given, settings
import hypothesis.strategies as st
import random
from hypothesis.extra.django import TestCase, from_model

class ContactImportGsheetsTest(TestCase):
    def test_something(self):
        Gsheets_Contact.pull_sheet()
