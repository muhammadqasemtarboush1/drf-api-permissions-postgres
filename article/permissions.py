from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'You are unauthorized. or you don\'t have permissions to inter to this rout'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user