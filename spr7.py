class AirplaneHandler:
    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, handler):
        self.next_handler = handler

    def handle_request(self, request):
        if self.next_handler is not None:
            self.next_handler.handle_request(request)
        else:
            print(f"Не можливо обробити запит: {request}")


class EngineHandler(AirplaneHandler):
    def handle_request(self, request):
        if request == "Engine":
            print("Додавання двигуна")
        else:
            super().handle_request(request)


class AvionicsHandler(AirplaneHandler):
    def handle_request(self, request):
        if request == "Avionics":
            print("Додавання авіоніки")
        else:
            super().handle_request(request)


class InteriorHandler(AirplaneHandler):
    def handle_request(self, request):
        if request == "Interior":
            print("Додавання інтер'єру")
        else:
            super().handle_request(request)


def main():
    # Створення обробників
    engine_handler = EngineHandler()
    avionics_handler = AvionicsHandler()
    interior_handler = InteriorHandler()

    # Налаштування ланцюга відповідальності
    engine_handler.set_next_handler(avionics_handler)
    avionics_handler.set_next_handler(interior_handler)

    # Обробка запитів
    engine_handler.handle_request("Engine")
    engine_handler.handle_request("Avionics")
    engine_handler.handle_request("Interior")
    engine_handler.handle_request("Fuel System")


if __name__ == "__main__":
    main()
