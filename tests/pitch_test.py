import unittest
from app.models import Pitch
Pitch = Pitch
from app import db

class PitchTest(unittest.TestCase):
    def setUp(self):
        sels.new_pitch = Pitch('test all new_pitch')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,))