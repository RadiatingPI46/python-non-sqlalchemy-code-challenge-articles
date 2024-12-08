class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters")
        self.author = author
        self.magazine = magazine
        self.title = title

    def show(self):
        return self.title
       
class Author:
    def __init__(self, name):
        self.name = name
        self.articles=[]

    def articles(self):
        return self.articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article =Article(self,magazine,title)
        self.articles.append(article)

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))
    

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise ValueError("Magazine name must be between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self.name = name
        self.category = category
        self.author_instance = Author(self)

    def articles(self):
        return self.author_instance.articles

    def contributors(self):
        self.author_instance.name

    def article_titles(self):
        self.article_titles

    def contributing_authors(self):
        pass

author = Author("John")

magazine_1 = Magazine("Vogue", "Fashion")
magazine_2 = Magazine("AD", "Architecture & Design")
magazine_3 = Magazine("GQ", "Fashion")

article_1 = Article(author, magazine_1, "How to wear a tutu with style") 


print(magazine_1)