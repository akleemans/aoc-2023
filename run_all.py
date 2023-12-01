import timeit
import datetime

if __name__ == '__main__':
    # Uncomment if running current AoC
    today = datetime.datetime.now()
    for d in range(1, today.day + 1):
        p = 'day' + str(d).zfill(2)
        t = timeit.timeit('import ' + p + '; ' + p + '.main()', number=1)
        print(p, ':', round(t, 3), 's')
