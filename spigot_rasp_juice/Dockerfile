FROM openjdk:17.0.2-oraclelinux8 

LABEL maintainer="Petr Laptev <bastsoft@yandex.ru>"

ARG SPIGOT_VER=1.18
ARG RASPBERRYJUICE_VER=1.12.1
ENV SPIGOT_VER ${SPIGOT_VER}
ENV MC_MINMEM 512M
ENV MC_MAXMEM 1536M

WORKDIR /minecraft
RUN microdnf install git
# cервер spigot
ADD https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar buildtools.jar
RUN java -Xmx1024M -jar buildtools.jar --rev ${SPIGOT_VER}
# Плагин для spigot для Minecraft Pi API
ADD https://github.com/zhuowei/RaspberryJuice/raw/master/jars/raspberryjuice-${RASPBERRYJUICE_VER}.jar plugins/raspberryjuice-${RASPBERRYJUICE_VER}.jar
RUN java -jar spigot-${SPIGOT_VER}.jar nogui
RUN sed -i -e '/eula=/s/=.*/=true/' eula.txt
RUN sed -i -e '/online\-mode=/s/=.*/=false/' server.properties
RUN sed -i -e '/gamemode=/s/=.*/=creative/' server.properties
RUN sed -i -e '/allow\-flight=/s/=.*/=true/' server.properties
RUN echo "level-type=FLAT" >> server.properties

# порт сервера spigot
EXPOSE 25565
# порт raspberryjuice
EXPOSE 4711

#java -Xms512M -Xmx1536M -jar spigot-1.18.jar --plugins /plugins
CMD java -Xms${MC_MINMEM} -Xmx${MC_MAXMEM} -jar spigot-${SPIGOT_VER}.jar
