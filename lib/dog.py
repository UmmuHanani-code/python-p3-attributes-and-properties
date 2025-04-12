APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Golden", breed="Beagle"):
        self._name = None
        self._breed = None

        valid_name = isinstance(name, str) and 1 <= len(name) <= 25
        valid_breed = breed in APPROVED_BREEDS

        if not valid_name:
            print("Name must be string between 1 and 25 characters.")
        if not valid_breed:
            print("Breed must be in list of approved breeds.")

        if valid_name and valid_breed:
            self.name = name
            self.breed = breed

    def get_name(self):
        print("Retrieving name.")
        return self._name

    def set_name(self, name):
        self._name = name.title()
        print(f"Setting name to {self._name}")

    name = property(get_name, set_name)

    def get_breed(self):
        print("Retrieving breed.")
        return self._breed

    def set_breed(self, breed):
        self._breed = breed
        print(f"Setting breed to {self._breed}")

    breed = property(get_breed, set_breed)
