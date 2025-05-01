from django.core.management.base import BaseCommand
from faker import Faker
from root.models import Ability, Agents
from faker.providers import job
from services.models import Category, Services
from accounts.models import User
import random



class Command(BaseCommand):
    def __init__(self):
        super().__init__(self)
        self.fake = Faker("fa_IR")
        self.job = ["A1", "A2", "A3"]
        self.list_category = ["c1", "c2", "c3"]


    help = "tis is first custome command"

    def handle(self, *args, **options):
        for item in self.job:
            Ability.objects.get_or_create(name=item)

        for item in self.list_category:
            Category.objects.get_or_create(title=item)
        
        for _ in range (10):
            User.objects.create_user(email=self.fake.email(), password=self.fake.password())

        list_users = User.objects.all()
        List_ability = Ability.objects.all()

        for _ in range (10):
            user = random.choice(list_users)
            ability = random.choice(List_ability)
            Agents.objects.create(user=user, ability=ability)

        list_agents = Agents.objects.all()
        list_category = Category.objects.all()
        for _ in range (10):
            agent = random.choice(list_agents)
            category = random.choices(list_category)
            service = Services.objects.create(title=self.fake.name(),
                                    creator=agent, 
                                    status=True
                                    )
            service.category.set(category)

        print ("data created successfully...")