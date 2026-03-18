from django.core.management.base import BaseCommand
from faker import Faker
from apps.core.models import Product, Order, OrderItem
from apps.account.models import User

fake = Faker()

class Command(BaseCommand):
    help = 'Generate dummy data for Product and Order models'

    def handle(self, *args, **kwargs):
        # Create dummy users
        users = []
        for _ in range(5):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password='password123',
                phone_number=fake.numerify(text='01#########'),
                gender=fake.random_element(elements=('male', 'female'))
            )
            users.append(user)

        self.stdout.write(self.style.SUCCESS('Successfully created dummy users.'))

        # Create dummy products
        products = []
        for _ in range(10):
            product = Product.objects.create(
                name=fake.word().capitalize(),
                description=fake.text(),
                price=fake.random_number(digits=5) / 100,
                stock=fake.random_int(min=1, max=100),
                image='products/dummy_image.jpg'  # Assuming you have a dummy image in this path
            )
            products.append(product)

        self.stdout.write(self.style.SUCCESS('Successfully created dummy products.'))

        # Create dummy orders
        for _ in range(5):
            order = Order.objects.create(
                user=fake.random_element(elements=users),
                status=fake.random_element(elements=Order.OrderStatus.values)
            )
            # Add products to the order with random quantities
            for _ in range(fake.random_int(min=1, max=5)):
                product = fake.random_element(elements=products)
                quantity = fake.random_int(min=1, max=10)
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity
                )

        self.stdout.write(self.style.SUCCESS('Successfully created dummy orders with order items.'))