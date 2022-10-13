from socket import fromshare
from django import forms
from .models import Chat

class ChatForm(forms.ModelForm):

    class Meta:
        model = Chat
        fields = '__all__'