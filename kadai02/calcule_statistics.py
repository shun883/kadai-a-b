def create_sum(dates):
    dates_sum = 0
    for date in dates:
        dates_sum += date
    return dates_sum


def create_max(dates):
    max_date = 0
    for date in dates:
        if date > max_date:
            max_date = date
    return max_date


def create_min(dates):
    min_date = dates[0]
    for date in dates:
        if date < min_date:
            min_date = date
    return min_date


def create_average(dates):
    sum = 0
    count = 0
    for date in dates:
        sum += date
        count += 1
    return sum / count


input_dates_str = list()
dates_int = list()
input_dates_str = input('データを入力してください(スペース区切り) > ').split(' ')
for date in input_dates_str:
    dates_int.append(int(date))

print(f'合計値: {create_sum(dates_int)}')
print(f'最大値 {create_max(dates_int)}')
print(f'最小値 {create_min(dates_int)}')
print(f'平均値{create_average(dates_int)}')
