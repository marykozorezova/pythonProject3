# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов,
# которые также являются свойствами экземпляра.

class Archive:
    def __init__(self, s, i):
        self.number_history = None
        self.text_history = None

    """
    Создайте класс Архив, который хранит пару свойств. Например, число и строку.
При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов,
которые также являются свойствами экземпляра.
"""
instance = None

def __new__(cls, *args, **kwargs):
# применение свойств для класса
    if cls.instance is None:
        cls.instance = super().__new__(cls)
        cls.instance.text_history = []
        cls.instance.number_history = []
    else:
        cls.instance.text_history.append(cls.instance.text)
        cls.instance.number_history.append(cls.instance.number)
    return cls.instance

def __init__(self, text: str, number: int):
    self.text = text
    self.number = number

def __str__(self) -> str:
    return f"now {self.text}, now {self.number}, arhiv_text {self.text_history}, arhiv_num {self.number_history}"

def __repr__(self) -> str:
    return f"Arhive({self.text}, {self.number})"


a = Archive("vdhvdv", 5)
print(a.text_history, a.number_history)
b = Archive("gdvbdrjfrvb", 5)
print(b.text_history, b.number_history)
print(a.text_history, a.number_history)
print(Archive.__doc__)
print(repr(b))