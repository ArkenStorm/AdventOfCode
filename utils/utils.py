from datetime import datetime

def benchmark(year, day, func):
    executions = 1000

    start = datetime.now()
    for _ in range(executions):
        func(year, day)
    end = datetime.now()

    print(f'Total Average Execution Time: {(end - start) / executions}')
