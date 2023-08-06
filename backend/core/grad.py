class Grad:
    """
    Everything that is gradable, and you can determine the level of advancement
    """
    max_level: int

    def __init__(self, name: str, level: int, max_level: int = 5):
        """
        Init values
        :param name: string
        :param level: int
        :param max_level: int - remember that you change it for all instances of this class
        """
        self.name = name
        self.level = level
        Grad.max_level = max_level
