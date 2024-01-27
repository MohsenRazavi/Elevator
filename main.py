import threading
from threading import Thread
from queue import Queue

from elevator_functions import get_request, fcfs, input_getter
from general_functions import get_integer_user_input, get_user_choice

ALGORITHMS = [
    'FCFS',
    'SJF',
    'ROUND-ROBIN',
    'STRF'
]

num_of_floors = get_integer_user_input('Enter number of floors: ', default=4)
floor_height = get_integer_user_input('Enter floor height(m): ', default=3)
print('Elevator algorithm: ')
algo_index = get_user_choice(ALGORITHMS) - 1
algo = ALGORITHMS[algo_index]
elevator_speed = get_integer_user_input('Enter elevator speed(m/s): ', default=1)

floor_list = []
current_floor = 0
inp_list = []

inp_getter = threading.Thread(target=input_getter, args=(inp_list,))

if algo == 'FCFS':
    req_getter = threading.Thread(target=get_request, args=(inp_list, floor_list))
    fcfs_trd = threading.Thread(target=fcfs, args=(inp_list, floor_list, current_floor, elevator_speed))

    inp_getter.start()
    req_getter.start()
    fcfs_trd.start()

    inp_getter.join()
    req_getter.join()
    fcfs_trd.join()
elif algo == 'SJF':
    pass
elif algo == 'Round-Robin':
    pass
elif algo == 'STRF':
    pass
else:
    print('🤢🤢🤢🤢🤢🤢')
