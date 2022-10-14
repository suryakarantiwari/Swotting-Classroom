from django.contrib import admin
from .models import Teacher
from .models import OS_Assignment
from .models import Project_Assignment
from .models import Java_Assignment
from .models import Ooad_Assignment
from .models import Cn_Assignment
# Register your models here.

admin.site.register(Teacher)
admin.site.register(OS_Assignment)
admin.site.register(Project_Assignment)
admin.site.register(Java_Assignment)
admin.site.register(Ooad_Assignment)
admin.site.register(Cn_Assignment)
