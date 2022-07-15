from django.contrib import admin
from about_us.models import AboutUsModel, OurGeneralStatisticsModel, OurCoursesModel
# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )
    list_display_links = ('id', 'title')
    search_fields = ('title', 'id', 'subtitle')
    list_filter = ('id',)


class TodoAdminAbout(admin.ModelAdmin):
    list_display = ('id', 'body', 'phone_number', )
    list_display_links = ('id', 'body', )
    search_fields = ('body', 'id', 'phone_number')
    list_filter = ('id',)


admin.site.register(OurCoursesModel, TodoAdmin)
admin.site.register(OurGeneralStatisticsModel, TodoAdmin)
admin.site.register(AboutUsModel, TodoAdminAbout)
