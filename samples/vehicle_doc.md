# Vehicle Alert API

POST /vehicles/alert

Creates an alert for a vehicle.

Body:
- voltage
- engine_temp

Responses:
- 200 OK
- 400 Bad Request
- 429 Too Many Requests
- 500 Server Error
