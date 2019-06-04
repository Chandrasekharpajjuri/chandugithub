from django.contrib import admin

from .models import Curdmodel1,EmailSendModel
class CurdAdmin(admin.ModelAdmin):
    list_display=['Select','Ename','Subject','Sal','Date_of_birth','Gender','Distric','Technologies','Search','File','User_Image','Passed']
    
admin.site.register(Curdmodel1,CurdAdmin)


class EmailSendAdmin(admin.ModelAdmin):
    list_display=['From','To','Subject','Attach','Message']
admin.site.register(EmailSendModel,EmailSendAdmin)

