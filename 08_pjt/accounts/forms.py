from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from movies.models import Genre

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Genre의 정보들을 이용하여 'choices'를 생성합니다.
        self.fields['favorite_genre'].choices = [(genre.id, genre.name) for genre in Genre.objects.all()]

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('favorite_genre',)


class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Genre의 정보들을 이용하여 'choices'를 생성합니다.
        self.fields['favorite_genre'].choices = [(genre.id, genre.name) for genre in Genre.objects.all()]

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ("first_name", "last_name", "email", "favorite_genre")