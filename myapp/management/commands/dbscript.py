from django.core.management.base import BaseCommand
from myapp.models import Article
import random

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for i in range(1, 51):
            Article.objects.create(
                title=f"Article {i}",
                content=f"This is the content of article {i}",
                author=f"user{i}",
                is_published=random.choice([True, False])
            )
        self.stdout.write("Successfully created 50 articles.")