@echo off
setlocal
cd /d "%~dp0"
if exist ".venv\Scripts\python.exe" goto ready
py -m venv .venv
if errorlevel 1 goto error
:ready
.venv\Scripts\python.exe -m pip install -r requirements.txt
if errorlevel 1 goto error
.venv\Scripts\python.exe manage.py migrate
if errorlevel 1 goto error
.venv\Scripts\python.exe manage.py shell -c "from django.contrib.auth import get_user_model; raise SystemExit(0 if get_user_model().objects.filter(is_superuser=True).exists() else 1)"
if not errorlevel 1 goto server
echo Crea il tuo account amministratore personale.
.venv\Scripts\python.exe manage.py createsuperuser
if errorlevel 1 goto error
:server
echo Apri http://127.0.0.1:8000/ nel browser.
.venv\Scripts\python.exe manage.py runserver
goto end
:error
echo Avvio non riuscito. Controlla Python e la connessione Internet. Vedi README.md.
pause
:end
