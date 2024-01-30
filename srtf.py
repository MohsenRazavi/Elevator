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
            try:
                req_flr = [int(i) for i in head.split('-')]
                req_flr.append(abs(req_flr[1] - req_flr[0]))
                requested_floors.append(req_flr)
                del inp_queue[-1]
            except ValueError:
                pass
        except IndexError:
            continue


def srtf(requested_floors, current_floor, ele_speed, floor_height):
    next_request = None
    index = None
    arrived_at_src_floor = False
    while True:
        try:
            if not next_request:
                next_request = min(requested_floors, key=lambda i: i[2])
                index = requested_floors.index(next_request)
            print('req : ', requested_floors)
            if next_request[2] == 0:
                del requested_floors[index]
            src_floor = current_floor
            dst_floor = next_request[0]
            direction = None
            if dst_floor > src_floor:
                direction = 'TOP'
            elif dst_floor < src_floor:
                direction = 'DOWN'
            distance = abs(dst_floor - src_floor)
            time_to_destination = distance
            print(f'Going to floor {dst_floor}')
            for _ in range(time_to_destination):
                timeit.default_timer()
                time.sleep(floor_height // ele_speed)
                timeit.default_timer()
                print(f'Floor {current_floor}')
                if direction == 'TOP':
                    current_floor += 1
                elif direction == 'DOWN':
                    current_floor -= 1
                shorter_request = min(requested_floors, key=lambda i: i[2])
                shorter_index = requested_floors.index(shorter_request)
                if shorter_index == index:
                    continue
                else:
                    next_request = shorter_request
                    index = shorter_index
                    print('Ignoring this, going to floor ', next_request[0])
                    arrived_at_src_floor = False
                    break
            else:
                print(f'We arrived at floor {dst_floor}')
                arrived_at_src_floor = True

            if arrived_at_src_floor:
                src_floor = current_floor
                dst_floor = next_request[1]
                direction = None
                if dst_floor > src_floor:
                    direction = 'TOP'
                elif dst_floor < src_floor:
                    direction = 'DOWN'
                distance = abs(dst_floor - src_floor)
                time_to_destination = distance
                for _ in range(time_to_destination):
                    timeit.default_timer()
                    time.sleep(floor_height // ele_speed)
                    timeit.default_timer()
                    print(f'Floor {current_floor}')
                    if direction == 'TOP':
                        current_floor += 1
                    elif direction == 'DOWN':
                        current_floor -= 1
                    next_request[2] -= 1
                    shorter_request = min(requested_floors, key=lambda i: i[2])
                    shorter_index = requested_floors.index(shorter_request)
                    if shorter_index == index:
                        continue
                    else:
                        next_request[0] = current_floor
                        next_request = shorter_request
                        index = shorter_index
                        print('Ignoring this, going to floor ', next_request[0])
                        arrived_at_src_floor = False
                        break
                else:
                    print(f'We arrived at destination floor {dst_floor} !')
                    del requested_floors[index]
                    next_request = None
                    index = None

        except ValueError:
            continue
