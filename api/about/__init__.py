import azure.functions as func
import json
from datetime import datetime

def main(req: func.HttpRequest) -> func.HttpResponse:

    student_data = {
        'name':       'Валентина',
        'email':      'vgrekova21@gmail.com',
        'specialty':  'Комп'ютерна інженерія',
        'skills':     ['Python', 'Azure', 'GitHub'],
        'labs_done':  2,
        'platform':   'Azure Static Web Apps (PaaS)',
        'deployed_at': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC'),
    }

    return func.HttpResponse(
        body=json.dumps(student_data, ensure_ascii=False, indent=2),
        mimetype='application/json',
        headers={'Access-Control-Allow-Origin': '*'}
    )