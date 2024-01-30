import timeit
import time

def input_getter(inp_queue):
    while True:
        try:
            i = input()
            if i == 'q':
                exit()
            inp_queue.append(i)
            print('q: ', inp_queue)
        except EOFError:
            continue


def get_request(inp_queue, requested_floors):
    while True:
        try:
            head = inp_queue[-1]
            try:
                requested_floors.append([int(i) for i in head.split('-')])
                del inp_queue[-1]
            except ValueError:
                pass
        except IndexError:
            continue


def go_to_floor(src_floor, dst_floor, elevator_speed, floor_height):
    if dst_floor > src_floor:
        direction = 'TOP'
    elif dst_floor < src_floor:
        direction = 'DOWN'
    distance = abs(src_floor - dst_floor)
    time_to_destination = distance // elevator_speed
    print(f'Going to floor {dst_floor}')
    for _ in range(time_to_destination + 1):
        timeit.default_timer()
        time.sleep(floor_height)
        timeit.default_timer()
        print(f'Floor {src_floor}')
        if direction == 'TOP':
            src_floor += 1
        else:
            src_floor -= 1
    print(f'We arrived at floor {dst_floor} !')
    return dst_floor


def sjf(requested_floors, current_floor, ele_speed, floor_height):
    while True:
        try:
            next_floor = min(requested_floors, key=lambda i: abs(i[0] - i[1]))
            index = requested_floors.index(next_floor)
            print('req : ', requested_floors)
            del requested_floors[index]
            current_floor = go_to_floor(current_floor, next_floor[0], ele_speed, floor_height)
            current_floor = go_to_floor(current_floor, next_floor[1], ele_speed, floor_height)
        except ValueError:
            continue
