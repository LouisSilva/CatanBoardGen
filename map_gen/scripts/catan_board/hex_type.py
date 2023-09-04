class ResourceUnknown(Exception):
    pass


class HexType:
    """An object that represents the resource type of a hex"""

    def __init__(self, resource: str) -> None:
        # Check if the inputted type is valid
        self.set_resource(resource)
        
    def __str__(self) -> str:
        return self.__resource

    @property
    def resource(self) -> str:
        return self.__str__()
    
    def set_resource(self, resource: str) -> None:
        resource = resource.lower()
        
        if resource == "s" or resource == "sheep":
            self.__resource = "sheep"

        elif resource == "w" or resource == "wood":
            self.__resource = "wood"

        elif resource == "o" or resource == "ore":
            self.__resource = "ore"

        elif resource == "g" or resource == "grain":
            self.__resource = "grain"

        elif resource == "b" or resource == "brick":
            self.__resource = "brick"

        elif resource == "d" or resource == "desert":
            self.__resource = "desert"

        else:
            raise ResourceUnknown(f"The resource inputted: '{resource}' is unknown.")
