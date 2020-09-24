import os
import time
from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            self.stdout.write(
                self.style.WARNING("start load initial data ---")
            )
            self.load_initial_data()
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"failed load initial data --- {e}")
            )
        self.stdout.write(
            self.style.SUCCESS("initial data successfully loaded---")
        )

    def load_initial_data(self):
        file_path = os.path.join(settings.BASE_DIR, 'db_script/codinghw2.sql')
        sql_statements = open(file_path).readlines()
        per_batch = 100000
        first = 0
        last = per_batch
        batch_num = len(sql_statements) // per_batch
        last_batch = len(sql_statements) % per_batch
        if last_batch > 0:
            batch_num += 1
        for batch in range(0, batch_num):
            print('btach', batch)
            if batch == (batch_num):
                sql_statement = sql_statements[first:]
            else:
                sql_statement = sql_statements[first:last]

            with connection.cursor() as c:
                c.execute(''.join(sql_statement))

            first = last
            last += per_batch
            time.sleep(5)
