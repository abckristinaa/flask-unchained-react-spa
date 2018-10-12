from flask_unchained.bundles.api import ModelResource
from flask_unchained import injectable

from ..models import Article
from ..services import ArticleManager


class ArticleResource(ModelResource):
    class Meta:
        model = Article
        include_methods = ('get', 'list')
        include_decorators = ('get',)
        member_param = '<string:slug>'

    def __init__(self, article_manager: ArticleManager = injectable):
        super().__init__()
        self.article_manager = article_manager

    def get(self, article):
        prev, next = self.article_manager.get_prev_next(article)
        return {'article': article, 'prev': prev, 'next': next}

    def list(self):
        return self.article_manager.find_published()
