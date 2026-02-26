class Name:
    def __init__(self, value: str):
        self.value = value

    @property
    def value(self) -> str:
        return self._value
    
    @value.setter
    def value(self, new_value: str):
        if not isinstance(new_value, str):
            raise ValueError("Name must be a string")
        
        if not new_value.strip():
            raise ValueError("Name cannot be empty")
        self._value = new_value

    def __eq__(self, other):
        return isinstance(other, Name) and self.value == other.value