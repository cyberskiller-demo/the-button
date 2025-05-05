import time

from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    return render(request, "index.html")


def ping(request):
    version = os.environ.get("VERSION", "dev")
    return JsonResponse({"message": f"pong {time.time()}", "version": version})

