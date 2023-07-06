
class ColorPicker:
    @staticmethod
    def select(color: str):
        if color == "Bronze":
            return "CD7F32"
        elif color == "Silver":
            return "C0C0C0"
        elif color == "Gold":
            return "ffd700"
        elif color == "Platinum":
            return "e5e4e2"
        elif color == "Diamond":
            return "b9f2ff"
        elif color == "Master":
            return "294dc4"
        elif color == "Predator":
            return "FF0000"
        else:
            return "FFFFFF"
