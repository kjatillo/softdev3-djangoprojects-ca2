from django.contrib.auth.models import Group
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = CustomUser.objects.get(username=username)
            customer_group = Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)
            
            return redirect('login')
        else:
            return render(
                request,
                self.template_name,
                {'form': form}
            )
