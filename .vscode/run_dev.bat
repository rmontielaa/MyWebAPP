@echo off
set DEBUG=true
set DJANGO_SECRET_KEY=mDMWU2bWCh2THffQZa2TKPcGuX6OcK28g9hQOtTLDsQ6czYuRs
set NAME=ejemplo
set USER=postgres
set PASSWORD=example
set HOST=127.0.0.1
set PORT=5432

if not defined VIRTUAL_ENV (
    call venv\Scripts\activate.bat
)

python mysite\manage.py runserver