
import unittest
from worker_node import WorkerNode

class TestWorkerNode(unittest.TestCase):

    def setUp(self):
        self.worker = WorkerNode("localhost", 5001)

    def test_store_file(self):
        file_content = b"This is a test file."
        file_name = "test.txt"
        self.worker.store_file(file_name, file_content)
        stored_content = self.worker.retrieve_file(file_name)
        self.assertEqual(stored_content, file_content)

    def test_delete_file(self):
        file_name = "test.txt"
        self.worker.store_file(file_name, b"Content to delete.")
        self.worker.delete_file(file_name)
        self.assertIsNone(self.worker.retrieve_file(file_name))

    def test_handle_overload(self):
        
        for i in range(100):
            self.worker.store_file(f"file_{i}.txt", b"content")
        self.assertRaises(Exception, self.worker.store_file, "file_101.txt", b"content")

    def test_health_check(self):
        self.worker.fail()
        self.assertFalse(self.worker.is_healthy())

        self.worker.recover()
        self.assertTrue(self.worker.is_healthy())

if __name__ == "__main__":
    unittest.main()
