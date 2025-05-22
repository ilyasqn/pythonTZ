import pytest
from ads.models.ads import Ad


@pytest.mark.django_db
class TestAdAPI:

    def test_create_ad(self, auth_client, user):
        payload = {
            "title": "Отдам велосипед",
            "description": "Старый, но на ходу",
            "category": "Транспорт",
            "condition": "used"
        }
        response = auth_client.post("/api/ads/", payload, format='json')
        assert response.status_code == 201
        assert Ad.objects.count() == 1
        assert response.data["title"] == payload["title"]
        assert Ad.objects.first().user == user

    def test_update_ad(self, auth_client, user):
        ad = Ad.objects.create(
            user=user,
            title="Старый ноутбук",
            description="Работает с перебоями",
            category="Электроника",
            condition="used"
        )
        payload = {
            "title": "Обновлённый ноутбук",
            "description": "Уже лучше работает",
            "category": "Электроника",
            "condition": "used"
        }
        response = auth_client.put(f"/api/ads/{ad.id}/", payload, format="json")
        assert response.status_code == 200
        ad.refresh_from_db()
        assert ad.title == "Обновлённый ноутбук"

    def test_delete_ad(self, auth_client, user):
        ad = Ad.objects.create(
            user=user,
            title="Удаляемая вещь",
            description="Не нужна больше",
            category="Разное",
            condition="used"
        )
        response = auth_client.delete(f"/api/ads/{ad.id}/")
        assert response.status_code == 204
        assert Ad.objects.count() == 0

    def test_filter_ads(self, auth_client, user):
        Ad.objects.create(user=user, title="Книга", description="Роман", category="Книги", condition="new")
        Ad.objects.create(user=user, title="Лампа", description="Светодиодная", category="Техника", condition="used")

        response = auth_client.get("/api/ads/?category=Книги")
        assert response.status_code == 200
        results = response.data["results"]
        assert len(results) == 1
        assert results[0]["title"] == "Книга"
