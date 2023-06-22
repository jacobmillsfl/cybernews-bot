from .json_serializable import JSONSerializable

class Source(JSONSerializable):
    def __init__(self, data):
        self.id = data.get('id')
        self.name = data.get('name')


class Article(JSONSerializable):
    def __init__(self, data):
        self.source = Source(data.get('source'))
        self.author = data.get('author')
        self.title = data.get('title')
        self.description = data.get('description')
        self.url = data.get('url')
        self.url_to_image = data.get('urlToImage')
        self.published_at = data.get('publishedAt')
        self.content = data.get('content')


class NewsData(JSONSerializable):
    def __init__(self, data):
        self.status = data.get('status')
        self.total_results = data.get('totalResults')
        self.articles = [Article(article) for article in data.get('articles')]
