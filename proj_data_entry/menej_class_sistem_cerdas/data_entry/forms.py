from django import forms
from .models import Pengguna,Content

STATES = (
    ('', 'Choose...'),
    ('DKI','Daerah Khusus Ibu Kota'),
    ('DIY','Daerah Istimewa Yogyakarta'),
    ('JaBar','Jawa Barat')
)
STATUS = (
    ('', 'Choose...'),
    ('S','Selesai'),
    ('B','Berlangsung'),
    ('G','Gagal')
)

class SearchPengguna(forms.Form):
    state = forms.ChoiceField(choices=STATES)

class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)

class PenggunaForm(forms.ModelForm):
    state = forms.ChoiceField(choices=STATES)

    class Meta:
        model = Pengguna
        exclude = ['tanggal_join',]

class ContentForm(forms.ModelForm):

    class Meta:
        model = Content
        exclude = ['date_created']
