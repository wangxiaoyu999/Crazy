#_*_coding:utf-8_*_
__author__ = 'jieli'
import os,sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Crazy.settings")
    import django
    django.setup()
    from django.conf import settings
    from backend import main

    # print(settings)
    main.call(sys.argv[1:])




