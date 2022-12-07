from django.contrib import admin
from .models import Mistake, Exercise_Model, Learned_Word, Learned_Context

admin.site.register(Mistake)
admin.site.register(Exercise_Model)
admin.site.register(Learned_Word)
admin.site.register(Learned_Context)
