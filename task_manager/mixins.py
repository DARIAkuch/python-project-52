from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext
from django.urls import reverse_lazy


class AuthRequired(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        self.permission_denied_message = gettext("Please log in first")
        self.redirect_field_name = reverse_lazy('login')
        return super().dispatch(request, *args, **kwargs)