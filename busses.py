def busses(students):
    num_bus = int(students/52)
    left = students%52
    if left == 0:
        return num_bus
    elif left > 0:
        return num_bus+1

print(busses(204))