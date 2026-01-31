class UserRepository:
    def __init__(self):
        # Имитируем базу данных с парой водителей
        self.users = [
            {"id": 1, "username": "Ivan_Driver", "role": "driver", "rating": 4.9},
            {"id": 2, "username": "Mariya_Driver", "role": "driver", "rating": 5.0},
        ]

    def get_available_drivers(self):
        # Возвращаем только водителей
        return [user for user in self.users if user["role"] == "driver"]