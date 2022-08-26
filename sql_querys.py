# INFO
# Вывести топ 5 самых коротких по длительности перелетов.  Duration - разница между scheduled_arrival и scheduled_departure.
# В ответе должно быть 2 колонки [flight_no, duration]
TASK_1_QUERY = """
select flight_no , scheduled_arrival - scheduled_departure duration  from flights f 
order by 2
limit 5
"""

#  flight_no | duration
# -----------+----------
#  PG0235    | 00:25:00
#  PG0234    | 00:25:00
#  PG0233    | 00:25:00
#  PG0235    | 00:25:00
#  PG0234    | 00:25:00


# INFO
# Вывести топ 3 рейса по числу упоминаний в таблице flights
# количество упоминаний которых меньше 50
# В ответе должно быть 2 колонки [flight_no, count]
TASK_2_QUERY = """
select flight_no, count(*)
from flights f 
group by flight_no 
having count(*) < 50
order by 2 desc
limit 3
"""
#  flight_no | count
# -----------+-------
#  PG0260    |    27
#  PG0371    |    27
#  PG0310    |    27

# INFO
# Вывести число перелетов внутри одной таймзоны
# Нужно вывести 1 значение в колонке count
TASK_3_QUERY = """
select count(*) from flights f  
join airports_data ad on f.departure_airport = ad.airport_code 
join airports_data ad2 on f.arrival_airport = ad2.airport_code 
where ad.timezone  = ad2.timezone  
"""
#  count
# --------
#  16824
