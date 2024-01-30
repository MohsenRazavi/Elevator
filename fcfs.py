import time
import timeit


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
            if head.startswith('f-'):
                try:
                    requested_floors.append(int(head.split('-')[1]))
                    del inp_queue[-1]
                except ValueError:
                    pass
        except IndexError:
            continue


def fcfs(inp_queue, requested_floors, current_floor, ele_speed, floor_height):
    while True:
        try:
            next_floor = requested_floors[0]
            print('req : ', requested_floors)
            del requested_floors[0]
            current_floor = go_to_floor(current_floor, next_floor, ele_speed, floor_height)
            print(f'Enter your destination ({current_floor}): ')
            while inp_queue == [] or inp_queue[-1].startswith('f-'):
                pass
            print('q: ', inp_queue)
            try:
                dest_floor = int(inp_queue[-1])
                del inp_queue[-1]
            except ValueError:
                dest_floor = int(input())
            current_floor = go_to_floor(current_floor, dest_floor, ele_speed, floor_height)
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
    for _ in range(time_to_destination+1):
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
