import subprocess
import datetime
import time

# # Test for compiling code using codon
# codon run -release day03.py
# codon build -release day03.py
# time ./day03

if __name__ == '__main__':
    times = 20
    today = datetime.datetime.now()
    for d in range(20, today.day + 1):
        p = 'day' + str(d).zfill(2)
        if d in [8, 12, 17, 19]:
            # Exclusions not working with Codon:
            # - Day 8: math.lcm(*args)
            # - Day 12: @cache decorator (functools)
            # - Day 17: from queue import PriorityQueue (for Dijkstra)
            # - Day 19: Dynamic list items (tuples or str)
            # - Day 20: math.lcm()
            print(p, ': -')
            continue
        subprocess.run(['/home/adrianus/.codon/bin/codon', 'build', '-release', f'{p}.py'])
        start_time = time.time()
        for _ in range(times):
            subprocess.run([f'./{p}'])
        print(p, ':', round((time.time() - start_time) * 1000 / times, 1), 'ms')
        subprocess.run(['rm', f'./{p}'])
