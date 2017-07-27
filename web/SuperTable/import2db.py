import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SuperTable.settings")

import django
if django.VERSION >= (1,7):
    django.setup()

from table.models import SearchResult

if __name__ == '__main__':
    print("DONE")
    