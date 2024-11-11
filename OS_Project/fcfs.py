
# Function to calculate waiting time for each process
def calculate_waiting_time(processes, burst_times):
    waiting_times = [0] * len(processes)
    total_waiting_time = 0

    # Waiting time for the first process is always 0
    for i in range(1, len(processes)):
        waiting_times[i] = burst_times[i - 1] + waiting_times[i - 1]
        total_waiting_time += waiting_times[i]

    return waiting_times, total_waiting_time

# Function to calculate turnaround time for each process
def calculate_turnaround_time(burst_times, waiting_times):
    turnaround_times = [0] * len(burst_times)
    total_turnaround_time = 0

    for i in range(len(burst_times)):
        turnaround_times[i] = burst_times[i] + waiting_times[i]
        total_turnaround_time += turnaround_times[i]

    return turnaround_times, total_turnaround_time

# Function to read input from file, calculate and write output
def fcfs_scheduling(input_file, output_file):
    # Reading the input from file
    processes = []
    burst_times = []

    with open(input_file, 'r') as file:
        for line in file:
            data = line.split()
            processes.append(data[0])
            burst_times.append(int(data[1]))

    # Calculating waiting time and turnaround time
    waiting_times, total_waiting_time = calculate_waiting_time(processes, burst_times)
    turnaround_times, total_turnaround_time = calculate_turnaround_time(burst_times, waiting_times)

    # Calculating averages
    average_waiting_time = total_waiting_time / len(processes)
    average_turnaround_time = total_turnaround_time / len(processes)

    # Writing the results to the output file
    with open(output_file, 'w') as file:
        file.write("Process\tBurst Time\tWaiting Time\tTurnaround Time\n")
        for i in range(len(processes)):
            file.write(f"{processes[i]}\t{burst_times[i]}\t\t{waiting_times[i]}\t\t{turnaround_times[i]}\n")
        
        file.write(f"\nAverage Waiting Time: {average_waiting_time:.2f}\n")
        file.write(f"Average Turnaround Time: {average_turnaround_time:.2f}\n")

# Main function to execute the FCFS algorithm
if __name__ == "__main__":
    input_file = "input.txt"  # Specify your input file
    output_file = "output.txt"  # Specify your output file

    fcfs_scheduling(input_file, output_file)
    print(f"Results have been written to {output_file}")
    cont = input("Want to display the output? Press y to continue...")
    if cont == 'y':
        with open(output_file, 'r') as file:
            for line in file:
                print(line)