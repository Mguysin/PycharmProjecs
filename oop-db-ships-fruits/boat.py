class Boat():
    def __init__(self, name, current_location = '', destination = ''):
        self.name = name
        self.current_location = current_location
        self.destination = destination
        self.cargo_list = []

    def sail(self):
        print("whoooho im sailing somewhere nice")
        print(f"sailing from {self.current_location} to {self.destination}")

    def add_cargo(self, cargo):
        self.cargo_list.append(cargo)

    def print_cargo_list(self):
        for cargo in self.cargo_list:
            print(">", cargo.type_of_fruit, "-", cargo.kg_of_fruit, "tones")

