from django.contrib import admin

from .models import {{ cookiecutter.model_name }}


@admin.register({{ cookiecutter.model_name }})
class {{ cookiecutter.model_name }}Admin(admin.ModelAdmin):
    pass
