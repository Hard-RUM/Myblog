from haystack import indexes
from .models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    # 获取模型
    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        # 把所有的post对象返回
        return self.get_model().objects.all()
