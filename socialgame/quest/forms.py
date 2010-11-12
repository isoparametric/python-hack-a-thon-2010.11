# -*- coding: utf-8 -*-
from django import forms

from models import QuestProgress

class QuestProgressForm(forms.ModelForm):
    '''
    クエストの進行フォーム
    '''
    class Meta:
        model = QuestProgress


