from django.db import models


# Create your models here.


class Prime(models.Model):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numbers = int

    @property
    def primes(self):
        tab = []
        for i in range(2, self.numbers):

            for j in (tab):
                if i % j == 0: break
            else:
                yield i
                tab.append(i)
        return tab
