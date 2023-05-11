from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.urls import reverse

from django_rest_passwordreset.signals import reset_password_token_created


email_html_message = """
    <html>
        <body>
            <p>
                Hola {current_user},
            </p>
            <p>
                Recibimos una solicitud para cambiar la contraseña de tu cuenta en #ChatHolaMaestro.
            </p>
            <p>
                Si hiciste esta solicitud, haz clic en el siguiente enlace para cambiar tu contraseña:
            </p>
            <p>
                <a href="{reset_password_url}">Cambiar contraseña</a>
            </p>
            <p>
                Si no hiciste esta solicitud, puedes ignorar este correo electrónico.
            </p>
        </body>
    </html>
"""

email_plaintext_message = """
    Hola {current_user},
    Recibimos una solicitud para cambiar la contraseña de tu cuenta en #ChatHolaMaestro.
    Si hiciste esta solicitud, haz clic en el siguiente enlace para cambiar tu contraseña:
    {reset_password_url}
    Si no hiciste esta solicitud, puedes ignorar este correo electrónico.
"""


@receiver(reset_password_token_created)
def password_reset_token_created(
    sender, instance, reset_password_token, *args, **kwargs
):
    """Handles password reset tokens.
    When a token is created, an e-mail needs to be sent to the user

    Args:
        sender: view class that sent the signal
        instance: view instance that sent the signal
        reset_password_token: Token Model Object
    """
    # send an e-mail to the user
    context = {
        "current_user": reset_password_token.user.get_full_name(),
        "reset_password_url": "{}?token={}".format(
            instance.request.build_absolute_uri(
                reverse("password_reset:reset-password-confirm")
            ),
            reset_password_token.key,
        ),
    }

    # render email text
    msg = EmailMultiAlternatives(
        # title:
        "Cambio de contraseña #ChatHolaMaestro",
        # message:
        email_plaintext_message.format(**context),
        # from:
        "noreply@chatholamaestro.com",
        # to:
        [reset_password_token.user.email],
    )
    msg.attach_alternative(email_html_message.format(**context), "text/html")
    msg.send()
