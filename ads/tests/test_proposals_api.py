import pytest
from ads.models.exchange_proposals import ExchangeProposal


@pytest.mark.django_db
class TestExchangeProposalAPI:

    def test_create_proposal(self, auth_client, ad_sender, ad_receiver):
        payload = {
            "comment": "Хочу обменяться",
            "status": "pending",
            "ad_sender": ad_sender.id,
            "ad_receiver": ad_receiver.id
        }
        response = auth_client.post("/api/proposals/create/", payload, format="json")
        assert response.status_code == 201
        assert ExchangeProposal.objects.count() == 1
        assert response.data["comment"] == payload["comment"]

    def test_list_proposals(self, auth_client, ad_sender, ad_receiver):
        ExchangeProposal.objects.create(
            ad_sender=ad_sender,
            ad_receiver=ad_receiver,
            comment="Тестовый обмен",
            status="pending"
        )
        response = auth_client.get("/api/proposals/")
        assert response.status_code == 200
        assert any("Тестовый обмен" in p["comment"] for p in response.data["results"])

    def test_update_proposal_status(self, auth_client, user, ad_sender, ad_receiver):
        proposal = ExchangeProposal.objects.create(
            ad_sender=ad_sender,
            ad_receiver=ad_receiver,
            comment="Для изменения статуса",
            status="pending"
        )
        payload = {"status": "accepted"}
        response = auth_client.patch(f"/api/proposals/{proposal.id}/", payload, format="json")
        assert response.status_code == 200
        proposal.refresh_from_db()
        assert proposal.status == "accepted"
