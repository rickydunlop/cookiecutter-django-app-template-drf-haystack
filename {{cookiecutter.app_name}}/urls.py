# from django.conf.urls import include, url
from rest_framework import routers

from .views import {{ cookiecutter.model_name }}ViewSet

router = routers.SimpleRouter()
router.register(r'{{ cookiecutter.app_name }}', {{ cookiecutter.model_name }}ViewSet)

urlpatterns = [
]
