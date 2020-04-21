from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout,
)

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
            username = self.cleaned_data.get("username")
            password = self.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            user_qs = User.objects.filter(username=username)

            if user_qs.count()==1:
                user = user_qs.first()
            if not user:
                raise forms.ValidationError("This user does not exist!!")
            if not user.check_password(password):
                raise forms.ValidationError("Password is incorrect !!")
            if not user.is_active:
                raise forms.ValidationError("This User is not longer active")
            return super(UserLoginForm,self).clean(*args,**kwargs)

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = (
            'first_name',
            'username',
            'email',
            'password',
            'password2',
        )
    def clean(self):
        first_name = self.cleaned_data['first_name']
        print(first_name)
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password!=password2:
            raise forms.ValidationError("Password does't match")
        #check whether username is present in the database or not
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already exists")

        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Email is already exists")
        return super(UserRegisterForm,self).clean()
