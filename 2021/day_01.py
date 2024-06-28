from pathlib import Path

sum1 = 0
sum2 = 0
with open(Path("2021","day_01.txt")) as file:
    meas = [int(n) for n in file.read().split("\n")]
    
    for n in range(len(meas)):
        if n >= 1 and meas[n] > meas[n-1]:
            sum1 += 1
        if n >=3 and meas[n] + meas[n-1] + meas[n-2] > meas[n-1] + meas[n-2] + meas[n-3]:
            sum2 += 1

print(sum1)
print(sum2)