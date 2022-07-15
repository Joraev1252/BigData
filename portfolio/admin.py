from django.contrib import admin
from portfolio.models import AnyProblemsModel, PortfolioModel, ContactUsModel, AskedQuestionsModel, OurTeamModel, OurPartnersModel, PartnersLogoModel
# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )
    list_display_links = ('id', 'title')
    search_fields = ('title', 'id', )
    list_filter = ('id',)


class TodoAdminContact(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'number', )
    list_display_links = ('id', 'full_name', )
    search_fields = ('number', 'id', 'full_name')
    list_filter = ('id',)


class TodoAdminQuestions(admin.ModelAdmin):
    list_display = ('id', 'question', )
    list_display_links = ('id', 'question', )
    search_fields = ('number', 'id', 'question')
    list_filter = ('id',)


admin.site.register(PortfolioModel, TodoAdmin)
admin.site.register(AnyProblemsModel, TodoAdmin)
admin.site.register(ContactUsModel, TodoAdminContact)

admin.site.register(AskedQuestionsModel, TodoAdminQuestions)
admin.site.register(OurTeamModel, TodoAdmin)

admin.site.register(OurPartnersModel, TodoAdmin)
admin.site.register(PartnersLogoModel)
