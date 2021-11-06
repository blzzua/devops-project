from app import flask_app
from models import db
from models import Article

from loremipsum import get_sentences
import random

# pocet článku
COUNT = 47

def create_article(num):
    title = "Article {:02d}".format(num)

    content = " ".join(get_sentences(random.randint(3,9), True))
    article = Article(title=title, content=content)
    return article

with flask_app.app_context():

    for num in range(1, COUNT+1):
        article = create_article(num)
        db.session.add(article)
        db.session.commit()
        print("article #{:02d} created!".format(num))