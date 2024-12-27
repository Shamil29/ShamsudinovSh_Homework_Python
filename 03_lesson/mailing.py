class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return (f"Отправление из {self.to_address}, в {self.from_address}. "
                f"Стоимость {self.cost} рублей, трек-номер: {self.track}")
