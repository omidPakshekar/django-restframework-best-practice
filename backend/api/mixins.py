from rest_framework import permissions
from .permissions import IsStaffEditorPermission

class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]


class UserQuerySetMixin():
    user_field = 'user'
    def get_queryset(self, *args, **kwargs):
        user_ = self.request.user
        lookup_data = {}
        lookup_data[self.user_field] = user_
        qs = super().get_queryset(*args, **kwargs)
        if user_.is_superuser:
            return qs
        return qs.filter(**lookup_data)
