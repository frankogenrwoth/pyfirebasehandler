import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class FirebaseHandler:
    def __init__(self, credentials_path):
        # Initialize Firebase credentials
        cred = credentials.Certificate(credentials_path)
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def create_document(self, collection_name, document_data):
        """
        Creates a new document in the specified collection.
        Args:
            collection_name (str): The name of the collection.
            document_data (dict): The data to be stored in the document.
        Returns:
            str: The ID of the newly created document.
        """
        collection_ref = self.db.collection(collection_name)
        doc_ref = collection_ref.add(document_data)
        return doc_ref.id

    def get_document(self, collection_name, document_id):
        """
        Retrieves a document from the specified collection.
        Args:
            collection_name (str): The name of the collection.
            document_id (str): The ID of the document to retrieve.
        Returns:
            dict: The data stored in the retrieved document.
        """
        collection_ref = self.db.collection(collection_name)
        doc_ref = collection_ref.document(document_id)
        return doc_ref.get().to_dict()

    def update_document(self, collection_name, document_id, updated_data):
        """
        Updates a document in the specified collection.
        Args:
            collection_name (str): The name of the collection.
            document_id (str): The ID of the document to update.
            updated_data (dict): The updated data to be stored in the document.
        """
        collection_ref = self.db.collection(collection_name)
        doc_ref = collection_ref.document(document_id)
        doc_ref.update(updated_data)

    def delete_document(self, collection_name, document_id):
        """
        Deletes a document from the specified collection.
        Args:
            collection_name (str): The name of the collection.
            document_id (str): The ID of the document to delete.
        """
        collection_ref = self.db.collection(collection_name)
        doc_ref = collection_ref.document(document_id)
        doc_ref.delete()
