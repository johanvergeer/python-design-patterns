class Orc:
    def attack(self, weapon: str) -> None:
        if weapon == "sword":
            print("The orc swings the sword.")
        elif weapon == "bow":
            print("The orc shoots an arrow.")
        else:
            raise ValueError(f"The orc doesn't have a {weapon}")


if __name__ == "__main__":
    azog = Orc()
    azog.attack("sword")
