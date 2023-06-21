from django.contrib import admin

from polls.models import Question, Choice

# Register your models here. 테이블에 CRUD를 할 수 있게 하는 명령어
admin.site.register(Question)
admin.site.register(Choice)
