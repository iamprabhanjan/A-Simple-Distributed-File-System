import unittest
from master_node import MasterNode, WorkerNode, Metadata

class TestMasterNode(unittest.TestCase):

    def setUp(self):
        self.master_node = MasterNode()

    def test_register_worker(self):
        worker = WorkerNode("localhost", 5001)
        self.master_node.register_worker(worker)
        self.assertIn(worker, self.master_node.worker_nodes)
        self.assertEqual(len(self.master_node.worker_nodes), 1)

    def test_assign_worker_for_upload(self):
        worker1 = WorkerNode("localhost", 5001)
        worker2 = WorkerNode("localhost", 5002)
        self.master_node.register_worker(worker1)
        self.master_node.register_worker(worker2)
        selected_workers = self.master_node.assign_worker_for_upload("file.txt")
        self.assertEqual(len(selected_workers), 2)  
        self.assertIn(worker1, selected_workers)
        self.assertIn(worker2, selected_workers)

    def test_metadata_update_on_upload(self):
        worker1 = WorkerNode("localhost", 5001)
        worker2 = WorkerNode("localhost", 5002)
        self.master_node.register_worker(worker1)
        self.master_node.register_worker(worker2)
        self.master_node.update_metadata("file.txt", [worker1, worker2])
        self.assertIn("file.txt", self.master_node.metadata)
        self.assertEqual(self.master_node.metadata["file.txt"].locations, [worker1, worker2])

    def test_load_balancing(self):
        worker1 = WorkerNode("localhost", 5001)
        worker2 = WorkerNode("localhost", 5002)
        worker3 = WorkerNode("localhost", 5003)
        self.master_node.register_worker(worker1)
        self.master_node.register_worker(worker2)
        self.master_node.register_worker(worker3)

        
        self.master_node.update_metadata("file1.txt", [worker1])
        self.master_node.update_metadata("file2.txt", [worker2])
        self.master_node.update_metadata("file3.txt", [worker3])

        
        selected_workers = self.master_node.assign_worker_for_upload("file4.txt")
        
        
        worker_loads = [worker.load for worker in self.master_node.worker_nodes]
        self.assertEqual(min(worker_loads), max(worker_loads))

    def test_fault_tolerance(self):
        worker1 = WorkerNode("localhost", 5001)
        worker2 = WorkerNode("localhost", 5002)
        self.master_node.register_worker(worker1)
        self.master_node.register_worker(worker2)
        self.master_node.update_metadata("file.txt", [worker1, worker2])

        
        worker1.fail()
        self.master_node.check_worker_health()

        
        self.assertIn(worker2, self.master_node.metadata["file.txt"].locations)
        self.assertNotIn(worker1, self.master_node.metadata["file.txt"].locations)

if __name__ == "__main__":
    unittest.main()
