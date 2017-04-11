# forms : something like viewmodel
# draw_member/forms.py
from django import forms

class DrawForm(forms.Form):
    GROUP_CHOICES = [
        ("資料庫", "資料庫"),
        ("YAML", "YAML"),
        ("dumpdata", "dumpdata"),
        ("ALL", "（全）"),
    ]
    group = forms.ChoiceField(
        choices=GROUP_CHOICES,
        label='團隊名稱',
        label_suffix='：',
        widget=forms.RadioSelect,
        initial='ALL'
    )
