from rest_framework import serializers
from ads.models.ads import Ad
from ads.models.exchange_proposals import ExchangeProposal


class AdSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Ad
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at']


class ExchangeProposalSerializer(serializers.ModelSerializer):
    sender_user = serializers.CharField(source='ad_sender.user.username', read_only=True)
    receiver_user = serializers.CharField(source='ad_receiver.user.username', read_only=True)

    class Meta:
        model = ExchangeProposal
        fields = [
            'id',
            'comment',
            'status',
            'ad_sender',
            'ad_receiver',
            'created_at',
            'sender_user',
            'receiver_user',
        ]

    def validate_status(self, value):
        if self.instance is None and value != "pending":
            raise serializers.ValidationError("Статус при создании должен быть 'pending'.")
        return value


class ExchangeProposalStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeProposal
        fields = ['status']
