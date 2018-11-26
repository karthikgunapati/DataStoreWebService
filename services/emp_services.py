"""
All the services regarding the employee details
"""

from flask import jsonify, make_response, request
from flask_restful import Resource, abort
from google.appengine.ext import ndb
from models.emp_models import Service, Employee, Company, Territory
from utils.basic_utils import generate_url, req_parser
from service_args.emp_service_args import *


class employee_by_id(Resource):
    """
    this resource takes the list of ids of an employee and return their details

    Returns: json
    """
    def get(self):  
        args = req_parser(*employee_by_ids_args)
        cursor = ndb.Cursor(urlsafe=args['cursor'])
        query = Employee.query().order(Employee.key).filter(Employee.email.IN (list(set(args['ids']))))
        rslt, nxt_cursor, more = query.fetch_page(args['results_per_page'], start_cursor=cursor)
        return jsonify({
            "data": [r.to_dict() for r in rslt],
            "next": generate_url(request.url, nxt_cursor.urlsafe() if more else None),
            "results_per_page": args['results_per_page']
        })


class employee_by_lastname(Resource):
    """
    this resource takes the 'company' and 'lastname' of an employee
    full/partial lastname and the returns the matching results

    Returns: json
    """
    def get(self):
        args = req_parser(*employee_search_args)
        cursor = ndb.Cursor(urlsafe=args['cursor'])
        query = Employee.query(ancestor=Company.query(Company.name == args['companyName']).get().key)
        q_iter = query.iter(**{"produce_cursors": True, "start_cursor": cursor})
        rslt = list()
        for r in q_iter:
            if r.lastName.startswith(args['lastName']):
                rslt.append(r.to_dict())
            if len(rslt) == args['results_per_page']:
                break
        if len(rslt) == 0:
            return make_response(jsonify({"message": "No content available"}), 204)
        cursor = q_iter.cursor_after().urlsafe() if q_iter.has_next() else None
        return jsonify({
            "data": rslt, "next": generate_url(request.url, cursor),
            "results_per_page": args['results_per_page']
            })


class employee_by_service(Resource):
    """
    resource URL contains the <service-name> passed as string by which
    the the employee datils are returned accordingly

    Return: json
    """
    def get(self, service):
        args = req_parser(*employee_by_service_args)
        cursor = ndb.Cursor(urlsafe=args['cursor'])
        query = Employee.query(ancestor=Service.query(Service.name == service).get().key)
        rslt, nxt_cursor, more = query.fetch_page(args['results_per_page'], start_cursor=cursor)
        return jsonify({
            "data": [r.to_dict() for r in rslt],
            "next": generate_url(request.url, nxt_cursor.urlsafe() if more else None),
            "results_per_page": args['results_per_page']
        })


class employee_by_territory(Resource):
    """
    resource URL contains the <territory-name> passed as string by which
    the the employee details are returned accordingly

    Return: json
    """
    def get(self, territory):
        args = req_parser(*employee_by_territory_args)
        cursor = ndb.Cursor(urlsafe=args['cursor'])
        query = Employee.query(ancestor=Territory.query(Territory.name == territory).get().key)
        rslt, nxt_cursor, more = query.fetch_page(args['results_per_page'], start_cursor=cursor)
        return jsonify({
            "data": [r.to_dict() for r in rslt],
            "next": generate_url(request.url, nxt_cursor.urlsafe() if more else None),
            "results_per_page": args['results_per_page']
        })


class employee_by_company(Resource):
    """
    resource URL contains the <company-name> passed as string by which
    the the employee details are returned accordingly

    Return: json
    """
    def get(self, company):
        args = req_parser(*employee_by_company_args)
        cursor = ndb.Cursor(urlsafe=args['cursor'])
        query = Employee.query(ancestor=Company.query(Company.name == company).get().key)
        rslt, nxt_cursor, more = query.fetch_page(args['results_per_page'], start_cursor=cursor)
        return jsonify({
            "data": [r.to_dict() for r in rslt],
            "next": generate_url(request.url, nxt_cursor.urlsafe() if more else None),
            "results_per_page": args['results_per_page']
        })
        

class employee(Resource):
    """
    Resource accepts request as a json having the keys lname, fname, company,
    territory, service by which a new user can be added as an entity in datastore

    Returns: 1.'json' with status 409 if user already exists
             2.'json' with status 201 with the unique user_id
    """
    def post(self):
        args = req_parser(*crud_employee_args)
        key = Service.query(Service.name == args['serviceName']).get()
        if Employee.query(Employee.email==args['id'], ancestor=key.key if key else None).get() is not None:
            abort(409, message="Employee with Username '{0}' already exists".format(args['id']))
        else:
            com = Company(id=args['companyName'], name=args['companyName'])
            com.put()
            terr = Territory(id=args['territoryName'], name=args['territoryName'], parent=com.key)
            terr.put()
            serv = Service(id=args['serviceName'], name=args['serviceName'], parent=terr.key)
            serv.put()
            emp = Employee(
                firstName=args["firstName"], id=args['id'], email=args['id'],
                lastName=args["lastName"], parent=serv.key).put()
            resp = jsonify({"Message": "Empoyee added created with id '{0}'".format(emp.id())})
            return make_response(resp, 201)
