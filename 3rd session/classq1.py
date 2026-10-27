
class Character:
    def __init__(self, name, power, health, coins):
        self.name = name
        self.power = power
        self.health = health
        self.coins = coins
        self.level = 1

    def show_info(self):
        print(
            f"{self.name} | Level: {self.level} | "
            f"Power: {self.power} | Health: {self.health} | "
            f"Coins: {self.coins}"
        )

    def is_alive(self):
        return self.health > 0

    def attack(self, other):
        other.health -= self.power
        print(
            f"{self.name} attacked {other.name}. "
            f"{other.name}'s health: {other.health}"
        )

    def earn_coins(self, amount):
        self.coins += amount

    def buy_potion(self):
        if self.coins >= 20:
            self.coins -= 20
            self.health += 30
            print(
                f"{self.name} bought a potion. "
                f"Health: {self.health}, Coins: {self.coins}"
            )
        else:
            print("Not enough coins")

    def level_up(self):
        self.level += 1
        self.power += 5
        print(
            f"{self.name} reached level {self.level}. "
            f"New power: {self.power}"
        )


# Testing
arya = Character("Arya", 10, 100, 50)
bran = Character("Bran", 8, 100, 30)

arya.attack(bran)
bran.attack(arya)
arya.attack(bran)
bran.attack(arya)

arya.buy_potion()
bran.level_up()

print("\n--- Final Character Info ---")
arya.show_info()
bran.show_info()

print("\nIs Arya alive?", arya.is_alive())
print("Is Bran alive?", bran.is_alive())
