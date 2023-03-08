from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

from apps.shared.shared_models import SharedModelHistorical, Person


class UserManager(BaseUserManager):
    """
    Custom user manager. This manager is used to create users in the system.
    """

    use_in_migrations = True

    def _create_user(self, email="email", password="password", **extra_fields) -> "User":
        """
        Default method to create and save users. Email and password are required.
        Extra fields may be provided.

        Args:
            email (str): Email address.
            password (str): Password.

        Returns:
            User: User object.

        Raises:
            ValueError: If email or password are not provided.
        """
        if not email or email =="":
            raise ValueError("User must have an email address")
        if not password or password=="":
            raise ValueError("User must have a password")

        email = self.normalize_email(email)
        user = self.model(email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email: str, password: str, **extra_fields) -> "User":
        """
        Creates and saves an user with the given email and password.
        Extra fields may be provided.

        Args:
            email (str): Email address.
            password (str): Password.

        Returns:
            User: User object.

        Raises:
            ValueError: If email or password are not provided.
        """
        extra_fields.setdefault("is_admin", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email=email, password=password, **extra_fields)

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
            ValueError: If email or password are not provided.
        """
        extra_fields.setdefault("is_admin", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_admin") is not True:
            raise ValueError("Superuser must have is_admin=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email=email, password=password, **extra_fields)


class User(AbstractBaseUser, SharedModelHistorical, Person):
    """
    Custom user model. This model is used to authenticate users in the system.
    It uses the email address as the username.
    """

    email = models.EmailField(
        "Correo electrónico",
        unique=True,
        max_length=255,
    )
    is_admin = models.BooleanField(
        "Administrador",
        default=False,
    )
    is_superuser = models.BooleanField(
        "Superusuario",
        default=False,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self) -> str:
        return "id={}, full_name={}".format(str(self.id), self.get_full_name())
