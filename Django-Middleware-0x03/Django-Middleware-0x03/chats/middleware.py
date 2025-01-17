from datetime import datetime
from django.http import HttpResponseForbidden


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
     
        user = request.user if request.user.is_authenticated else "Anonymous"
        log_entry = f"{datetime.datetime.now()} - User: {user} - Path: {request.path}\n"

        # Write log entry to a file
        with open("requests.log", "a") as log_file:
            log_file.write(log_entry)

        
        response = self.get_response(request)
        return response

class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the current time in 24-hour format
        current_hour = datetime.now().hour

        # Define allowed access hours (9 AM to 6 PM)
        if current_hour < 9 or current_hour > 18:
            return HttpResponseForbidden("Access to the messaging app is restricted outside 9:00 AM to 6:00 PM.")

        response = self.get_response(request)
        return response

