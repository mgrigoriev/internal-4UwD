run:
	poetry run ./manage.py runserver
requirements:
	poetry export -f requirements.txt --output requirements.txt
