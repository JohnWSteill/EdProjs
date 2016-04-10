from removal_service import RemovalService, UploadService

import unittest
import mock

class RemovalServiceTestCase(unittest.TestCase):
    @mock.patch('removal_service.os.path')
    @mock.patch('removal_service.os')
    def test_rm(self,mock_os,mock_path):
        ref = RemovalService()
        mock_path.isfile.return_value = False
        ref.rm("any path")
        self.assertFalse(mock_os.remove.called, "failed to not remove.")
        
        mock_path.isfile.return_value = True
        ref.rm("any path")
        mock_os.remove.assert_called_with("any path")

class UploadServiceTestCase(unittest.TestCase):
    # There are two ways to test UploadService's calls of RemovalService with
    # out (re) testing Removal Service:
        # 1) Mock out RemovalService.rm method itself
        # 2) Supply a mocked instance in constructor of UploadService

    # To mock object instance method: @mock.patch.object
    @mock.patch.object(RemovalService,'rm')
    def testUploader(self,mock_rm):
        ref = UploadService(RemovalService())
        ref.upload_complete("any path")
        mock_rm.assert_called_with("any path") # any removal service

        remSvRef = RemovalService()
        ref = UploadService(remSvRef)
        ref.upload_complete("any path")
        remSvRef.rm.assert_called_with("any path") # OUR rem sv
    
# To supply a mocked instance with constructor:
class UploadSvTestCase2(unittest.TestCase):
    def testU(self):
        mock_removal_service = mock.create_autospec(RemovalService)
        ref = UploadService(mock_removal_service)
        ref.upload_complete("any file")
        mock_removal_service.rm.assert_called_with("any file")


if __name__ == "__main__": unittest.main()
