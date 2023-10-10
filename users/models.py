from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from django.utils.timezone import now

import store.settings


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    is_verified_user = models.BooleanField(default=False)
    is_verified_email = models.BooleanField(default=False)


class EmailVerification(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    code = models.UUIDField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def str(self):
        return f'EmailVerification object for {self.user.email}'

    def send_verification_email(self):
        link = reverse('users:email_verification', kwargs={'email':self.user.email, 'code':self.code})
        verification_link = f'{settings.DOMAIN_NAME}{link}'
        subject = f'Подтверждение почты для {self.user.username}'
        message = 'Для подтверждения учетной записи {} перейдите по ссылке: {}'.format(
            self.user.email,
            verification_link
        )
        send_mail(
            subject=subject,
            message=message,
            from_email=store.settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
            )

    def is_expired(self):
        return now() > self.expiration

