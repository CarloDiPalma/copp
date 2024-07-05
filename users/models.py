from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """Create and save a user with the given email, and
        password."""
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    # def create_user(self, email, first_name, last_name, password=None, is_admin=False, is_staff=False,
    #                 is_active=True):
    #     if not email:
    #         raise ValueError("User must have an email")
    #     if not password:
    #         raise ValueError("User must have a password")
    #     if not first_name:
    #         raise ValueError("User must have a first_name")
    #     if not last_name:
    #         raise ValueError("User must have a last_name")
    #
    #     user = self.model(
    #         email=self.normalize_email(email)
    #     )
    #     user.first_name = first_name
    #     user.last_name = last_name
    #     user.set_password(password)  # change password to hash
    #     user.admin = is_admin
    #     user.staff = is_staff
    #     user.active = is_active
    #     user.save(using=self._db)
    #     return user

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not first_name:
            raise ValueError("User must have a first_name")
        if not first_name:
            raise ValueError("User must have a last_name")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.admin = True
        user.staff = True
        user.active = True
        user.save(using=self._db)
        return user

    # def create_superuser(self, email, password, **extra_fields):
    #     extra_fields.setdefault('is_staff', True)
    #     extra_fields.setdefault('is_superuser', True)
    #     extra_fields.setdefault('is_admin', True)
    #
    #     if extra_fields.get('is_staff') is not True:
    #         raise ValueError(
    #             'Superuser must have is_staff=True.'
    #         )
    #     if extra_fields.get('is_superuser') is not True:
    #         raise ValueError(
    #             'Superuser must have is_superuser=True.'
    #         )
    #
    #     return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Кастомный юзер."""

    USER_ROLE = 'user'
    ORGANIZATION_ROLE = 'organization'
    ADMIN_ROLE = 'admin'
    TEACHER_ROLE = 'teacher'
    STUDENT_ROLE = 'student'

    ROLE_CHOICES = (
        (USER_ROLE, 'Пользователь'),
        (ORGANIZATION_ROLE, 'Организация'),
        (ADMIN_ROLE, 'Администратор'),
        (TEACHER_ROLE, 'Преподаватель'),
        (STUDENT_ROLE, 'Обучающийся')
    )

    username = None
    email = models.EmailField(unique=True, max_length=254)
    first_name = models.CharField(max_length=150, blank=True, null=False)
    last_name = models.CharField(max_length=150, blank=True, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # is_admin = models.BooleanField(default=False)
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=USER_ROLE,
        blank=True
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ["-id"]

    @property
    def is_admin(self):
        return self.role == User.ADMIN_ROLE

    @property
    def is_organization(self):
        return self.role == User.ORGANIZATION_ROLE

    @property
    def is_user(self):
        return self.role == User.USER_ROLE

    @property
    def is_teacher(self):
        return self.role == User.TEACHER_ROLE

    @property
    def is_student(self):
        return self.role == User.STUDENT_ROLE
