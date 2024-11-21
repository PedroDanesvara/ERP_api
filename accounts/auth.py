from rest_framework.exceptions import AuthenticationFailed, APIException

from django.contrib.auth.hashers import check_password, make_password

from accounts.models import User
from companies.models import Enterprise, Employee


class Authentication:
    def signin(self, email=None, password=None) -> User:
        exception_auth = AuthenticationFailed("Email e/ou senha incorreto(s)")
        user: User | None = User.objects.filter(email=email).first()

        if user is None:
            raise exception_auth

        if not check_password(password, user.password):
            raise exception_auth

        return user

    def signup(
        self, name, email, password, account_type="owner", company_id=False
    ) -> User:
        if not name or name == "":
            raise APIException("O nome não deve ser null")

        if not email or email == "":
            raise APIException("O email não deve ser null")

        if not password or password == "":
            raise APIException("O password não deve ser null")

        if account_type == "employee" and not company_id:
            raise APIException("O id da empresa não deve ser null")

        user = User
        if user.objects.filter(email=email).exists():
            raise APIException("Este email já existe na plataforma")

        password_hashed: str = make_password(password)

        created_user: User = user.objects.create(
            name=name,
            email=email,
            password=password_hashed,
            is_owner=False if account_type == "employee" else True,
        )

        if account_type == "owner":
            created_enterprise: Enterprise = Enterprise.objects.create(
                name=created_user.name,
                user_id=created_user.id,
            )

        if account_type == "employee":
            Employee.objects.create(
                user_id=created_user.id,
                enterprise_id=company_id or created_enterprise.id,  # type: ignore
            )

        return created_user
