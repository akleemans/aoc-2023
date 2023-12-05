import subprocess
import datetime
import time

# # Test for compiling code using codon
# codon run -release day03.py
# codon build -release day03.py
# time ./day03

if __name__ == '__main__':
    today = datetime.datetime.now()
    for d in range(1, today.day + 1):
        p = 'day' + str(d).zfill(2)
        subprocess.run(['/home/adrianus/.codon/bin/codon', 'build', '-release', f'{p}.py'])
        start_time = time.time()
        subprocess.run([f'./{p}'])
        print(p, ':', round(time.time() - start_time, 3), 's')
        subprocess.run(['rm', f'./{p}'])
