# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d
    #m miles on full tank
    #d distance between cities
    #stops distance between gasstation
    location = 0
    if location + m >= d:
        return 0
    if len(stops) == 0 or (stops[0] - location) > m:
        return -1
    last_stop = location
    while len(stops) != 0 and (stops[0] - location) <= m:
        last_stop = stops[0]
        stops.pop(0)
    return 1 + compute_min_number_of_refills(d, m, stops)



if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
