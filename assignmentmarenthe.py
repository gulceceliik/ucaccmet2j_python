import json
stats = {}

with open("precipitation.json",encoding= 'utf-8')as file:
    all_precip = json.load(file)
#test 
print(all_precip[3]['station'])

#select seattle station
seattle_station = []
for measurement in all_precip:
    print(measurement)
    if (measurement)['station']== 'GHCND:US1WAKG0038':
        seattle_station.append(measurement)

#print(seattle_station)

#total montly precipitation for jan

total_monthly_precipitation_jan = []
for (measurement) in seattle_station:
     if measurement['date'] < '2010-02-01':
        total_monthly_precipitation_jan.append(measurement['value'])
        sum(total_monthly_precipitation_jan)
print(sum(total_monthly_precipitation_jan))

#total montly precipitation for feb

total_monthly_precipitation_feb = []
for (measurement) in seattle_station:
     if measurement['date'] < '2010-03-01':
        total_monthly_precipitation_feb.append(measurement['value'])
    #sum of jan and feb
        sum(total_monthly_precipitation_feb)

print(sum(total_monthly_precipitation_feb)-sum(total_monthly_precipitation_jan))

#total montly precipitation for march

total_monthly_precipitation_march = []
for (measurement) in seattle_station:
     if measurement['date'] < '2010-04-01':
        total_monthly_precipitation_march.append(measurement['value'])
    #sum of jan, feb and march
        sum(total_monthly_precipitation_march)

print(sum(total_monthly_precipitation_march)-sum(total_monthly_precipitation_feb))

 # find for more efficient way of getting months


month_sum_list = []
for month in range(1,13):
    month_sum = 0 
    for entry in seattle_station:
        if int(entry['date'].split('-')[1]) == month:
            month_sum = month_sum + entry['value']
    month_sum_list.append(month_sum)

print(month_sum_list)

#calculate yearly precipitation
yearly_precipitation = sum(month_sum_list)
print(yearly_precipitation)

#relative monthly precipitation 

relative_monthly_precipitation = []
for month_sum in month_sum_list:
    relative_month_sum= month_sum/yearly_precipitation
    relative_monthly_precipitation.append(relative_month_sum)
    print(relative_month_sum)
 
stats = {
    'month_sum_list' : month_sum_list,
    'relative_monthly_precipitation' : relative_monthly_precipitation,
    'yearly_precipitation' : yearly_precipitation
}
 
#json file
with open('result.json', 'w') as file:
    json.dump(stats, file, indent = 4)
