
HOUR_TO_MINUTE = 60
DAY_TO_HOUR = 24
# The data is inaccurate, we treate power below 500 as off, otherwise on.
THRESHOLD = 500
KWH_TO_WATMIN = 1000 * 60


def count_time(data):
    minute_count = len(data)
    hour_count = minute_count / HOUR_TO_MINUTE
    day_count = hour_count / DAY_TO_HOUR
    print(f'Data covers a total of {hour_count} hours')
    print(f'(That\'s {day_count} days)')
    print()
    return day_count


def cal_produce(data, day_count):
    minute_run = 0
    for i in data:
        if i > THRESHOLD:
            minute_run += 1
    production = 2 * minute_run
    efficient = production / day_count
    print(f'Pump was running for {minute_run} minutes', end='')
    print(f'producing {production} gallons')
    print(f'(That is {efficient} gallons per day)')
    print()


def total_power(data):
    watt_minute = sum(data)
    kwh = watt_minute / KWH_TO_WATMIN
    print(f'Pump required a total of {watt_minute} watt minutes of power')
    print(f'That\'s {kwh} kWh')
    print()


def milestone(data):
    sum = 0
    count = 1
    milestone_5 = -1
    milestone_100 = -1
    for i in data:
        if i > THRESHOLD:
            sum += 2
            if sum >= 5 and milestone_5 == -1:
                milestone_5 = count
            if sum >= 100 and milestone_100 == -1:
                milestone_100 = count
                break
        count += 1
    print(f'It took {milestone_5} minutes of data to reach 5 gallons.')
    print(f'It took {milestone_100} minutes of data to reach 100 gallons.')
    print()


def pump(data):
    count = 0
    minute = 1
    print('Information on water softener recharges:')
    for i in data:
        if i >= THRESHOLD:
            count += 1
        else:
            if count >= 120:
                print(f'{count} minutes, started at {minute - count}')
                count = 0
            else:
                count = 0
        minute += 1


def main():
    file_name = input('Please enter the file name: ')

    try:
        with open(file_name, 'r') as file_content:
            data = []
            for i in file_content:
                data.append(int(i.rstrip()))
    except FileNotFoundError:
        print(f'Unable to open {file_name}')
        return

    day_count = count_time(data)
    cal_produce(data, day_count)
    total_power(data)
    milestone(data)
    pump(data)


main()
