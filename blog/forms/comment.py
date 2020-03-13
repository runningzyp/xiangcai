from django import forms

# from blog.models.comment import Comment


class CommentForm(forms.Form):
    comment = forms.Textarea()
