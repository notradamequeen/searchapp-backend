#!/bin/bash

echo "Flush the manage.py command it any"

while ! python manage.py flush --no-input 2>&1; do
  echo "Flusing django manage command"
  sleep 3
done

echo "Migrate the Database at startup of project"

# Wait for few minute and run db migraiton
python manage.py migrate
#    echo "Migration is in progress status"
#    sleep 3
# done

# while ! python manage.py load_initial_data  2>&1; do
#    echo "Load data"
#    sleep 120
# done

echo "Rebuild es index"
echo 'y' | python manage.py search_index --rebuild


echo "Django docker is fully configured successfully."

exec "$@"
