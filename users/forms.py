from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from jobportal.models import Jobs, JobApplication
from rents.models import Item4Rent
from blog.models import Comment


class UserRegistrationForm(UserCreationForm):
    Category = [
        ('MP', 'Marketplace'),
        ('JP', 'Job Portal'),
        ('AU', 'Auction'),
        ('RT', 'Rental')
    ]   
    email = forms.EmailField(required=True)
    category = forms.ChoiceField(choices = Category)



    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class Jobs(forms.ModelForm):
    model = Jobs
    fields = ['job_title', 'date_end', 'organization', 'location', 'salary', 'job_description']


class JobApplicationForm(forms.Form):
    model = JobApplication
    fields = ['applicant', 'cover_letter', 'cv', 'date_applied']


class RentsForm(forms.ModelForm):
    model = Item4Rent
    fields = ['item_name', 'image', 'description', 'location']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']