def LRTF(processes):
    # Sort processes by their arrival time
    processes.sort(key=lambda x: x[2])

    n = len(processes)
    remaining_time = [process[1] for process in processes]  # Burst time of each process
    completion_time = [0] * n  # Initialize completion time for each process
    waiting_time = [0] * n  # Initialize waiting time for each process
    turnaround_time = [0] * n  # Initialize turnaround time for each process
    response_time = [-1] * n  # Initialize response time for each process
    current_time = 0

    while True:
        # Check if all processes have completed
        if sum(remaining_time) == 0:
            break
        
        # Find processes that have arrived at current time
        arrived_processes = [i for i in range(n) if processes[i][2] <= current_time and remaining_time[i] > 0]
        
        if arrived_processes:
            # Select process with the longest remaining burst time
            max_time_process = max(arrived_processes, key=lambda x: remaining_time[x])
            # Update response time if it's the first time the process is executed
            if response_time[max_time_process] == -1:
                response_time[max_time_process] = current_time - processes[max_time_process][2]
            # Update current time
            current_time += 1
            # Decrement remaining burst time
            remaining_time[max_time_process] -= 1
            # Update completion time if the process has completed
            if remaining_time[max_time_process] == 0:
                completion_time[max_time_process] = current_time
                turnaround_time[max_time_process] = completion_time[max_time_process] - processes[max_time_process][2]
                waiting_time[max_time_process] = turnaround_time[max_time_process] - processes[max_time_process][1]
        else:
            # No process has arrived, move to the next time step
            current_time += 1
    
    # Map process IDs to completion times
    completion_times = {processes[i][0]: completion_time[i] for i in range(n)}
    
    return completion_times, turnaround_time, waiting_time, response_time

# Input the number of processes
num_processes = int(input("Enter the number of processes: "))

# Input arrival time and burst time for each process
processes = []
for i in range(num_processes):
    process_id = i + 1
    arrival_time = int(input(f"Enter arrival time for process {process_id}: "))
    burst_time = int(input(f"Enter burst time for process {process_id}: "))
    processes.append((process_id, burst_time, arrival_time))

# Run LRTF algorithm
completion_times, turnaround_time, waiting_time, response_time = LRTF(processes)

# Display output in tabular format
print("\nProcess ID\tCompletion Time\tTurnaround Time\tWaiting Time\tResponse Time")
for i in range(num_processes):
    print(f"{processes[i][0]}\t\t{completion_times[processes[i][0]]}\t\t{turnaround_time[i]}\t\t{waiting_time[i]}\t\t{response_time[i]}")

# Calculate average turnaround time and waiting time
avg_turnaround_time = sum(turnaround_time) / num_processes
avg_waiting_time = sum(waiting_time) / num_processes
print("\nAverage Turnaround Time:", avg_turnaround_time)
print("Average Waiting Time:", avg_waiting_time)
