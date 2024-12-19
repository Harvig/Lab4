import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import Putovanje, Prijave
from main.factory import (
    PutovanjeFactory,
    PrijaveFactory
)

NUM_PUTOVANJE = 10
NUM_PRIJAVE = 100

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Putovanje, Prijave]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_PUTOVANJE):
            putovanje = PutovanjeFactory()

        for _ in range(NUM_PRIJAVE):
            prijava = PrijaveFactory()