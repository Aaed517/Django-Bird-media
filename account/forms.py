from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label= 'Kullanici Adi')
    password = forms.CharField(label= 'Parola', widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 50, label= 'Kullanici Adi', required='required')
    firstname = forms.CharField(label= 'Ad', required='required')
    lastname = forms.CharField(label= 'Soyad', required='required')
    mail = forms.CharField(max_length=30, label='Mail Adres')
    password = forms.CharField(max_length = 20, label= 'Parola', widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20, label= 'Parolayı Doğrula', widget= forms.PasswordInput)
    address = forms.CharField(max_length=100, label= 'Adres')
    city = forms.CharField(max_length=40, label= 'Şehir')
    country = forms.CharField(max_length=40, label= 'Ülke')
    postalcode = forms.CharField(max_length=10, label='Posta Kodu')
    about = forms.CharField(widget=forms.Textarea, label='Hakkımda')


    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        firstname = self.cleaned_data.get('firstname')
        lastname= self.cleaned_data.get('lastname')
        confirm = self.cleaned_data.get('confirm')
        address = self.cleaned_data.get('address')
        city = self.cleaned_data.get('city')
        country = self.cleaned_data.get('country')
        postalcode = self.cleaned_data.get('postalcode')
        about = self.cleaned_data.get('about')

        if password and confirm and password !=confirm:
            raise forms.ValidationError('Parolalar Eşleşmiyor')

        
        values = {
            'username' : username,
            'password' : password,
            'firstname': firstname,
            'lastname' : lastname,
            'address'  : address,
            'city' : city,
            'country' : country,
            'postalcode' : postalcode,
            'about' : about
        }
        return values
            
        
