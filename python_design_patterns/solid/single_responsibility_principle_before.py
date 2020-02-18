class Burglar:
    def __init__(self):
        self._artifacts = []

    def steal(self, artifact: str) -> None:
        print("Putting on the invisibility cloak.")
        print("Sneaking in.")
        print("Taking the artifact.")
        self._artifacts.append(artifact)
        print("Sneaking out.")
        print("Removing the invisibility cloak.")


if __name__ == "__main__":
    bilbo = Burglar()
    bilbo.steal("Arkenstone")
