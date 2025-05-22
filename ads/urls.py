from django.urls import path
from ads.views.ad_views import AdListCreateView, AdRetrieveUpdateDestroyView
from ads.views.proposal_views import ProposalCreateView, ProposalListView, ProposalUpdateStatusView

urlpatterns = [
    path('ads/', AdListCreateView.as_view(), name='ad-list-create'),
    path('ads/<int:pk>/', AdRetrieveUpdateDestroyView.as_view(), name='ad-detail'),
    path('proposals/', ProposalListView.as_view(), name='proposal-list'),
    path('proposals/create/', ProposalCreateView.as_view(), name='proposal-create'),
    path('proposals/<int:pk>/', ProposalUpdateStatusView.as_view(), name='proposal-update'),
]
