def sjf(process_list):
    process_list.sort()  # Sort processes based on arrival time
    t = 0
    gantt = []
    completed = {}
    burst_times = {}
    for p in process_list:
        pid = p[2]
        burst_time = p[1]
        burst_times[pid] = burst_time
    while process_list:  
        available = [p for p in process_list if p[0] <= t]
        if not available:
            gantt.append(("Idle", t, t + 1))
            t += 1
            continue
        else:
            process = min(available, key=lambda x: x[1])
            gantt.append((process[2], t, t + process[1]))
            process_list.remove(process)
            rem_burst = process[1]
            t += rem_burst
            ct = t
            pid = process[2]
            arrival_time = process[0]
            burst_time = burst_times[pid]
            tt = ct - arrival_time
            wt = tt - burst_time
            completed[process[2]] = [ct, tt, wt]

    print("Gantt Chart:")
    print("Process | Start Time\t| End Time")
    for item in gantt:
        print(f"{item[0]}\t| {item[1]}\t\t| {item[2]}")
    print("\nCompleted Processes:")
    print("Process | Completion Time\t| Turnaround Time\t| Waiting Time")
    for pid, metrics in completed.items():
        print(f"{pid}\t| {metrics[0]}\t\t\t| {metrics[1]}\t\t\t| {metrics[2]}")

    # Calculate average TAT and WT
    total_tat = sum(metrics[1] for metrics in completed.values())
    total_wt = sum(metrics[2] for metrics in completed.values())
    num_processes = len(completed)
    avg_tat = total_tat / num_processes
    avg_wt = total_wt / num_processes

    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")


if __name__ == "__main__":
    num_processes = int(input("Enter the number of processes: "))
    process_list = []
    for i in range(num_processes):
        print(f"\nEnter details for Process {i + 1}:")
        at = int(input("Arrival time: "))
        bt = int(input("Burst time: "))
        pid = "p" + str(i + 1)
        process_list.append([at, bt, pid])

    sjf(process_list)
