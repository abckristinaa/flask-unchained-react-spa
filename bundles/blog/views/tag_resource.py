from flask_unchained.bundles.api import ModelResource
from flask_unchained import injectable

from ..models import Tag
from ..services import ArticleManager, SeriesManager


class TagResource(ModelResource):
    class Meta:
        model = Tag
        include_methods = ('get', 'list')

    def __init__(self,
                 article_manager: ArticleManager = injectable,
                 series_manager: SeriesManager = injectable):
        super().__init__()
        self.article_manager = article_manager
        self.series_manager = series_manager

    def get(self, tag):
        return self.Meta.serializer.dump({
            'name': tag.name,
            'slug': tag.slug,
            'series': self.series_manager.find_by_tag(tag),
            'articles': self.article_manager.find_by_tag(tag),
        })
