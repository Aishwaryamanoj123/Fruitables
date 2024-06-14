from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
import datetime

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    def __str__(self):
        return self.name



class categories(models.Model): 
    name = models.CharField(max_length=100)   
    def __str__(self):
        return self.name 
    

class sub_category(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(categories,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    


    
class prdct(models.Model):
    category = models.ForeignKey(categories,on_delete=models.CASCADE)
    Sub_category = models.ForeignKey(sub_category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/img')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    # description = models.TextField(default=1)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
# class our_organic_products(models.Model):
#     name = models.CharField(max_length=100)
    

    def __str__(self):
       return self.name

class UsercreateForm(UserCreationForm):
    email = forms.EmailField(required=True,label='Email',error_messages={'Exist':'This Already Exists'})



class UsercreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UsercreateForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'




        def save(self,commi=True):
            user = super(UsercreateForm,self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commi:
                user.save()
                return user
            
        def clean_email(self):
            if User.objects.filter(email=self.cleaned_data['email']).exists():
                raise forms.ValidationError(self.fields['email'].error_message['Exists'])
            return self.cleaned_data['email']
        
            
class Order(models.Model):
    image = models.ImageField(upload_to='static/img')
    product = models.CharField(max_length=1000)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.CharField(max_length=5)
    total = models.CharField(max_length=1000, default='')
    address = models.TextField()
    phone = models.CharField(max_length=10)
    pincode = models.CharField(max_length=10)
    date = models.DateField(default=datetime.datetime.today)

    
    def __str__(self):
       return self.product




    
   