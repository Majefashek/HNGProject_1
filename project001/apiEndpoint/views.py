from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from datetime import datetime, timedelta
import pytz

class GetInfoView(View):
    def get(self, request):
        # Get query parameters from the request
        slack_name = request.GET.get('slack_name')
        track = request.GET.get('track')

        # Get current day of the week
        current_day = datetime.now().strftime('%A')
        utc_time = datetime.utcnow()

        # Calculate the Nigerian time by adding 1 hour (60 minutes)
        nigerian_time = utc_time + timedelta(minutes=60)

        # Format the time as a string with the Nigerian time zone offset
        nigerian_time_str = nigerian_time.strftime('%Y-%m-%dT%H:%M:%SZ')

        # Get current UTC time with a +/-2 minute window
       
        # Construct GitHub URLs
        github_file_url = "https://github.com/Majefashek/HNGProject_1/blob/main/project001/apiEndpoint/views.py"
        github_repo_url = "https://github.com/Majefashek/HNGProject_1"

        # Prepare the JSON response
        response = {
            "slack_name": slack_name,
            "current_day": current_day,
            "utc_time": nigerian_time_str,
            "track": track,
            "github_file_url": github_file_url,
            "github_repo_url": github_repo_url,
            "status_code": 200
        }

        return JsonResponse(response)

