#docker-compose app run -c sh "python manage.py $1"
docker-compose run app sh -c "python manage.py $1"
