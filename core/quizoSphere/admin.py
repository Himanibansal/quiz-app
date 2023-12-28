from django.contrib import admin
from .models import *

admin.site.register(quiz)
admin.site.register(Question)
admin.site.register(Options)