
# Домашнее задание к занятию "5.3. Введение. Экосистема. Архитектура. Жизненный цикл Docker контейнера"

---

## Задача 1

Сценарий выполения задачи:

- создайте свой репозиторий на https://hub.docker.com;
- выберете любой образ, который содержит веб-сервер Nginx;
- создайте свой fork образа;
- реализуйте функциональность:
запуск веб-сервера в фоне с индекс-страницей, содержащей HTML-код ниже:
```
<html>
<head>
Hey, Netology
</head>
<body>
<h1>I’m DevOps Engineer!</h1>
</body>
</html>
```
Опубликуйте созданный форк в своем репозитории и предоставьте ответ в виде ссылки на https://hub.docker.com/username_repo.


Ссылка на репозиторий \
<https://hub.docker.com/r/yakimov778/nginx>
## Задача 2

Посмотрите на сценарий ниже и ответьте на вопрос:
"Подходит ли в этом сценарии использование Docker контейнеров или лучше подойдет виртуальная машина, физическая машина? Может быть возможны разные варианты?"

Детально опишите и обоснуйте свой выбор.

--

Сценарий:

#### Высоконагруженное монолитное java веб-приложение;
Приложение монолитное, поэтому использование Docker не принесет каких-либо существенных преимуществ, возможно, лучше использовать физический сервер
#### Nodejs веб-приложение;
Подойдет контейнер Docker  так как быстрота развертывания, масштабируемость, производительность, независимость от инфрастуктуры и т.д.
#### Мобильное приложение c версиями для Android и iOS;
Для Android подойдет Docker; iOS - физический хост, так как разработка возможна только в пределах macOS. 
#### Шина данных на базе Apache Kafka;
Docker (для масштабирования)
#### Elasticsearch кластер для реализации логирования продуктивного веб-приложения - три ноды elasticsearch, два logstash и две ноды kibana;
Тоже Docker
#### Мониторинг-стек на базе Prometheus и Grafana;
Docker подходит, так как данный стек не требователен к ресурсам. Контейнеризация позволит легко его масштабировать
#### MongoDB, как основное хранилище данных для java-приложения;
Виртуальная машина или физический сервер, так как требуется производительность. Контейнер можно использовать для невысоконагруженных БД
#### Gitlab сервер для реализации CI/CD процессов и приватный (закрытый) Docker Registry.
Достаточно контейнера

## Задача 3

- Запустите первый контейнер из образа ***centos*** c любым тэгом в фоновом режиме, подключив папку ```/data``` из текущей рабочей директории на хостовой машине в ```/data``` контейнера;
- Запустите второй контейнер из образа ***debian*** в фоновом режиме, подключив папку ```/data``` из текущей рабочей директории на хостовой машине в ```/data``` контейнера;
- Подключитесь к первому контейнеру с помощью ```docker exec``` и создайте текстовый файл любого содержания в ```/data```;
- Добавьте еще один файл в папку ```/data``` на хостовой машине;
- Подключитесь во второй контейнер и отобразите листинг и содержание файлов в ```/data``` контейнера.
```bash
 ✘  ~/DevOps/docker  docker run -it -d -v $(pwd)/data:/data --name centos centos tail -f /dev/null
Unable to find image 'centos:latest' locally
latest: Pulling from library/centos
52f9ef134af7: Already exists
Digest: sha256:a27fd8080b517143cbbbab9dfb7c8571c40d67d534bbdee55bd6c473f432b177
Status: Downloaded newer image for centos:latest
c6b2adbc4763f4db7c58903f96c79d05156240a399259936197b21dc59721b43

 ~/DevOps/docker  docker run -it -d -v $(pwd)/data:/data --name debian debian tail -f /dev/null
Unable to find image 'debian:latest' locally
latest: Pulling from library/debian
b04fae59f135: Already exists
Digest: sha256:432f545c6ba13b79e2681f4cc4858788b0ab099fc1cca799cc0fae4687c69070
Status: Downloaded newer image for debian:latest
44a6ee451f8e6347e8e95961b614c6b708954da2dd8d07b69072f5f57a69cadc 

 ~/DevOps/docker  docker exec -it c6b2adbc4763 bash

[root@c6b2adbc4763 /]# echo "test text centos" > data/centos.txt

[root@c6b2adbc4763 /]# exit
exit
 
 ~/DevOps/docker  echo "---" > data/1.tx
 
 ~/DevOps/docker  docker exec -ti debian bash

root@44a6ee451f8e:/# ls data/
1.tx  centos.txt
```
