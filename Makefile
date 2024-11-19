createuser:
	python manage.py createsuperuser

rmmigration:
	rm -rf api/**/migrations/0*
# Help DB
# SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE pg_stat_activity.datname = 'test' AND pid <> pg_backend_pid(); DROP DATABASE IF EXISTS "test"; CREATE DATABASE IF NOT EXISTS "test" WITH OWNER = test ENCODING = "UTF8" LOCALE_PROVIDER = "libc" CONNECTION LIMIT = -1 IS TEMPLATE = False;

virtualenv:
	export PYTHONPATH="$PYTHONPATH:$PWD/venv/lib/python3.12/site-packages"

env:
	cp .env-example .env

nix:
	sudo nix-shell

initvenv:
	sh run.sh

create_env:
	virtualenv -p python3.12 venv

req:
	pip install -r requirements.txt

pyrun:
	python manage.py runserver

up:
	docker compose up --remove-orphans mysql

down:
	docker compose down --remove-orphans

prune:
	docker system prune -f

image:
	docker compose up erp_api --build

	