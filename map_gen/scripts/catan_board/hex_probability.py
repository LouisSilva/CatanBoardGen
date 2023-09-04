class ProbabilityNumberInvalid(Exception):
    pass

class HexProb:
    def __init__(self, probability_number: int) -> None:

        # Check if the number given is valid
        if (probability_number < 2 and probability_number != 0) or probability_number > 12:
            raise ProbabilityNumberInvalid("The probability number: '{probability_number}' is invalid. Valid numbers are 0, 2-12")
        
        else:
            self.__probability_number = probability_number

        if probability_number == "6" or probability_number == "8":
            self.__pips = "....."
        elif probability_number == "5" or probability_number == "9":
            self.__pips = "...."
        elif probability_number == "4" or probability_number == "10":
            self.__pips = "..."
        elif probability_number == "3" or probability_number == "11":
            self.__pips = ".."
        elif probability_number == "2" or probability_number == "12":
            self.__pips = "."

    @property
    def num(self) -> int:
        return self.__probability_number
    
    @property
    def pips(self) -> str:
        return self.__str__()
    
    def __str__(self) -> str:
        return self.__pips
