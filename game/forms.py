from django import forms
from models import UserProfile, Level


class AvatarUploadForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar']


class AvatarPreUploadedForm(forms.Form):
    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('my_choices')
        super(AvatarPreUploadedForm, self).__init__(*args, **kwargs)
        self.fields['avatars'] = forms.ChoiceField(choices=choices)

    class Meta:
        model = UserProfile
        fields = ('avatar',)


class ShareLevelPerson(forms.Form):
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    level = forms.IntegerField()


class ShareLevelClass(forms.Form):
    def __init__(self, *args, **kwargs):
        classes = kwargs.pop('classes')
        super(ShareLevelClass, self).__init__(*args, **kwargs)
        self.fields['classes'] = forms.ModelChoiceField(queryset=classes)
        self.fields['levels'] = forms.IntegerField()


class ScoreboardForm(forms.Form):
    def __init__(self, *args, **kwargs):
        classes = kwargs.pop('classes')
        super(ScoreboardForm, self).__init__(*args, **kwargs)
        self.fields['classes'] = forms.ModelChoiceField(queryset=classes,
                                                        required=False)
        self.fields['levels'] = forms.ModelChoiceField(queryset=Level.objects.filter(default=1),
                                                       required=False)

        def validate(self):
            cleaned_data = super(ScoreboardForm, self).clean()
            classes = cleaned_data.get('classes')
            levels = cleaned_data.get('levels')
            return classes or levels
