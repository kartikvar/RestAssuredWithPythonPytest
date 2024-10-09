create_booking_valid_data = {
    "firstname": "Swapnil",
    "lastname": "Rawat",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2025-01-01",
        "checkout": "2025-01-01"
    },
    "additionalneeds": "Breakfast"
}

create_booking_invalid_data = [
    {
        "firstname": 123,
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    },
    {
        "firstname": "",
        "lastname": "",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "",
            "checkout": ""
        },
        "additionalneeds": "Breakfast"
    }
]
