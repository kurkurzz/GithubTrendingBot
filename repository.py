
class Repository:
    author = ''
    name = ''
    languageColor = ''
    url = ''
    description = ''
    language = ''
    stars = ''
    currentPeriodStars = ''
    forks = ''
    avatar = ''
    builtBy = []

    def __init__(self,dict):
        self.author = dict['author']
        self.name = dict['name']
        self.languageColor = dict['languageColor']
        self.url = dict['url']
        self.description = dict['description']
        self.language = dict['language']
        self.stars = dict['stars']
        self.currentPeriodStars = dict['currentPeriodStars']
        self.forks = dict['forks']
        self.avatar = dict['avatar']
        self.builtBy = dict['builtBy']

    def __str__(self):
        return f'author: {self.author}\n'\
            f'name: {self.name}\n' \
            f'languageColor: {self.languageColor}' \
            f'url: {self.url}\n' \
            f'description: {self.description}\n' \
            f'language: {self.language}\n' \
            f'stars: {self.stars}\n' \
            f'currentPeriodStars: {self.currentPeriodStars}\n' \
            f'forks: {self.forks}\n' \
            f'avatar: {self.avatar}\n' \
            f'builtBy: {self.builtBy}'