def max_visitors_online(n, t_in, t_out):
    events = []
    for i in range(n):
        events.append((t_in[i], -1))
        events.append((t_out[i], 1))
    events.sort()

    online = 0
    max_online = 0
    for event in events:
        if event[1] == -1:
            online += 1
        else:
            online -= 1
        max_online = max(online, max_online)
    return max_online


def time_with_visitors(n, t_in, t_out):
    events = []
    for i in range(n):
        events.append((t_in[i], -1))
        events.append((t_out[i], 1))
    events.sort()

    online = 0
    not_empty_time = 0
    for i in range(len(events)):
        if online > 0:
            not_empty_time += events[i][0] - events[i - 1][0]
        if events[i][1] == -1:
            online += 1
        else:
            online -= 1
    return not_empty_time


def boss_counters(n, t_in, t_out, m, t_boss):
    events = []
    for i in range(n):
        events.append((t_in[i], -1))
        events.append((t_out[i], 1))
    for i in range(m):
        events.append((t_boss[i]), 0)
    events.sort()

    online = 0
    boss_ans = []
    for i in range(len(events)):
        if events[i][1] == -1:
            online += 1
        elif events[i][1] == 1:
            online -= 1
        else:
            boss_ans.append(online)
    return boss_ans


def is_parking_full(cars, n):
    events = []
    for car in cars:
        time_in, time_out, place_from, place_to = car
        events.append((time_in, 1, place_to - place_from + 1))
        events.append((time_out, -1, place_to - place_from + 1))
    events.sort()

    occupied = 0
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
        elif events[i][1] == 1:
            occupied += events[i][2]
        if occupied == n:
            return True
        return False


def min_cars_on_full_parking(cars, n):
    events = []
    for car in cars:
        time_in, time_out, place_from, place_to = car
        events.append((time_in, 1, place_to - place_from + 1))
        events.append((time_out, -1, place_to - place_from + 1))
    events.sort()

    occupied = 0
    now_cars = 0
    min_cars = len(cars) + 1
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            now_cars -= 1
        elif events[i][1] == 1:
            occupied += events[i][2]
            now_cars += 1
        if occupied == n:
            min_cars = min(min_cars, now_cars)
        return min_cars


# with numbers of cars
def min_cars_on_full_parking(cars, n):
    events = []
    for i in range(len(cars)):
        time_in, time_out, place_from, place_to = cars[i]
        events.append((time_in, 1, place_to - place_from + 1, i))
        events.append((time_out, -1, place_to - place_from + 1, i))
    events.sort()

    occupied = 0
    now_cars = 0
    min_cars = len(cars) + 1
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            now_cars -= 1
        elif events[i][1] == 1:
            occupied += events[i][2]
            now_cars += 1
        if occupied == n and now_cars < min_cars:
            min_cars = now_cars

    car_nums = set()
    now_cars = 0
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            now_cars -= 1
            car_nums.remove(events[i][3])
        elif events[i][1] == 1:
            occupied += events[i][2]
            now_cars += 1
            car_nums.add(events[i][3])
        if occupied == n and now_cars == min_cars:
            return car_nums
    return set()

