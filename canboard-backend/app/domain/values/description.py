class Description:
    def __init__(self, value: str):
        self.value = value

    @property
    def value(self) -> str:
        return self._value
    
    @value.setter
    def value(self, new_value: str):
        if not isinstance(new_value, str):
            raise ValueError("Description must be a string")
        
        if not new_value.strip():
            raise ValueError("Description cannot be empty")
        self._value = new_value

    def __eq__(self, other):
        return isinstance(other, Description) and self.value == other.value