from django.core.management.base import BaseCommand
from inventory.models import Item

class Command(BaseCommand):
    help = 'Populate the database with demo data.'

    def handle(self, *args, **kwargs):
        # Check if items already exist to avoid duplicates
        if Item.objects.exists():
            self.stdout.write(self.style.WARNING('Items already exist in the database. No new data added.'))
            return

        items = [
            {"name": "Laptop", "description": "Gaming laptop", "item_id": "LP123", "price": 1500, "quantity": 10},
            {"name": "Smartphone", "description": "Flagship phone", "item_id": "SP123", "price": 900, "quantity": 50},
            {"name": "Headphones", "description": "Noise-cancelling", "item_id": "HP123", "price": 150, "quantity": 100},
        ]

        for item in items:
            Item.objects.create(
                name=item['name'], description=item['description'], item_id=item['item_id'],
                price=item['price'],quantity=item['quantity']
            )

        self.stdout.write(self.style.SUCCESS('Demo data successfully populated.'))