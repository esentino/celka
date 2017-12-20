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
## uruchamianie workera celery
```
celery -A celka worker -l info
```
gdzie:

- celka - to nazwa aplikacji
- worker - uruchomienie celery w trybie worker-a
- l - logowanie ustawione na info

## Uruchamianie webserwera
```
pyton manage.py runserver
```

# Działanie/wyświetlanie
## Główny widok

Po wejściu na stronę http://localhost:8000 powinno się zobaczyć listę zadań np.

<Task: e10956a3-5e82-4cbb-aaf1-57c9644fc34d (SUCCESS)> 67

<Task: 76e5392b-c389-4267-a531-effd50b6b2f2 (SUCCESS)> 116

<Task: 7c8dafc2-a60f-4840-a60a-9529b6df734b (SUCCESS)> 43

<Task: 2564d5b4-1ddd-4bb9-b285-0f90b33f33bf (SUCCESS)> 160

<Task: 01b49d0c-7597-4f92-8ee6-35e202e8f8e3 (SUCCESS)> 93

<Task: 634d1d27-5e6b-4df8-9eaa-cfbe7de7cbbf (SUCCESS)> 127

<Task: 86c621f9-87fb-4978-92bc-d0dd039c871f (SUCCESS)> 132

<Task: a98fa38e-d697-4398-8aac-435839307349 (SUCCESS)> 99

<Task: 24a7c83c-700c-4b68-ac0e-ab3f8822f80a (SUCCESS)> 100

oraz link, która zleca nowe zadanie zsumowanie 2 liczb całkowityc z zakresu 0 - 100 dodatkowo do tego zadania jest dołożony losowy sleep, aby zadanie wykonywało się trochę dłużej udawało, że jest to pracochłonna operacja.  