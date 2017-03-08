from django.contrib import admin
from .models import User


admin.site.register(User)


'''
from django.utils.translation import ugettext_lazy as _
from .models import Account, Department, UserImage
from django.db.models import Q
'''

'''
class AccountActiveFilter(admin.SimpleListFilter):
	title = _('სტატუსის')
	parameter_name = 'is_active'

	def lookups(self, request, model_admin):
		return (
			("active", _("აქტიური")),
			("pending", _("არა აქტიური")),
		)

	def queryset(self, request, queryset):
		if self.value() == "active":
			return queryset.filter(is_active=True)
		elif self.value() == "pending":
			return queryset.filter(is_active=False)

class AccountStatusFilter(admin.SimpleListFilter):
	title = _('სტატუსის')
	parameter_name = 'is_admin'

	def lookups(self, request, model_admin):
		return (
			("user", _("მომხმარებელი")),
			("staff", _("თანამშრომელი")),
			("admin", _("ადმინისტრატორი")),
		)

	def queryset(self, request, queryset):
		if self.value() == "user":
			return queryset.filter(Q(is_admin=False)&Q(is_staff=False))
		elif self.value() == "admin":
			return queryset.filter(is_admin=True)
		elif self.value() == "staff":
			return queryset.filter(is_staff=True)


class AccountAdmin(admin.ModelAdmin):
	list_display = [ 'email',	'first_name', 'last_name' ]
	search_fields = [ 'email', 'first_name',	'last_name']
	
	list_filter = (AccountActiveFilter, AccountStatusFilter, )

	fieldsets = (
				(None, {
						"fields": ("email", "first_name", "last_name", ),
				}),
				(_("დაგენერირებული ინფორმაცია"), {
						"fields": ("token", "image", ),
				}),
				(_("დამატებითი ინფორმაცია"), {
						"fields": ("telephone", "department", 
							"company", "position", "date_of_birth", ),
				}),
		)

	readonly_fields = ('token',)
	
	class Meta:
		model = Account
'''

# admin.site.register(Account, AccountAdmin)

 

