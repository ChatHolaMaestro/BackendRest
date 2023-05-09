from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

from apps.shared.models import SharedModelHistorical, Person


class UserManager(BaseUserManager):
    """
    Custom user manager. This manager is used to create users in the system.
    """

    use_in_migrations = True

    def create_user_without_password(self, email: str, **extra_fields) -> "User":
        """
        Creates and saves a user with an unusable password. Email is required.
        Extra fields may be provided.

        Args:
            email (str): Email address.

        Returns:
            User: User object.

        Raises:
            ValueError: If email is not provided.
        """

        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_staff", False)
        if extra_fields.get("is_superuser"):
            raise ValueError("Non-password user must have is_superuser=False.")
        if extra_fields.get("is_staff"):
            raise ValueError("Non-password user must have is_staff=False.")

        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_user_with_password(
        self, email: str, password: str, **extra_fields
    ) -> "User":
        """
        Creates and saves a user. Email and password fields are required.
        Extra fields may be provided.

        Args:
            email (str): Email address.
            password (str): Password.

        Returns:
            User: User object.

        Raises:
            ValueError: If email or password aren't provided.
        """

        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have a password")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email: str, password: str, **extra_fields) -> "User":
        """
        Creates and saves a superuser with the given email and password.
        Extra fields may be provided.

        Args:
            email (str): Email address.
            password (str): Password.

        Returns:
            User: User object.

        Raises:
            ValueError:
            - If is_superuser is not True.
            - If is_staff is not True.
            - If role is not User.ADMIN.
        """

        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("role", User.ADMIN)
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser must have is_superuser=True.")
        if not extra_fields.get("is_staff"):
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("role") != User.ADMIN:
            raise ValueError("Superuser must have role={}".format(User.ADMIN))

        return self.create_user_with_password(email, password, **extra_fields)


class User(AbstractBaseUser, SharedModelHistorical, Person):
    """
    Custom user model. This model is used to authenticate users in the system.
    It uses the email address as the username.
    """

    ADMIN = 1
    TEACHER = 2
    SCHOOL_MANAGER = 3
    ROLE_CHOICES = (
        (ADMIN, "Administrador"),
        (TEACHER, "Profesor"),
        (SCHOOL_MANAGER, "Director de escuela"),
    )

    email = models.EmailField(
        "Correo electrónico",
        unique=True,
        max_length=255,
    )
    is_superuser = models.BooleanField(
        "Superusuario",
        default=False,
        help_text="Designates that this user has all permissions without explicitly assigning them.",
    )
    is_staff = models.BooleanField(
        "Staff",
        default=False,
        help_text="Designates whether the user can log into the admin site.",
    )
    role = models.PositiveSmallIntegerField(
        "Rol",
        choices=ROLE_CHOICES,
        default=ADMIN,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self) -> str:
        return "{{id: {}, full_name: {}, role: {}}}".format(
            str(self.id), self.get_full_name(), self.get_role_display()
        )
