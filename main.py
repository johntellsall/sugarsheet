from pysugarcrm import sugar_api

with sugar_api("http://testserver.com/", "admin", "12345") as api:
    data = api.get(
        "/Employees",
        query_params={"max_num": 2, "offset": 2, "fields": "user_name,email"},
    )
    api.post(
        "/Leads",
        json={
            "first_name": "John",
            "last_name": "Smith",
            "business_name_c": "Test John",
            "contact_email_c": "john@smith.com",
        },
    )

# Once we exit the context manager the sugar connection is closed and the user is logged out

