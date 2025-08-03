from django.core.management.base import BaseCommand
import subprocess
import os
import sys


class Command(BaseCommand):
    help = 'Runs both Django server and a separate Python script.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--port', type=int, default=8000
        )

    def handle(self, *args, **options):
        port = options['port']
        project_root = os.path.abspath(os.path.join(
            os.path.dirname(__file__), '..', '..'))
        localAiPath = os.path.join(
            project_root, 'Local_AI_Models', 'Insight.py')
        print('script path::: ', localAiPath)

        self.stdout.write(self.style.SUCCESS('Starting Local AI server'))
        other_script_process = subprocess.Popen([sys.executable, localAiPath])

        self.stdout.write(self.style.SUCCESS('Starting Django server...'))
        django_server_process = subprocess.Popen(
            [sys.executable, 'manage.py', 'runserver', str(port)])

        try:

            django_server_process.wait()
            other_script_process.wait()
        except KeyboardInterrupt:
            django_server_process.terminate()
            other_script_process.terminate()
            self.stdout.write(self.style.SUCCESS('Both processes terminated.'))
