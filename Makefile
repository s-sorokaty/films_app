start_project:
	cp .example.env .env
	docker-compose up --build -d --force-recreate
down_project:
	cp .example.env .env
	docker-compose down 