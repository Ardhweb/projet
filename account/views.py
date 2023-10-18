from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
from .forms import UserSignupForm,LoginForm,CustomPwdChgForm,PasswordResetForm,PasswordResetConfirmForm
from django.contrib.auth import authenticate, login, logout
from .models import User

from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth import update_session_auth_hash


def register_user(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid ():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request,'accounts/account/register_done.html',{'new_user': new_user})
    else:
        form = UserSignupForm()
    return render(request,'accounts/account/register.html',{'form': form})




    #LoginView
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                        email=cd['email'],
                                        password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    #return HttpResponse('Authenticated 'successfully')
                    return redirect('home')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    
        
    else:
        form = LoginForm()
    return render(request, 'accounts/account/login.html', {'form': form})



    #LogoutView



def logout_view(request):
    logout(request)
    return redirect("home")






def changepwview(request):
    if request.method == 'POST':
        form = CustomPwdChgForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('home')
    else:
        form = CustomPwdChgForm(user=request.user)
    return render(request, 'accounts/registration/chgpwd.html', {'form': form})







#send mail testing
def test_send_mail(request):
    send_mail(
    subject = 'That’s your subject',
    message = 'That’s your message body',
    from_email = settings.EMAIL_HOST_USER ,
    recipient_list = ['hiwhystudio.dev@gmail.com',],
    # auth_user = 'Login'
    # auth_password = 'Password'
    fail_silently = False,)
    return HttpResponse("Send Compeleted")



from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from django.forms import ValidationError
from django import forms



class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'accounts/registration/password_reset_form.html'
    email_template_name = 'accounts/registration/password_reset_email.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('account:password_reset_done')

    def form_valid(self, form):
        # Get the email entered in the form
        form_email = form.cleaned_data.get('email')
        # Get the email of the currently logged-in user
        # user_email = self.request.user.email #pr
        if self.request.user.is_authenticated:
            user_email = self.request.user.email  #Getting Current Loggend inuser email
            # Check if they are the same
            if form_email != user_email:
               # If not, raise a ValidationError and stop further processes
               raise forms.ValidationError("The entered email does not match with the logged-in user's email.")
               #messages.success(self.request, 'Password reset has been sent to your email.')
        else:
            #Check if the entered email exists in the user model table
            if not User.objects.filter(email=form_email).exists():
                raise forms.ValidationError("The entered email does not exist.")
        return super().form_valid(form)
   

 
    

class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accounts/registration/password_reset_done.html'

class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/registration/password_reset_confirm.html'
    form_class = PasswordResetConfirmForm
    success_url = reverse_lazy('account:password_reset_complete')

class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/registration/password_reset_complete.html'
