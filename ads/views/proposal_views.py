from rest_framework import generics, permissions, status
from ads.models.exchange_proposals import ExchangeProposal
from ads.serializers import ExchangeProposalSerializer
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q


class ProposalCreateView(generics.CreateAPIView):
    queryset = ExchangeProposal.objects.all()
    serializer_class = ExchangeProposalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()


class ProposalListView(generics.ListAPIView):
    serializer_class = ExchangeProposalSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ad_sender', 'ad_receiver', 'status']

    def get_queryset(self):
        user_ads = self.request.user.ad_set.all()
        return ExchangeProposal.objects.filter(
            Q(ad_receiver__in=user_ads) | Q(ad_sender__in=user_ads)
        ).order_by('-created_at', '-id')


class ProposalUpdateStatusView(generics.UpdateAPIView):
    queryset = ExchangeProposal.objects.all()
    serializer_class = ExchangeProposalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.ad_receiver.user != request.user:
            return Response({"detail": "Нет прав для изменения статуса."}, status=status.HTTP_403_FORBIDDEN)
        new_status = request.data.get('status')
        if new_status == 'accepted':
            ad_sender = instance.ad_sender
            ad_receiver = instance.ad_receiver

            sender_user = ad_sender.user
            receiver_user = ad_receiver.user

            ad_sender.user = receiver_user
            ad_receiver.user = sender_user

            ad_sender.save()
            ad_receiver.save()
        return super().partial_update(request, *args, **kwargs)
