# Project Overview
```bash
Text to image build with stability.ai API. this image creation task is running by django-celery.
create a new API key and add it in task.py authorization header.

```


# Install dependencies 
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

# Run the django Server and celery in separate CLI
```bash
python3 manage.py runserver
celery -A Text_to_Image worker -l info
```

# Provide the image prompt for image formation in views.py
```bash
example : prompt = ["Lighthouse on a cliff overlooking the ocean","Flying Snake"]
```

# Provide the redis server credentials in settings.py

# Make a request to the url specified in urls.py and check the project directory you would get the image.
```bash
http://localhost:8000/trigger-task/
```