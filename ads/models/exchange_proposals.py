from django.db import models
from .ads import Ad


class StatusChoices(models.TextChoices):
    PENDING = 'pending', 'Ожидает'
    ACCEPTED = 'accepted', 'Принята'
    REJECTED = 'rejected', 'Отклонена'


class ExchangeProposal(models.Model):
    ad_sender = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='sent_proposals')
    ad_receiver = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='received_proposals')
    comment = models.TextField()
    status = models.CharField(max_length=10, choices=StatusChoices, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['ad_sender', 'ad_receiver'], name='unique_exchange_between_ads')
        ]

    def __str__(self):
        return f"{self.ad_sender} → {self.ad_receiver} [{self.status}]"
