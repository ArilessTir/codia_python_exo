import unittest

from hello_world import helloWorld

class HelloWorldTestCase(unittest.TestCase):
    def test_hello_world_return(self):
        self.assertEqual(helloWorld(),'Hello World!')

if __name__ == "__main__":
    unittest.main()