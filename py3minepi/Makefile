build:
	docker build -t py3minepi .
run:
	docker run -t -d --name py3minepi --network host py3minepi
python:
	docker cp ./index.py py3minepi:/; docker exec -it py3minepi python /index.py;
rm:
	docker stop py3minepi; docker rm py3minepi;