from django.contrib import admin
from .models import Post, Comment


admin.site.register(Post)
admin.site.register(Comment)

'''
from django.utils.translation import ugettext_lazy as _
from .models import ProjectModel, ProblemModel, Comment, FileModel
from . import choices

class ProjectAdmin(admin.ModelAdmin):
	list_display = [ 'title', 'created',  'updated' ]
	# search_fields = [ 'title', 'email', 'created',  'updated' ]
	class Meta:
		model = ProjectModel



class ProblemSectionFilter(admin.SimpleListFilter):
	title = _('განყოფილების')
	parameter_name = 'section'

	def lookups(self, request, model_admin):
		return choices.SECTIONS

	def queryset(self, request, queryset):
		if self.value():
			return queryset.filter(section=self.value())
		return queryset



class ProblemStatusFilter(admin.SimpleListFilter):
	title = _('სტატუსის')
	parameter_name = 'status'

	def lookups(self, request, model_admin):
		return choices.STATUS

	def queryset(self, request, queryset):
		if self.value():
			return queryset.filter(status=self.value())
		return queryset


class ProblemPriorityFilter(admin.SimpleListFilter):
	title = _('პრიორიტეტულობის')
	parameter_name = 'priority'

	def lookups(self, request, model_admin):
		return choices.PRIORITY

	def queryset(self, request, queryset):
		if self.value():
			return queryset.filter(priority=self.value())
		return queryset


class ProblemAdmin(admin.ModelAdmin):
	list_filter = (ProblemSectionFilter, ProblemStatusFilter, ProblemPriorityFilter)

	list_display = [ 'title', 'created',  'updated', 'account' ]
	
	class Meta:
		model = ProblemModel



admin.site.register(ProblemModel, ProblemAdmin)
admin.site.register(ProjectModel, ProjectAdmin)
admin.site.register(Comment)
admin.site.register(FileModel)
'''



