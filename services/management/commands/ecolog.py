import json
import os
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Prints the content of a JSON log file.'
    
    
    def handle(self, *args, **options):
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        QueuePath = os.path.join(project_root, 'Data', 'analyze')
        try:
            with open(os.path.join(QueuePath, "Status.json"), 'r', encoding='utf-8') as file:
                log = json.load(file)
                status = log["Status"]
                if status:
                    self.stdout.write(json.dumps(status, indent=4, ensure_ascii=False))
                    
        except Exception as e:
            print(
                f"there is an Error with Status.json; {e}")
        
            
