from django.contrib import admin
from .models import Student
from .models import Os_UploadAssignment
from .models import CN_UploadAssignment
from .models import Project_UploadAssignment
from .models import Java_UploadAssignment
from .models import OOAD_UploadAssignment

# Register your models here.
admin.site.register(Student)
admin.site.register(Os_UploadAssignment)
admin.site.register(CN_UploadAssignment)
admin.site.register(Project_UploadAssignment)
admin.site.register(Java_UploadAssignment)
admin.site.register(OOAD_UploadAssignment)
