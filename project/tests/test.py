import unittest
from project import app


class ProjectTests(unittest.TestCase):
    # setup and teardown
    # executed prior to each test

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.assertEquals(app.debug, False)

    def tearDown(self):
        pass

    # tests
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b'Welcome to the Flask Hubble project!', response.data)
        self.assertIn(b'This site is a template to your web project.', response.data)
        self.assertIn(b'Python', response.data)
        self.assertIn(b'Flask', response.data)
        self.assertIn(b'HTML', response.data)
        self.assertIn(b'CSS', response.data)


if __name__ == "__main__":
    unittest.main()