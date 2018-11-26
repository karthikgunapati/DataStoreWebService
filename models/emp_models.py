"""
This file will have all the models regarding the Employees
"""

from google.appengine.ext import ndb


class Company(ndb.Model):
    """
    This has all the company names in it
    """
    name = ndb.StringProperty()

class Territory(ndb.Model):
    """
    This has all the territory names in it and should be used
    with parent as Company
    """
    name = ndb.StringProperty()

class Service(ndb.Model):
    """
    This has all the service names in it and should be used
    with parent as Territory
    """
    name = ndb.StringProperty()

class Employee(ndb.Model):
    """
    This has all the employee details in it and should be used
    with parent as Service
    """
    email = ndb.StringProperty(required=True)
    firstName = ndb.StringProperty(required=True)
    lastName = ndb.StringProperty(required=True)
