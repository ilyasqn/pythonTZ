from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from ads.models.ads import Ad
from ads.serializers import AdSerializer
from ads.permissions import IsOwnerOrReadOnly


class AdListCreateView(generics.ListCreateAPIView):
    queryset = (
        Ad.objects
        .select_related('user')
        .order_by('-created_at')
    )
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'description']
    filterset_fields = ['category', 'condition']

    def perform_create(self, serializer):
        print("DEBUG current user:", self.request.user)
        serializer.save(user=self.request.user)


class AdRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
