from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, resolve_url
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import (
     get_user_model, logout as auth_logout,
)
from .forms import UserCreateForm, UserUpdateForm



User = get_user_model()

class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk'] or user.is_superuser

class SignUpView(generic.CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ProfileView(LoginRequiredMixin, generic.View):

    def get(self, *args, **kwargs):
        return render(self.request,'registration/profile.html')

class UserUpdateView(OnlyYouMixin, generic.UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'registration/user_form.html'

    def get_success_url(self):
        return resolve_url('../../profile', pk=self.kwargs['pk'])

class UserDeleteView(OnlyYouMixin, generic.DeleteView):
    template_name = "registration/delete.html"
    success_url = reverse_lazy('accounts:signup')
    model = User
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
