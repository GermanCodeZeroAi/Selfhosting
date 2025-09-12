SHELL := /bin/bash
.PHONY: up down logs validate backup restore test lint format

up: validate
	docker compose up -d --build

down:
	docker compose down

logs:
	docker compose logs -f --tail=200

validate:
	python3 OPS/scripts/validate_registry.py

backup:
	docker compose exec -T postgres pg_dump -U $$POSTGRES_USER $$POSTGRES_DB > DATA/backups/backup_`date +%F_%H%M`.sql

restore:
	@if [ -z "$$FILE" ]; then echo "Usage: make restore FILE=DATA/backups/<file>.sql"; exit 1; fi
	docker compose exec -T postgres psql -U $$POSTGRES_USER $$POSTGRES_DB < $$FILE