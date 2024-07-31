# myapp/views.py
from django.http import JsonResponse
from .task import texttoimage

def trigger_task(request):
    prompt = ["Lighthouse on a cliff overlooking the ocean","Flying Snake"]  # Replace with your desired prompt
    texttoimage(prompt)
    return JsonResponse({'message': 'Task completed successfully'})
