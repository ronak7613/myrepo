from django.contrib import admin
from .models import Data, myUser
from .models import subregion,table_TapTyag,table_Swadhyay

# Register your models here
admin.site.register(subregion)
admin.site.register(table_TapTyag)
admin.site.register(table_Swadhyay)

# Register the Data model
admin.site.register(Data)

# Define a custom admin for CustomUser
class myUserAdmin(admin.ModelAdmin):
   list_display = ['username', 'is_admin', 'is_regional_head', 'is_activity_head', 'is_sub_regional_head', 'region', 'activity', 'sub_region']

# Register the CustomUser model with the custom admin
admin.site.register(myUser, myUserAdmin)
