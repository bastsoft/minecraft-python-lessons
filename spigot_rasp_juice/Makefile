start:
	docker start spigot
stop:
	docker stop spigot
exec:
	docker exec -it spigot sh
rm:
	docker stop spigot; docker rm spigot;
rmi: 
	docker rmi spigot_rasp_juice:1_18
build:
	docker build -t spigot_rasp_juice:1_18 .
run:
	docker run -t -d -p 25565:25565 -p 4711:4711 --name spigot spigot_rasp_juice:1_18
logs:
	 docker logs -f spigot