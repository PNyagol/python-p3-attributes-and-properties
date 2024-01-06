class Dog:
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

    def __init__(self, name, breed):
        self._name = name
        self._breed = breed

    def get_name(self):
        print("Retrieving name.")
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            print(f"Setting name to {name}")
            self._name = name.title()
        else:
            print("Name must be a string under 25 characters.")

    def get_breed(self):
        print("Retrieving breed.")
        return self._breed

    def set_breed(self, breed):
        if breed in Dog.APPROVED_BREEDS:
            print(f"Setting breed to {breed}")
            self._breed = breed
        else:
            print("Breed must be in the list of approved breeds.")

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)

fido = Dog(name="Fido", breed="Labrador")
