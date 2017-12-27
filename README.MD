# Manual instalacyjny
## Instalacja virtualenv-a
```
virtualenv -p python3 env
```
## Aktywowanie virtualenva
```
. env/bin/active
```
## Instacja niezbędnych bibiotek
```
pip install -r requirements.txt
```
## Instacja migracja tabeli do wyników zadań
```
python manage.py migrate django_celery_results

```
## Instalacja migracji dla wyników zadań w tabeli History
```
python manage.py makemigrations celina
python manage.py migrate celina
```


## uruchamianie workera celery
```
celery -A celka worker -l info
```
gdzie:

- celka - to nazwa aplikacji
- worker - uruchomienie celery w trybie worker-a
- l - logowanie ustawione na info

## uruchomienie schedulera celery 
```
celery beat -A celka -l DEBUG
```
gdzie:
- celka - to nazwa aplikacji
- beat - uruchomienie celery w trybie schedulera
- l - logowanie ustawione na debug, aby było wszystko widać
## Uruchamianie webserwera
```
pyton manage.py runserver
```

# Działanie/wyświetlanie
## Główny widok

Po wejściu na stronę http://localhost:8000 powinno się zobaczyć listę zadań np.
```
<Task: e10956a3-5e82-4cbb-aaf1-57c9644fc34d (SUCCESS)> 67
<Task: 76e5392b-c389-4267-a531-effd50b6b2f2 (SUCCESS)> 116
<Task: 7c8dafc2-a60f-4840-a60a-9529b6df734b (SUCCESS)> 43
<Task: 2564d5b4-1ddd-4bb9-b285-0f90b33f33bf (SUCCESS)> 160
<Task: 01b49d0c-7597-4f92-8ee6-35e202e8f8e3 (SUCCESS)> 93
<Task: 634d1d27-5e6b-4df8-9eaa-cfbe7de7cbbf (SUCCESS)> 127
<Task: 86c621f9-87fb-4978-92bc-d0dd039c871f (SUCCESS)> 132
<Task: a98fa38e-d697-4398-8aac-435839307349 (SUCCESS)> 99
<Task: 24a7c83c-700c-4b68-ac0e-ab3f8822f80a (SUCCESS)> 100
```
oraz linki:

- Dodaj zadanie - zlec nowe zadanie zsumowanie 2 liczb całkowityc z zakresu 0 - 100 dodatkowo do tego zadania jest dołożony losowy sleep, aby zadanie wykonywało się trochę dłużej udawało, że jest to pracochłonna operacja.
- Dodaj 100 liczb do historii - dodaje 100 rekordów do bazy danych w pętli
- Dodaj 100 liczb do historii (jedną paczką) - dodaje 10 rekordów do bazy danych przy użyciu bulk_create

## Widok scheduler

```
celery beat -A celka -l DEBUG
celery beat v4.1.0 (latentcall) is starting.
__    -    ... __   -        _
LocalTime -> 2017-12-27 22:39:02
Configuration ->
    . broker -> sqla+sqlite:///celerydb.sqlite
    . loader -> celery.loaders.app.AppLoader
    . scheduler -> celery.beat.PersistentScheduler
    . db -> celerybeat-schedule
    . logfile -> [stderr]@%DEBUG
    . maxinterval -> 5.00 minutes (300s)
[2017-12-27 22:39:02,402: DEBUG/MainProcess] Setting default socket timeout to 30
[2017-12-27 22:39:02,404: INFO/MainProcess] beat: Starting...
[2017-12-27 22:39:02,440: DEBUG/MainProcess] Current schedule:
<ScheduleEntry: Roll the dice by 5s celka.celery.roll_the_dice() <freq: 5.00 seconds>
<ScheduleEntry: Roll the dice by 7s 5 times celka.celery.roll_the_dice() <freq: 7.00 seconds>
<ScheduleEntry: Roll the dice every 2 minutes celka.celery.roll_the_dice() <crontab: */2 * * * * (m/h/d/dM/MY)>
<ScheduleEntry: celery.backend_cleanup celery.backend_cleanup() <crontab: 0 4 * * * (m/h/d/dM/MY)>
[2017-12-27 22:39:02,440: DEBUG/MainProcess] beat: Ticking with max interval->5.00 minutes

```
## Resultat worker dla schedulera

