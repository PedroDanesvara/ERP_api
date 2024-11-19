from django.db.models.manager import BaseManager
from rest_framework.views import APIView
from rest_framework.exceptions import APIException

from accounts.models import Group, User_Groups, Group_Permissions
from companies.models import Employee, Enterprise

class Base(APIView):
    def get_enterprise_user(self, user_id):
        enterprise = {
            "is_owner": False,
            "permissions": []
        }

        enterprise['is_owner'] = Enterprise.objects.filter(user_id=user_id).exists()
        if enterprise['is_owner']: 
            return enterprise
        
        employee: Employee | None = Employee.objects.filter(user_id=user_id).first()
        if employee is None: 
            raise APIException('Este usuário não é um funcionário')
        
        groups: BaseManager[User_Groups] = User_Groups.objects.filter(user_id=user_id).all()
        
        for g in groups:
            group: Group = g.group
            permissions: BaseManager[Group_Permissions] = Group_Permissions.objects.filter(group_id=group.id).all()
            
            for p in permissions:
                enterprise['permissions'].append({ 
                    "id": p.permission.id, # type: ignore
                    "label": p.permission.name,
                    "codename": p.permission.codename,
                })
        
        return enterprise
    