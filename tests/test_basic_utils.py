import unittest
from utils.basic_utils import req_parser, generate_url


class testBasicUtils(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_generate_url(self):
        test_url = "http://localhost:5000/employee/companies/pwc?cursor=page0"
        self.assertEqual(generate_url(test_url, 'page1'), "http://localhost:5000/employee/companies/pwc?cursor=page1")


    def test_req_parser(self):
        pass


if __name__ == "__main__":
    unittest.main()