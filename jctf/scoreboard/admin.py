from django.contrib import admin
from .models import User, Problem, Hint

admin.site.register(User)
admin.site.register(Problem)
admin.site.register(Hint)

