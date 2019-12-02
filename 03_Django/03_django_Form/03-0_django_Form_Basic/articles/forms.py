from django import forms
from .models import Article

## 일반 form
# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=10,
#         label='제목',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'my-title',
#                 'placeholder': 'Enter the title',
#             }
#         )
#     )
#     # form은 charfield의 max_length를 적지않으면 textfield와 같다
#     content = forms.CharField(
#         label='내용',
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'my-content',
#                 'placeholder': 'Enter the content',
#                 'rows': 5,
#                 'cols': 50,
#             }
#         )
#     )


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title'
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        )
    )

    class Meta:
        model = Article
        # fields = ('title', 'content',)
        # 모두 포함 __all__
        fields = '__all__'

        # 제외하는 법 : exclude
        # exclude = ('title',)

        # widgets = {
        #     'title': forms.TextInput(attrs={
        #         'class': 'mytitle'})
        # }

        