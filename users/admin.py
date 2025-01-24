from django.contrib import admin
from . import models as usermodels

class Admin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.fields]

admin.site.register(usermodels.CustomUser,Admin)
admin.site.register(usermodels.Education,Admin)
admin.site.register(usermodels.Experience,Admin)
admin.site.register(usermodels.Project,Admin)
admin.site.register(usermodels.Skill,Admin)
admin.site.register(usermodels.JobDescription,Admin)
admin.site.register(usermodels.Resume,Admin)
admin.site.register(usermodels.SimilarityScore,Admin)
