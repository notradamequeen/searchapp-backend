#!/bin/bash

echo "Migrate the Database at startup of project"
python manage.py migrate
sleep 60
echo "Rebuild es index"
echo 'y' | python manage.py search_index --rebuild

echo "Django docker is fully configured successfully."

exec "$@"
