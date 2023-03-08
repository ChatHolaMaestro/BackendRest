from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


from apps.shared.shared_models import SharedModelHistorical, Person


class UserManager(BaseUserManager):
    """
    Custom user manager. This manager is used to create users in the system.
    """

    use_in_migrations = True

    def _create_user_without_password(self, email: str, **extra_fields) -> "User":
        """
        Default method to create and save users without password. Email is required.
        Extra fields may be provided.

        Args:
            email (str): Email address.

        Returns:
            User: User object.

        Raises:
            ValueError: If email is not provided.
        """

        if not email:
            raise ValueError("User must have an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_unusable_password()
        user.save(using=self._db)
        return user

    def _create_user_with_password(
        self, email: str, password: str, **extra_fields
    ) -> "User":
        """
        Default method to create and save users. Email and password are required.
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

    def create_user_without_password(self, email: str, **extra_fields) -> "User":
        """
        Creates and saves an user without password. Email is required.
        Extra fields may be provided.

        Args:
            email (str): Email address.

        Returns:
            User: User object.

        Raises:
            ValueError: If email is not provided.
        """

        return self._create_user_without_password(email, **extra_fields)

    def create_user_with_password(
        self, email: str, password: str, **extra_fields
    ) -> "User":
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

        return self._create_user_with_password(email, password, **extra_fields)

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

        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user_with_password(email, password, **extra_fields)


class User(AbstractBaseUser, SharedModelHistorical, Person):
    """
    Custom user model. This model is used to authenticate users in the system.
    It uses the email address as the username.
    """

    ADMIN = 1
    TEACHER = 2
    SCHOOL_MANAGER = 3
    CHATBOT = 4

    email = models.EmailField(
        "Correo electrónico",
        unique=True,
        max_length=255,
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
