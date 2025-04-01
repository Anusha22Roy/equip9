from collections import defaultdict
from bisect import bisect_left, bisect_right

def preprocess_maintenance_logs(maintenance_logs)
    Preprocess logs to compute prefix sums for date-based queries.
    date_cost_map = defaultdict(int)

    # Aggregate costs by date
    for _, date, cost in maintenance_logs
        date_cost_map[date] += cost

    # Convert to sorted list
    sorted_dates = sorted(date_cost_map.keys())
    prefix_sums = []
    cumulative_sum = 0

    for date in sorted_dates
        cumulative_sum += date_cost_map[date]
        prefix_sums.append(cumulative_sum)

    return sorted_dates, prefix_sums

def query_total_cost(sorted_dates, prefix_sums, start_date, end_date)
    Returns total maintenance cost in the given date range.
    start_idx = bisect_left(sorted_dates, start_date)
    end_idx = bisect_right(sorted_dates, end_date) - 1

    if start_idx = len(sorted_dates) or sorted_dates[start_idx]  end_date
        return 0  # No records in the given range

    total_cost = prefix_sums[end_idx]
    if start_idx  0
        total_cost -= prefix_sums[start_idx - 1]

    return total_cost

def process_queries(maintenance_logs, queries)
    Processes all queries efficiently using prefix sums.
    sorted_dates, prefix_sums = preprocess_maintenance_logs(maintenance_logs)
    return [query_total_cost(sorted_dates, prefix_sums, start, end) for start, end in queries]

# Example Input
maintenance_logs = [
    (101, 2024-01-01, 500),
    (102, 2024-01-10, 300),
    (101, 2024-01-15, 700)
]

queries = [
    (2024-01-01, 2024-01-10),
    (2024-01-01, 2024-01-15)
]

# Running the function
output = process_queries(maintenance_logs, queries)
print(output)  # Expected Output [800, 1500]