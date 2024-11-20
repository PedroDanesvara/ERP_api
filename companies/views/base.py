from typing import Any
from rest_framework.views import APIView

from companies.utils.exceptions import (
    NotFoundExployee,
    NotFoundGroup,
    NotFoundTask,
    NotFoundTaskStatus,
)
from companies.models import Employee, Enterprise, Tasks, TaskStatus

from accounts.models import Group


class Base(APIView):
    def get_enterprise_id(self, user_id) -> int:
        employee: Employee | None = Employee.objects.filter(user_id=user_id).first()
        owner: Enterprise | None = Enterprise.objects.filter(user_id=user_id).first()

        if employee:
            return employee.enterprise.id
        elif owner:
            return owner.id
        else:
            raise NotFoundExployee

    def get_employee(self, employee_id, user_id) -> Employee:
        enterprise_id: int = self.get_enterprise_id(user_id)

        employee: Employee | None = Employee.objects.filter(
            id=employee_id, enterprise_id=enterprise_id
        ).first()

        if not employee:
            raise NotFoundExployee

        return employee

    def get_group(self, group_id, enterprise_id) -> dict[str, Any]:
        group: dict[str, Any] | None = (
            Group.objects.values("name")
            .filter(id=group_id, enterprise_id=enterprise_id)
            .first()
        )

        if not group:
            raise NotFoundGroup

        return group

    def get_status(self, status_id) -> TaskStatus:
        status: TaskStatus | None = TaskStatus.objects.filter(id=status_id).first()

        if not status:
            raise NotFoundTaskStatus

        return status

    def get_task(self, task_id, enterprise_id) -> Tasks:
        task: Tasks | None = Tasks.objects.filter(
            id=task_id, enterprise_id=enterprise_id
        ).first()

        if not task:
            raise NotFoundTask

        return task
