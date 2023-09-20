from django.contrib.auth.forms import AuthenticationForm
from users.models import User

class UserLoginForm(AuthenticationForm):
    class Meta:
        form = User
        fields = ('username',
                  'password',
                  )