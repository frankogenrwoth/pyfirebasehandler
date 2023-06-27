import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class FirebaseHandler:
    def __init__(self, credentials_path):
        # Initialize Firebase credentials
        if not firebase_admin._apps:
            cred = credentials.Certificate(credentials_path)
            firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def create_document(self, collection_path, document_data, custom_ref=""):
        """
        Creates a new document in the specified collection.
        Args:
            collection_path (str): The name of the collection or path to the collection i.e. 'Userdata/user01/Initials' but must be odd.
            document_data (dict): The data to be stored in the document.
        Returns:
            str: The ID of the newly created document.
        """

        collection_ref = self.db.collection(collection_path)
        if custom_ref != "":
            doc_ref = collection_ref.document(custom_ref)
            doc_ref.set(document_data)
        else:
            update_time, doc_ref = collection_ref.add(document_data)
        return doc_ref.id

    def get_document(self, collection_path, document_id):
        """
        Retrieves a document from the specified collection.
        Args:
            collection_path (str): The name of the collection.
            document_id (str): The ID of the document to retrieve.
        Returns:
            dict: The data stored in the retrieved document.
        """
        collection_ref = self.db.collection(collection_path)
        doc_ref = collection_ref.document(document_id)
        return doc_ref.get().to_dict()

    def update_document(self, collection_path, document_id, updated_data):
        """
        Updates a document in the specified collection.
        Args:
            collection_path (str): The name of the collection.
            document_id (str): The ID of the document to update.
            updated_data (dict): The updated data to be stored in the document.
        """
        collection_ref = self.db.collection(collection_path)
        doc_ref = collection_ref.document(document_id)
        doc_ref.update(updated_data)

    def delete_document(self, collection_path, document_id):
        """
        Deletes a document from the specified collection.
        Args:
            collection_path (str): The name of the collection.
            document_id (str): The ID of the document to delete.
        """
        collection_ref = self.db.collection(collection_path)
        doc_ref = collection_ref.document(document_id)
        doc_ref.delete()

    def readCollection(self, collection_path):
        docs = self.db.collection(collection_path).stream()

        collection_data_list = list()
        for doc in docs:
            collection_data_list.append(doc.to_dict())

        return collection_data_list
