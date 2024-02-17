from django_filters import FilterSet, ModelMultipleChoiceFilter
from .models import Post, Category, PostCategory


class PostFilter(FilterSet):
    category = ModelMultipleChoiceFilter(
        field_name ='postСategory',
        queryset = Category.objects.all(),
        label = 'postcategory',
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'dateCreation': ['exact'],
        }
