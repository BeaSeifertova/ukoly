from dataclasses import dataclass


@dataclass
class Item:
    name: str
    price: float

    def __str__(self):
        return (f"{self.name}: {self.price} Kč")


@dataclass
class Pizza(Item):
    ingredients: dict

    def add_extra(self, ingredient, quantity, price_per_ingredient):
        self.ingredients[ingredient] = quantity
        self.price = self.price + quantity * price_per_ingredient

    def __str__(self):
        return f"{self.name} ({self.ingredients}): {self.price} Kč"


margarita = Pizza("Margarita", 189, {"rajčata": 100, "mozarella": 50})
margarita.add_extra("oregano", 10, 2)


@dataclass
class Drink(Item):
    volume: int

    def __str__(self):
        return super().__str__() + f" ({self.volume} ml)"


cola = Drink("Cola", 50, 500)
print(cola)


@dataclass
class Order:
    customer_name: str
    delivery_adress: str
    items: list
    status: str

    def mark_delivered(self):
        self.status = "doručeno"

    def __str__(self):
        return f"Zákazník: {self.customer_name} Adresa: {self.delivery_adress} Položky: {self.items} Stav: {self.status}"


order = Order("Jan Novák", "Pražská 123", [margarita, cola], "nedoručeno")
print(order)


@dataclass
class DeliveryPerson:
    name: str
    phone_number: str
    avaliable: bool
    current_order: Order

    def assign_order(self, order):
        if self.avaliable == True:
            self.current_order.status = "na cestě"

    def complete_delivery(self):
        self.current_order.status = "doručeno"
        self.avaliable = True

    def __str__(self):
        return f"Jmeno: {self.name} Cislo: {self.phone_number} Dostupnost: {self.avaliable} Objednavka: {self.current_order}"


delivery_person = DeliveryPerson("Petr Novotný", "777 888 999", True, order)
delivery_person.assign_order(order)
print(delivery_person)

# Dodání objednávky
delivery_person.complete_delivery()
print(delivery_person)

# Kontrola stavu objednávky po doručení
print(order)
