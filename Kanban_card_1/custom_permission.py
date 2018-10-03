from rest_framework import permissions

class IsCurrentUserOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class IsCurrentUserAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print('hello')
        print(obj)
        print(request)
        return obj.account.owner == request.user