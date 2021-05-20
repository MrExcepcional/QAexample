import os
form unittest import TestCase

SCREEN_DUMP_LOCATION = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'screendumps'
)

class FunctionalTest(TestCase):

    def setUp(self):
        pass