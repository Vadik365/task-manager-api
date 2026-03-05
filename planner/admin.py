from django.contrib import admin
from .models import Category, Goal, Task


# Register your models here.
admin.site.register(Category)
admin.site.register(Task)

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    exclude = ('user',)

    def save_model(self, request, obj, form, change):
        if not obj.pk: #if create new subject
            obj.user = request.user
        super().save_model(request, obj, form, change)
