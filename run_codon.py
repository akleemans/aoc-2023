import subprocess
import datetime
import time

if __name__ == '__main__':
    today = datetime.datetime.now()
    for d in range(1, today.day + 1):
        p = 'day' + str(d).zfill(2)
        subprocess.run(['/home/adrianus/.codon/bin/codon', 'build', '-release', f'{p}.py'])
        start_time = time.time()
        subprocess.run([f'./{p}'])
        print(p, ':', round(time.time() - start_time, 3), 's')
