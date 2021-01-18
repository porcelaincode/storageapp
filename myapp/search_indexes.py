import datetime 
from haystack import indexes

from .models import Data

class DataIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    content_auto = indexes.EdgeNgramField(model_attr="file")

    def get_model(self):
        return Data

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
        