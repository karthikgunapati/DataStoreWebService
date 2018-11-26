
"""
Request arguments for the services provided through the Web API
"""

employee_by_ids_args = [
            {
                "name": "results_per_page",
                "type": int,
                "default": 2,
                "location": "args"
            },
            {
                "name": "cursor",
                "type": str,
                "default": None,
                "location": "args"
            },
            {
                "name": "ids",
                "type": str,
                "action": "append",
                "required": True,
                "location": "args"
            }
        ]

employee_search_args = [
            {
                "name": "results_per_page",
                "type": int,
                "default": 2,
                "location": "args"
            },
            {
                "name": "cursor",
                "type": str,
                "default": None,
                "location": "args"
            },
            {
                "name": "companyName",
                "type": str,
                "required": True,
                "location": "args"
            },
            {
                "name": "lastName",
                "type": str,
                "required": True,
                "location": "args"
            }
        ]

employee_by_service_args = [
            {
                "name": "results_per_page",
                "type": int,
                "default": 2,
                "location": "args"
            },
            {
                "name": "cursor",
                "type": str,
                "default": None,
                "location": "args"
            }
        ]


employee_by_territory_args = [
            {
                "name": "results_per_page",
                "type": int,
                "default": 2,
                "location": "args"
            },
            {
                "name": "cursor",
                "type": str,
                "default": None,
                "location": "args"
            }
        ]

employee_by_company_args = [
            {
                "name": "results_per_page",
                "type": int,
                "default": 2,
                "location": "args"
            },
            {
                "name": "cursor",
                "type": str,
                "default": None,
                "location": "args"
            }
        ]

crud_employee_args = [
            {
                "name": "lastName",
                "type": str,
                "required": True,
                "location": "json"
            },
            {
                "name": "firstName",
                "type": str,
                "required": True,
                "location": "json"
            },
            {
                "name": "territoryName",
                "type": str,
                "required": True,
                "location": "json"
            },
            {
                "name": "companyName",
                "type": str,
                "required": True,
                "location": "json"
            },
            {
                "name": "serviceName",
                "type": str,
                "required": True,
                "location": "json"
            },
            {
                "name": "id",
                "type": str,
                "required": True,
                "location": "json"
            }
        ]
