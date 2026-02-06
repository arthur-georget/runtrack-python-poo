class Part:

    def __init__(self, name: str, material: str):
        if isinstance(name, str):
            self.__name = name
            if isinstance(material, str):
                self.__material = material
            else:
                raise Exception("Part.__init__(): material should be a str.")
        else:
            raise Exception("Part.__init__(): name should be a str.")  

    def change_material(self, new_material: str):
        if isinstance(new_material, str):
            self.__material = new_material
        else:
            raise Exception("Part.__init__(): new_material should be an int.")

    def get_name(self) -> str:
        return self.__name

    def __str__(self) -> str:
        return f"{self.__name} - {self.__material} - Memory address: {hex(id(self))}"