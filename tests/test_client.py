
import unittest
from client import Client
from master_node import MasterNode
from worker_node import WorkerNode

class TestClient(unittest.TestCase):

    def setUp(self):
        self.master_node = MasterNode()
        self.worker1 = WorkerNode("localhost", 5001)
        self.worker2 = WorkerNode("localhost", 5002)
        self.master_node.register_worker(self.worker1)
        self.master_node.register_worker(self.worker2)
        self.client = Client(self.master_node)

    def test_upload_file(self):
        response = self.client.upload_file("example.txt", b"Example content.")
        self.assertIn("File uploaded successfully", response)

        
        self.assertIn("example.txt", self.worker1.files)
        self.assertIn("example.txt", self.worker2.files)

    def test_download_file(self):
        self.client.upload_file("example.txt", b"Example content.")
        content = self.client.download_file("example.txt")
        self.assertEqual(content, b"Example content.")

    def test_delete_file(self):
        self.client.upload_file("example.txt", b"Example content.")
        response = self.client.delete_file("example.txt")
        self.assertIn("File deleted successfully", response)

        
        self.assertNotIn("example.txt", self.worker1.files)
        self.assertNotIn("example.txt", self.worker2.files)

    def test_consistency_mechanism(self):
        
        self.client.upload_file("example.txt", b"Example content.")
        self.worker1.store_file("example.txt", b"Old content.")

        
        content = self.client.download_file("example.txt")
        self.assertEqual(content, b"Example content.")

if __name__ == "__main__":
    unittest.main()
