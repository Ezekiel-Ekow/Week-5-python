# smartphone.py

class Smartphone:
    """
    A class to represent a smartphone.
    """
    def __init__(self, brand: str, model: str, battery_life: int):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours

    def call(self, number: str):
        return f"{self.model} is calling {number}..."

    def browse(self):
        return f"{self.model} is browsing the internet."

    def __str__(self):
        return f"{self.brand} {self.model} with {self.battery_life} hours battery life"


class GamingSmartphone(Smartphone):
    """
    A subclass of Smartphone with gaming-specific features.
    """
    def __init__(self, brand: str, model: str, battery_life: int, gpu: str):
        super().__init__(brand, model, battery_life)
        self.gpu = gpu

    def play_game(self, game: str):
        return f"{self.model} with {self.gpu} is playing {game}!"

    def browse(self):
        # Override to show a gaming focus
        return f"{self.model} is browsing for gaming accessories."

    def __str__(self):
        return super().__str__() + f" and a gaming GPU: {self.gpu}"


# Example usage
phone = Smartphone("Apple", "iPhone 15", 20)
gaming_phone = GamingSmartphone("Asus", "ROG Phone 7", 18, "Adreno 740")

print(phone)
print(phone.call("123-456-7890"))
print(phone.browse())

print(gaming_phone)
print(gaming_phone.play_game("Fortnite"))
print(gaming_phone.browse())
