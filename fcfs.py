class FCFS_Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid                      # Process ID
        self.arrival_time = arrival_time    # Arrival time of the process
        self.burst_time = burst_time        # Burst time of the process
        self.completion_time = 0            # Completion time of the process
        self.turnaround_time = 0            # Turnaround time of the process
        self.waiting_time = 0               # Waiting time of the process


def calculate_metrics(processes):
    current_time = 0
    total_turnaround_time = 0
    total_waiting_time = 0
    for process in processes:
        # Update completion time
        process.completion_time = max(current_time, process.arrival_time) + process.burst_time
        # Update turnaround time
        process.turnaround_time = process.completion_time - process.arrival_time
        # Update waiting time
        process.waiting_time = max(0, process.turnaround_time - process.burst_time)

        # Update current time
        current_time = process.completion_time

        # Update total turnaround and waiting times
        total_turnaround_time += process.turnaround_time
        total_waiting_time += process.waiting_time

    # Calculate average turnaround and waiting times
    avg_turnaround_time = total_turnaround_time / len(processes)
    avg_waiting_time = total_waiting_time / len(processes)

    return avg_turnaround_time, avg_waiting_time


def print_process_details(processes):
    print("Process\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
    for process in processes:
        print(f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.completion_time}\t\t{process.turnaround_time}\t\t{process.waiting_time}")


def generate_gantt_chart(processes):
    gantt_chart = []
    current_time = 0
    for process in processes:
        gantt_chart.append((process.pid, current_time, process.completion_time))
        current_time = process.completion_time
    return gantt_chart


def main():
    # Get number of processes from the user
    num_processes = int(input("Enter the number of processes: "))

    # Define an empty list to store processes
    processes = []

    # Get input for each process
    for i in range(1, num_processes + 1):
        arrival_time = int(input(f"Enter arrival time for Process {i}: "))
        burst_time = int(input(f"Enter burst time for Process {i}: "))
        processes.append(FCFS_Process(i, arrival_time, burst_time))

    # Add transient event
    transient_event = FCFS_Process('Trans', 7, 6)
    processes.append(transient_event)

    # Sort processes based on arrival time
    processes.sort(key=lambda x: x.arrival_time)

    # Calculate metrics for processes
    avg_tat, avg_wt = calculate_metrics(processes)

    # Print process details
    print_process_details(processes)

    # Generate Gantt chart
    gantt_chart = generate_gantt_chart(processes)
    print("\nGantt Chart:")
    print("Process\tStart Time\tEnd Time")
    for entry in gantt_chart:
        print(f"{entry[0]}\t{entry[1]}\t\t{entry[2]}")

    # Print average turnaround and waiting times
    print(f"\nAverage Turnaround Time: {avg_tat}")
    print(f"Average Waiting Time: {avg_wt}")


if __name__ == "__main__":
    main()
