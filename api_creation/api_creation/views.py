from django.http import JsonResponse
from django.utils import timezone
import datetime
import os

def info_endpoint(request):
    slack_name = "George wambani"
    current_day = timezone.now().strftime("%A")
    current_time_utc = timezone.now()
    github_url_file = "https://github.com/your_repo/your_file.py"
    github_url_source = "https://github.com/your_repo"
    
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "current_utc_time": current_time_utc.strftime("%Y-%m-%d %H:%M:%S %Z"),
        "track": "Your Track",
        "github_url_file": github_url_file,
        "github_url_source": github_url_source,
    }
    
    return JsonResponse(response_data)
