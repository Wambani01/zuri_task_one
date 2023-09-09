from django.http import JsonResponse
from django.utils import timezone
import datetime
import os


def info_endpoint(request):
    # Get the 'slack_name' and 'track' parameters from the URL
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')

    current_day = timezone.now().strftime("%A")
    current_time_utc = timezone.now()
    github_url_file = "https://github.com/your_repo/your_file.py"
    github_url_source = "https://github.com/your_repo"

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "current_utc_time": current_time_utc.strftime("%Y-%m-%d %H:%M:%S %Z"),
        "track": track,
        "github_url_file": "https://github.com/Wambani01/zuri_task_one/tree/main",
        "github_url_source": "https://github.com/Wambani01/zuri_task_one/tree/main",
    }

    return JsonResponse(response_data)
