import threading
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

if algo == 'FCFS':
    from fcfs import get_request, fcfs, input_getter

    inp_getter = threading.Thread(target=input_getter, args=(inp_list,))
    req_getter = threading.Thread(target=get_request, args=(inp_list, floor_list))
    fcfs_trd = threading.Thread(target=fcfs, args=(inp_list, floor_list, current_floor, elevator_speed, floor_height))

    inp_getter.start()
    req_getter.start()
    fcfs_trd.start()

    inp_getter.join()
    req_getter.join()
    fcfs_trd.join()
elif algo == 'SJF':
    from sjf import get_request, sjf, input_getter

    inp_getter = threading.Thread(target=input_getter, args=(inp_list,))
    req_getter = threading.Thread(target=get_request, args=(inp_list, floor_list))
    sjf_trd = threading.Thread(target=sjf, args=(floor_list, current_floor, elevator_speed, floor_height))

    inp_getter.start()
    req_getter.start()
    sjf_trd.start()

    inp_getter.join()
    req_getter.join()
    sjf_trd.join()
elif algo == 'ROUND-ROBIN':
    from round_robin import get_request, rr, input_getter

    q = 1
    inp_getter = threading.Thread(target=input_getter, args=(inp_list,))
    req_getter = threading.Thread(target=get_request, args=(inp_list, floor_list))
    rr_trd = threading.Thread(target=rr, args=(floor_list, current_floor, elevator_speed, q, floor_height))

    inp_getter.start()
    req_getter.start()
    rr_trd.start()

    inp_getter.join()
    req_getter.join()
    rr_trd.join()
elif algo == 'STRF':
    from srtf import get_request, srtf, input_getter

    inp_getter = threading.Thread(target=input_getter, args=(inp_list,))
    req_getter = threading.Thread(target=get_request, args=(inp_list, floor_list))
    srtf_trd = threading.Thread(target=srtf, args=(floor_list, current_floor, elevator_speed, floor_height))

    inp_getter.start()
    req_getter.start()
    srtf_trd.start()

    inp_getter.join()
    req_getter.join()
    srtf_trd.join()
else:
    print('🤢🤢🤢🤢🤢🤢')
