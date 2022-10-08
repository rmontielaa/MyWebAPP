@echo off
set DEBUG=true
set DJANGO_SECRET_KEY=mDMWU2bWCh2THffQZa2TKPcGuX6OcK28g9hQOtTLDsQ6czYuRs

if not defined VIRTUAL_ENV (
    call venv\Scripts\activate.bat
)

python mysite\manage.py shell_plus --ipython