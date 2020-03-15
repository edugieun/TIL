from django.core.management import BaseCommand
from mypost.models import Post

class Command(BaseCommand):
    help = 'Number of Posts?'

    def add_arguments(self, parser):
        parser.add_argument('num_posts', type=int)

    def handle(self, *args, **options):
        num_posts = options['num_posts']
        if num_posts > 0:
            Post.objects.bulk_create(
                [Post(title=f'Test Post{i}', content=f'This is the test post{i}') for i in range(num_posts)]
            )
        self.stdout.write(self.style.SUCCESS(f'Success'))