#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LightMail.settings")

    from django.core.management import execute_from_command_line

    if 'livereload' in sys.argv:
        from django.core.wsgi import get_wsgi_application
        from livereload import Server
        application = get_wsgi_application()
        server = Server(application)
        server.watch('Mail/templates/Mail/*.html')
        server.watch('Mail/views.py')
        server.watch('Mail/css/*.css')
        server.serve()
    else:
        execute_from_command_line(sys.argv)

