from rest_framework import permissions
from homepage.models import Profile, Team


class IsProductManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return Profile.objects.get(user=request.user).role == Profile.PRODUCT


class IsReviewer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return Profile.objects.get(user=request.user).role == Profile.REVIEWER


class IsTeamMember(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return Team.objects.get(profile=Profile.objects.get(user=request.user)) == obj

