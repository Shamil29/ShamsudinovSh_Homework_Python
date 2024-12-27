from smartphone import Smartphone

catalog = [
    Smartphone("iPhone", "13", "+79856658956"),
    Smartphone("Samsung", "Galaxy S24", "+79851256898"),
    Smartphone("Honor", "X7a", "+79853569852"),
    Smartphone("Realme", "C53", "+79853569852"),
    Smartphone("iPhone", "15 Pro", "+79853569852")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