```
[2017-12-27 22:44:56,458: INFO/MainProcess] Received task: celka.celery.roll_the_dice[8cec0b24-af25-438d-a546-5a4b19c5634c]  
[2017-12-27 22:44:56,478: INFO/ForkPoolWorker-4] Task celka.celery.roll_the_dice[8cec0b24-af25-438d-a546-5a4b19c5634c] succeeded in 0.017954696995730046s: 1
[2017-12-27 22:45:00,520: INFO/MainProcess] Received task: celka.celery.roll_the_dice[fa828cdf-0de9-4463-affd-5431426e9ddf]  
[2017-12-27 22:45:00,540: INFO/ForkPoolWorker-3] Task celka.celery.roll_the_dice[fa828cdf-0de9-4463-affd-5431426e9ddf] succeeded in 0.018824651000613812s: 3
[2017-12-27 22:45:05,600: INFO/MainProcess] Received task: celka.celery.roll_the_dice[86673eb3-70b3-434f-ade3-c8b1539d2b71]  
[2017-12-27 22:45:05,642: INFO/ForkPoolWorker-1] Task celka.celery.roll_the_dice[86673eb3-70b3-434f-ade3-c8b1539d2b71] succeeded in 0.04024314400157891s: 6
[2017-12-27 22:45:10,685: INFO/MainProcess] Received task: celka.celery.roll_the_dice[33063ba1-6899-4b66-86bc-fcde0aac1fc8]  
[2017-12-27 22:45:10,713: INFO/ForkPoolWorker-2] Task celka.celery.roll_the_dice[33063ba1-6899-4b66-86bc-fcde0aac1fc8] succeeded in 0.02643137300037779s: 5
[2017-12-27 22:45:10,726: INFO/MainProcess] Received task: celka.celery.roll_the_dice[de2bbfb3-60f0-460c-b2dd-bb6be53dbdc3]  
[2017-12-27 22:45:10,742: INFO/ForkPoolWorker-4] Task celka.celery.roll_the_dice[de2bbfb3-60f0-460c-b2dd-bb6be53dbdc3] succeeded in 0.014727758003573399s: 2
[2017-12-27 22:45:15,812: INFO/MainProcess] Received task: celka.celery.roll_the_dice[83606d68-904c-444e-ba5a-978020cae238]  
[2017-12-27 22:45:15,838: INFO/ForkPoolWorker-3] Task celka.celery.roll_the_dice[83606d68-904c-444e-ba5a-978020cae238] succeeded in 0.024320096003066283s: 3
[2017-12-27 22:45:17,871: INFO/MainProcess] Received task: celka.celery.roll_the_dice[4c7a9a85-5570-42f6-9ace-e082d4902f07]  
[2017-12-27 22:45:17,902: INFO/ForkPoolWorker-1] Task celka.celery.roll_the_dice[4c7a9a85-5570-42f6-9ace-e082d4902f07] succeeded in 0.02912110100442078s: 3
[2017-12-27 22:45:19,931: INFO/MainProcess] Received task: celka.celery.roll_the_dice[87d8230e-7ecb-41e5-b175-6de58f5646fb]  
[2017-12-27 22:45:19,957: INFO/ForkPoolWorker-2] Task celka.celery.roll_the_dice[87d8230e-7ecb-41e5-b175-6de58f5646fb] succeeded in 0.024823674000799656s: 2
[2017-12-27 22:45:23,993: INFO/MainProcess] Received task: celka.celery.roll_the_dice[f3212cac-b531-4d2a-acbc-e82c66689a8b]  
[2017-12-27 22:45:24,026: INFO/ForkPoolWorker-4] Task celka.celery.roll_the_dice[f3212cac-b531-4d2a-acbc-e82c66689a8b] succeeded in 0.031156958000792656s: 4
[2017-12-27 22:45:25,042: INFO/MainProcess] Received task: celka.celery.roll_the_dice[6beab278-323c-443e-9350-d04274052cc8]  
[2017-12-27 22:45:25,067: INFO/ForkPoolWorker-3] Task celka.celery.roll_the_dice[6beab278-323c-443e-9350-d04274052cc8] succeeded in 0.023017122999590356s: 6
[2017-12-27 22:45:30,135: INFO/MainProcess] Received task: celka.celery.roll_the_dice[3352f0d2-351e-48ff-b5cf-4901471c9496]  
[2017-12-27 22:45:30,161: INFO/ForkPoolWorker-1] Task celka.celery.roll_the_dice[3352f0d2-351e-48ff-b5cf-4901471c9496] succeeded in 0.02418703300645575s: 2
[2017-12-27 22:45:31,177: INFO/MainProcess] Received task: celka.celery.roll_the_dice[e7f1aa62-2872-495a-9ff2-dc56978fb679]  
[2017-12-27 22:45:31,206: INFO/ForkPoolWorker-2] Task celka.celery.roll_the_dice[e7f1aa62-2872-495a-9ff2-dc56978fb679] succeeded in 0.027063511006417684s: 4
[2017-12-27 22:45:35,246: INFO/MainProcess] Received task: celka.celery.roll_the_dice[8dc092d0-5cd1-42f4-8875-aa074716454a]  
[2017-12-27 22:45:35,267: INFO/ForkPoolWorker-4] Task celka.celery.roll_the_dice[8dc092d0-5cd1-42f4-8875-aa074716454a] succeeded in 0.01898105800501071s: 2
[2017-12-27 22:45:38,317: INFO/MainProcess] Received task: celka.celery.roll_the_dice[9887553a-6def-4df6-b2f3-743be92d3f07]  
[2017-12-27 22:45:38,338: INFO/ForkPoolWorker-3] Task celka.celery.roll_the_dice[9887553a-6def-4df6-b2f3-743be92d3f07] succeeded in 0.020020409996504895s: 4
[2017-12-27 22:45:40,363: INFO/MainProcess] Received task: celka.celery.roll_the_dice[492b9819-66e0-4ba2-92cd-735cb7d811b6]  
[2017-12-27 22:45:40,387: INFO/ForkPoolWorker-1] Task celka.celery.roll_the_dice[492b9819-66e0-4ba2-92cd-735cb7d811b6] succeeded in 0.021915597004408482s: 4
[2017-12-27 22:45:45,449: INFO/MainProcess] Received task: celka.celery.roll_the_dice[dce6d55d-7fb0-4e04-a480-740e3d932b3e]  
[2017-12-27 22:45:45,473: INFO/ForkPoolWorker-2] Task celka.celery.roll_the_dice[dce6d55d-7fb0-4e04-a480-740e3d932b3e] succeeded in 0.022281010998995043s: 1
[2017-12-27 22:45:45,488: INFO/MainProcess] Received task: celka.celery.roll_the_dice[f79b351e-715c-48bc-b39d-f940a11ab75d]  
[2017-12-27 22:45:45,507: INFO/ForkPoolWorker-4] Task celka.celery.roll_the_dice[f79b351e-715c-48bc-b39d-f940a11ab75d] succeeded in 0.016693198995199054s: 1

```

# Ostatnie słowo
## Zbudowane dzięki

* [Django](https://www.djangoproject.com/) - Web Framework
* [Celery](http://www.celeryproject.org/) - Rozproszona kolejka zadań :)
* [SQLite](https://www.sqlite.org/) - Silnik bazodanowy
