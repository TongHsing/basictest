import unittest

class TestBasic(unittest.TestCase):
    "Show setup and teardown"

    def setUp(self):
        self.a = 1

    def tearDown(self):
        del self.a

    def norun_test_fail(self):
        "This test should fail"
       # assert self.a == 2, "*Expected:%s, *Actual:%s" % (2, self.a)
        self.assertEqual(self.a, 1)

    def test_success(self):
        "This test should fail"
        assert self.a == 1, "*Expected:%s, *Actual:%s" % (1, self.a)
        self.assertEqual(self.a, 1)

    def test_success2(self):
        "This test should fail"
        assert self.a == 1, "*Expected:%s, *Actual:%s" % (1, self.a)
        self.assertEqual(self.a, 1)

    def test_success3(self):
        "This test should fail"
        assert self.a == 1, "*Expected:%s, *Actual:%s" % (1, self.a)
        self.assertEqual(self.a, 1)

    def test_fail(self):
        "This test should fail"
        #assert self.a == 2, "*Expected:%s, *Actual:%s" % (2, self.a)
        #self.assertEqual(self.a, 1)
