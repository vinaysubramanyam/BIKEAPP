from django.contrib import admin
from bike.models import Category,Page
from bike.models import UserProfile

# Register your models here.
# from .models import SignUp 


# from .forms import SignUpForm

# class SignUpAdmin(admin.ModelAdmin):
# 	list_display = ("__str__", "timestamp", "updated")
# 	form = SignUpForm
# #	class Meta:
# #		model = SignUp
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}



# admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Category)
admin.site.register(Page)
admin.site.register(UserProfile)



