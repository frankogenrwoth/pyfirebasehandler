import unittest
from pyfirebasehandler.firebase_handler import FirebaseHandler


class FirebaseHandlerTestCase(unittest.TestCase):
    def setUp(self):
        # Initialize FirebaseHandler with test credentials
        credentials_path = 'test_db/test_db.json'
        self.handler = FirebaseHandler(credentials_path)

    def tearDown(self):
        # Clean up any test data in the Firebase database
        # (e.g., delete test documents)
        pass

    def test_create_document(self):
        collection_name = 'test_collection'
        document_data = {'name': 'John Doe', 'age': 30}
        document_id = self.handler.create_document(collection_name, document_data)

        # Check if document was created successfully
        self.assertIsNotNone(document_id)

    def test_get_document(self):
        collection_name = 'test_collection'
        document_data = {'name': 'John Doe', 'age': 30}
        document_id = self.handler.create_document(collection_name, document_data)

        # Retrieve the created document
        retrieved_data = self.handler.get_document(collection_name, document_id)

        # Check if retrieved data matches the original data
        self.assertEqual(retrieved_data, document_data)

    def test_update_document(self):
        collection_name = 'test_collection'
        document_data = {'name': 'John Doe', 'age': 30}
        document_id = self.handler.create_document(collection_name, document_data)

        # Update the document
        updated_data = {'age': 31}
        self.handler.update_document(collection_name, document_id, updated_data)

        # Retrieve the updated document
        retrieved_data = self.handler.get_document(collection_name, document_id)

        # Check if the document was updated successfully
        self.assertEqual(retrieved_data['age'], updated_data['age'])

    def test_delete_document(self):
        db = self.handler
        collection_name = 'test_collection'
        document_data = {'name': 'John Doe', 'age': 30}
        document_id = db.create_document(collection_name, document_data)

        # Delete the document
        db.delete_document(collection_name, document_id)

        # Try to retrieve the deleted document
        retrieved_data = self.handler.get_document(collection_name, document_id)

        # Check if the document was deleted successfully
        self.assertIsNone(retrieved_data)


if __name__ == '__main__':
    unittest.main()
