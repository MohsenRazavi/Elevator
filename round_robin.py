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


def rr(requested_floors, current_floor, ele_speed, q, floor_height):
    index = 0
    next_request = None
    while True:
        try:
            if not next_request:
                next_request = requested_floors[index]
            print('req : ', requested_floors)
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
                else:
                    current_floor -= 1
            print(f'We arrived at floor {dst_floor}')
            src_floor = current_floor
            dst_floor = next_request[1]
            direction = None
            if dst_floor > src_floor:
                direction = 'TOP'
            elif dst_floor < src_floor:
                direction = 'DOWN'
            distance = q
            time_to_destination = distance
            for _ in range(time_to_destination):
                timeit.default_timer()
                time.sleep(floor_height // ele_speed)
                timeit.default_timer()
                print(f'Floor {current_floor}')
                if direction == 'TOP':
                    current_floor += 1
                else:
                    current_floor -= 1
                next_request[2] -= 1
            print(f'Floor {current_floor}')
            if next_request[2] == 0:
                print(f'We arrived at the destination floor {next_request[1]}')
                del requested_floors[index]
                next_request = None
                index = (index + 1) % len(requested_floors)
            else:
                next_request[0] = current_floor
                index = (index + 1) % len(requested_floors)
                next_request = requested_floors[index]
                if next_request[0] != current_floor:
                    print('Ignoring this, going to floor ', next_request[0])

        except ValueError:
            continue
        except IndexError:
            continue
        except ZeroDivisionError:
            continue