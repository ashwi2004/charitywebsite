from django.db import models
from django.utils import timezone

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=15, null=False)
    points = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # Can be used for tracking rewards or donations

    def __str__(self):
        return self.name

class Cause(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)
    goal_amount = models.DecimalField(max_digits=15, decimal_places=2, null=False)  # Total fundraising goal
    amount_raised = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)  # Amount raised so far
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Donation(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='donations')
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE, related_name='donations')
    amount = models.DecimalField(max_digits=15, decimal_places=2, null=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Donation of {self.amount} by {self.user.name} to {self.cause.name} on {self.date}"
