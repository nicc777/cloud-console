import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
print('sys.path={}'.format(sys.path))

import unittest


from cloud_console import cloud_console


class TestBasicStart(unittest.TestCase):

    def test_basic_launch(self):
        result = cloud_console.start_ui(exit_on_done=False, return_done=True)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, bool)
        self.assertTrue(result)



if __name__ == '__main__':
    unittest.main()
