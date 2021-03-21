from apps.tenant_db import models

buildings = [
    models.Building(
        street_number = "25",
        street_name = "Mabelle Ave.",
        postal_code = "M4C3C2"
    )
]

events = [
    models.Event(
        name = "Catan Party",
        location = "My pad",
        description = "byob"
    )
]

contacts = [
    models.Contact(
        first_name = "KRS",
        last_name = "-One",
    )
]

attendances = [
    models.Attendance(
        event = events[0],
        contact = contacts[0],
        result = models.CallResult.NO
    )
]
