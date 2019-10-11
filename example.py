import unittest

class example1(unittest,TestCase):
    def setup(self):
        print "Test1"

    def search_in_python_org(self):
        print "Test2"

    def tearDown(self):
        print "Test3"



if __name__=="_main_":
    unittest.main()
