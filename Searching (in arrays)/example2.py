def seq_search(reservation_list, key):
    found = False
    i = 0
    while not found and i < len(reservation_list):
        if reservation_list[i].name == key:
            found = True
        i += 1
    if found:
        return reservation_list[i - 1].room_number
    else:
        return f"{key} is not a guest here."

class Reservation:
    def __init__(self, name, room_number):
        self.name = name
        self.room_number = room_number
reservations = [Reservation("JK", 111), Reservation("JH", 112), Reservation("JM", 113)]

name = [reservation.name for reservation in reservations]
room_number = [reservation.room_number for reservation in reservations]
print(seq_search(reservations, "V"))