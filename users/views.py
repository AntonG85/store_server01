from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib import auth, messages
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users.models import User
from products.models import Basket
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm




class UserRegistrationView(CreateView):
    model = User
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super(UserRegistrationView, self).get_context_data()
        context.update({
        'title': 'Store - Регистрация'
        })
        return context


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context.update({
            'title': 'Store - Страница пользователя',
            'baskets': Basket.objects.filter(user=self.object)
        })
        return context

# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#     else:
#         form = UserLoginForm()
#     context = {'form': form}
#     return render(request, 'users/login.html', context)
#
# def logout(request):
#     user = auth.logout(request)
#     return HttpResponseRedirect(reverse('index'))

# def registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.info(request, 'Регистрация прошла успешно!')
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegistrationForm()
#     context = {'form': form}
#     return render(request, 'users/registration.html', context)

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:profile'))
#     else:
#         form = UserProfileForm(instance=request.user)
#     context = {'title': 'Профиль',
#                'form': form,
#                'baskets': Basket.objects.filter(user=request.user),
#     }
#     return render(request, 'users/profile.html', context)
