from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
	message = 'You must be owner of this object.'
	my_safe_method = ['GET', 'PUT']

	def has_object_permission(self, request, view, obj):
		if not request.method in self.my_safe_method:
			return False
		return obj.user == request.user