from typing import Any
from django.db.models.query import ValuesQuerySet
from rest_framework import permissions

from accounts.models import User_Groups, Group_Permissions

from django.contrib.auth.models import Permission


def check_permission(user, method, permission_to: str) -> bool:
    if not user.is_authenticated:
        return False

    if user.is_owner:
        return True

    required_permission: str = "view_" + permission_to

    if method == "POST":
        required_permission = "add_" + permission_to
    elif method == "PUT":
        required_permission = "change_" + permission_to
    elif method == "DELETE":
        required_permission = "delete_" + permission_to

    groups: ValuesQuerySet[User_Groups, dict[str, Any]] = (
        User_Groups.objects.values("group_id").filter(user_id=user.id).all()
    )

    for group in groups:
        permissions: ValuesQuerySet[Group_Permissions, dict[str, Any]] = (
            Group_Permissions.objects.values("permission_id")
            .filter(group_id=group["group_id"])
            .all()
        )

        for permission in permissions:
            if Permission.objects.filter(
                id=permission["permission_id"], codename=required_permission
            ).exists():
                return True

    return False


class EmployeePermission(permissions.BasePermission):
    message = "O funcionario não tem permissão para gerenciar outros funcionários"

    def has_permission(self, request, _view) -> bool:  # type: ignore
        return check_permission(
            user=request.user, method=request.method, permission_to="employee"
        )


class GroupPermission(permissions.BasePermission):
    message = "O funcionario não tem permissão para gerenciar os grupos"

    def has_permission(self, request, _view) -> bool:  # type: ignore
        return check_permission(
            user=request.user, method=request.method, permission_to="group"
        )


class GroupsPermissionsPermission(permissions.BasePermission):
    message = "O funcionario não tem permissão para gerenciar as permissões dos grupos"

    def has_permission(self, request, _view) -> bool:  # type: ignore
        return check_permission(
            user=request.user, method=request.method, permission_to="permission"
        )


class TaskPermission(permissions.BasePermission):
    message = "O funcionario não tem permissão para gerenciar as tarefas de todos os funcionários"

    def has_permission(self, request, _view) -> bool:  # type: ignore
        return check_permission(
            user=request.user, method=request.method, permission_to="task"
        )
