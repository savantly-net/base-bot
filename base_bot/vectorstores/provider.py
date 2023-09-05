from abc import ABC, abstractmethod

class VectorStoreProvider(ABC):
    @abstractmethod
    def get_vectorstore(self, variant: str):
        """
        Abstract method to get a vector store for a given variant.

        Args:
            variant (str): A string representing the variant.

        Returns:
            Any: The vector store for the specified variant.
        """
        pass