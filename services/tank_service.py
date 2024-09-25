from models.tank import Tank

def create_tank_service(name, capacity, number):
    tank_data = {
        "name": name,
        "capacity": capacity,
        "number": number
    }
    result = Tank.create_tank(tank_data)
    return str(result.inserted_id)