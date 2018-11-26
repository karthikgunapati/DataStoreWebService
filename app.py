
"""
Main class for initializing and running the App
"""

import appengine_config
from flask import Flask
from flask_restful import Api
from Exceptions.error_config import errors
from services.emp_services import (
    employee,
    employee_by_company,
    employee_by_service,
    employee_by_territory,
    employee_by_lastname, employee_by_id
    )

app = Flask(__name__)
api = Api(app, catch_all_404s=True, errors=errors)

# adding all the resouces created
api.add_resource(employee, '/employees')
api.add_resource(employee_by_company, '/employees/by_company/<company>')
api.add_resource(employee_by_service, '/employees/by_service/<service>')
api.add_resource(employee_by_territory, '/employees/by_territory/<territory>')
api.add_resource(employee_by_id, '/employees/by_ids')
api.add_resource(employee_by_lastname, '/employees/by_lastname')
