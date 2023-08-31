def main():
    m, s = map(int, input().split())
    n = int(input())
    data = {}
    
    for _ in range(n):
        week, day, hour, *requests = map(int, input().split())
        timestamp = (week, day, hour)
        data[timestamp] = requests

    q = int(input())
    results = []

    for _ in range(q):
        query_type, week, day, hour, *values = map(int, input().split())
        timestamp = (week, day, hour)
        
        if query_type == 1:
            data[timestamp] = values
        elif query_type == 2:
            total_couriers = s
            remaining_requests = list(data[timestamp])
            to_cut = [0] * m
            
            while total_couriers > 0 and sum(remaining_requests) > 0:
                min_requests = min(remaining_requests)
                min_index = remaining_requests.index(min_requests)
                cut_amount = min(min_requests, total_couriers)
                to_cut[min_index] += cut_amount
                remaining_requests[min_index] -= cut_amount
                total_couriers -= cut_amount

            results.append(to_cut)

    for result in results:
        print(" ".join(f"{val:.14f}" for val in result))

if __name__ == "__main__":
    main()