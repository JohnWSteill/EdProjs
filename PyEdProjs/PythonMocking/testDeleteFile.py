from deleteFile import rm

import os.path
import tempfile
import unittest
import mock


class RmTestCase(unittest.TestCase):
    tmpfilepath = os.path.join(tempfile.gettempdir(),"tmp_testfile")

    def setUp(self):
        with open(self.tmpfilepath,"wb") as f:
            f.write("Delete Me!")

    def test_rm(self):
        rm(self.tmpfilepath)
        self.assertFalse(os.path.isfile(self.tmpfilepath), 
                         "Failed to remove File")

class MockRM(unittest.TestCase):
    @mock.patch('deleteFile.os.path')
    @mock.patch('deleteFile.os')
    def test_rm(self,mock_os,mock_path):
        rm("any path")
        self.assertFalse(mock_os.remove.assert_called_with("any path"))
        mock_path.isfile.return_value = True
        rm("any path")
        mock_os.remove.assert_called_with("any path")

if __name__ == "__main__": unittest.main()
