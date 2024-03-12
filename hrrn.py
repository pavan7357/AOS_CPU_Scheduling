def sortByArrival(at, bt, n):
    # Selection Sort applied
    for i in range(0, n - 1):
        for j in range(i + 1, n):

            # Check for lesser arrival time
            if at[i] > at[j]:
                # Swap earlier process to front
                at[i], at[j] = at[j], at[i]
                bt[i], bt[j] = bt[j], bt[i]

# Driver code
if __name__ == '__main__':
    sum_bt = 0
    avg_wt = 0
    avg_TAT = 0
    n = int(input("Enter the number of processes: "))

    completed = [0] * n
    waiting_time = [0] * n
    turnaround_time = [0] * n
    response_time = [0] * n
    normalised_TT = [0] * n

    # User input arrival times
    arrival_time = []
    burst_time = []

    print("Enter arrival times and burst times for each process:")
    for i in range(n):
        arrival = int(input(f"Arrival time for process {i + 1}: "))
        burst = int(input(f"Burst time for process {i + 1}: "))
        arrival_time.append(arrival)
        burst_time.append(burst)
        sum_bt += burst

    # Sorting the processes by arrival times
    sortByArrival(arrival_time, burst_time, n)
    print("Name","\t\t", "Arrival time","\t\t", "Burst time","\t\t","Completion Time","\t\t", "Turnaround ","\t\t", "Waiting Time", "\t\t", "Response Time")
    t = arrival_time[0]

    while t < sum_bt:

        # Set lower limit to response ratio
        hrr = -9999
        temp, loc = 0, 0

        for i in range(n):

            # Checking if process has arrived
            # and is Incomplete
            if arrival_time[i] <= t and completed[i] != 1:

                # Calculating Response Ratio
                temp = ((burst_time[i] +
                         (t - arrival_time[i])) /
                        burst_time[i])

                # Checking for Highest Response Ratio
                if hrr < temp:
                    # Storing Response Ratio
                    hrr = temp
                    # Storing Location
                    loc = i

        # Updating time value
        t += burst_time[loc]

        # Calculation of waiting time
        waiting_time[loc] = (t - arrival_time[loc] -
                             burst_time[loc])

        # Calculation of Turn Around Time
        turnaround_time[loc] = t - arrival_time[loc]

        # Calculation of Response Time
        response_time[loc] = turnaround_time[loc] - burst_time[loc]

        # Calculation of Normalized Turn Around Time
        normalised_TT[loc] = float(turnaround_time[loc] /
                                   burst_time[loc])

        # Updating Completion Status
        completed[loc] = 1

        # Sum Turn Around Time for average
        avg_TAT += turnaround_time[loc]

        # Sum Waiting Time for average
        avg_wt += waiting_time[loc]

        # Print process details
        print(chr(65 + loc), "\t\t", arrival_time[loc],
              "\t\t\t", burst_time[loc], "\t\t\t",t, "\t\t\t\t", turnaround_time[loc], "\t\t\t",
              waiting_time[loc], "\t\t\t",
              response_time[loc])

    print("Average waiting time: {0:.2f}".format(avg_wt / n))
    print("Average Turn Around time: {0:.2f}".format(avg_TAT / n))
