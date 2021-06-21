# strona_sa

## utworzenie i aktywowanie środowiska wirtualnego oraz zainstalowanie pakietów

```bash
python3 -m venv srodowisko
source srodowisko/bin/activate
pip install -r requirements.txt
```

## zaaplikowanie migracji, utworzenie użytkownika administracyjnego (wymagane podanie danych) i uruchomienie serwera

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

projekt dostępny przez przeglądarkę pod adresem http://127.0.0.1:8000/
