import sys

N = int(sys.argv[1])
M = int(sys.argv[2])
L = int(sys.argv[3])
T = int(sys.argv[4])


cycle_length = N + M + L  # Длина полного цикла
time_in_cycle = T % cycle_length  # Время в текущем цикле

if time_in_cycle < N:
    print("green")
elif time_in_cycle < N + M:
    print("yellow")
else:
    print("red")
