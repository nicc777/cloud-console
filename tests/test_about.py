import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
print('sys.path={}'.format(sys.path))

import unittest


from cloud_console import cloud_console


class TestStringMethods(unittest.TestCase):

    def test_print_about_function(self):
        result = cloud_console.print_about(print_to_console=False, return_text=True)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)
        self.assertTrue('Cloud Console' in result)



if __name__ == '__main__':
    unittest.main()
