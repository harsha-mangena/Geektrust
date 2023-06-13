class Stock:
    def __init__(self, name:str) -> None:
        """
        Initializes an instance of the class with the given name.

        :param name: The name to be assigned to the instance.
        :type name: Any
        :return: None
        """
        self._name = name
    
    def get_stock_name(self) -> str:
        return self._name