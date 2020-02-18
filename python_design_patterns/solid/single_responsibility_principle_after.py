class Burglar:
    def __init__(self):
        self._artifacts = []

    def cloak(self):
        print("Putting on the invisibility cloak.")

    def sneak_in(self) -> None:
        print("Sneaks towards the artifact")

    def sneak_out(self) -> None:
        print("Sneaks back")

    def remove_cloak(self) -> None:
        print("Removing the invisibility cloak.")

    def steal(self, artifact: str) -> None:
        print("Taking the artifact.")
        self._artifacts.append(artifact)


if __name__ == "__main__":
    bilbo = Burglar()

    bilbo.cloak()
    bilbo.sneak_in()
    bilbo.steal("Arkenstone")
    bilbo.sneak_out()
    bilbo.remove_cloak()
