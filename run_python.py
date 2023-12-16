import subprocess
import datetime
import time

if __name__ == '__main__':
    times = 20
    today = datetime.datetime.now()
    for d in range(8, today.day + 1):
        p = 'day' + str(d).zfill(2)
        if d in [5]:
            print(p, ': -')
            continue
        start_time = time.time()
        for _ in range(times):
            subprocess.run(['python3', f'{p}.py'])
        print(p, ':', round((time.time() - start_time) * 1000 / times, 1), 'ms')
