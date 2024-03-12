class RoundRobin_Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid              # Process ID
        self.arrival_time = arrival_time  # Arrival time of the process
        self.burst_time = burst_time     # Burst time of the process
        self.completion_time = 0    # Completion time of the process
        self.turnaround_time = 0    # Turnaround time of the process
        self.waiting_time = 0       # Waiting time of the process
        self.response_time = -1     # Response time of the process, initialized to -1


def calculate_metrics(processes, time_quantum):
    current_time = 0
    remaining_burst = [process.burst_time for process in processes]

    while any(remaining_burst):
        for process in processes:
            if remaining_burst[process.pid - 1] > 0:
                if process.response_time == -1:
                    process.response_time = current_time - process.arrival_time

                if remaining_burst[process.pid - 1] <= time_quantum:
                    current_time += remaining_burst[process.pid - 1]
                    process.completion_time = current_time
                    remaining_burst[process.pid - 1] = 0
                else:
                    current_time += time_quantum
                    remaining_burst[process.pid - 1] -= time_quantum

    for process in processes:
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time


def print_process_details(processes):
    print("Process\tArrival Time\tBurst Time\tCompletion Time\t\tTurnAround Time\t\tWaiting Time\tResponse Time")
    for process in processes:
        print(f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.completion_time}\t\t\t{process.turnaround_time}\t\t\t{process.waiting_time}\t\t{process.response_time}")

def main():
    # Get number of processes from the user
    num_processes = int(input("Enter the number of processes: "))

    # Define an empty list to store processes
    processes = []

    # Get input for each process
    for i in range(1, num_processes + 1):
        arrival_time = int(input(f"Enter arrival time for Process {i}: "))
        burst_time = int(input(f"Enter burst time for Process {i}: "))
        processes.append(RoundRobin_Process(i, arrival_time, burst_time))

    # Get time quantum from the user
    time_quantum = int(input("Enter the time quantum: "))

    # Calculate metrics for processes
    calculate_metrics(processes, time_quantum)

    # Print process details
    print_process_details(processes)

    # Calculate average TAT and WT
    total_tat = sum(process.turnaround_time for process in processes if process.pid != 'Trans')
    total_wt = sum(process.waiting_time for process in processes if process.pid != 'Trans')
    avg_tat = total_tat / num_processes
    avg_wt = total_wt / num_processes

    print(f"\nAverage Turnaround Time (excluding transient event): {avg_tat:.2f}")
    print(f"Average Waiting Time (excluding transient event): {avg_wt:.2f}")


if __name__ == "__main__":
    main()