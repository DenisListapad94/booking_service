from .models import PersonQueue
# TDD

class Queue():
    FIFO = "FIFO"
    LIFO = "LIFO"
    STRATEGIES = [FIFO, LIFO]

    def __init__(self, strategy):
        if strategy not in self.STRATEGIES:
            raise TypeError
        self.strategy = strategy

    def add(self, value):
        if self.strategy == self.FIFO:
            PersonQueue.objects.create(value=value)

    def pop(self):
        if self.strategy == self.FIFO:
            value = PersonQueue.objects.order_by("id").first()
            if value:
                value = value.value
                PersonQueue.objects.order_by("id").first().delete()
                return value

            return None
