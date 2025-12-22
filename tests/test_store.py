import allure
import requests
import pytest


BASE_URL = "http://5.181.109.28:9090/api/v3"



@allure.feature("Store")
class TestStore:


    @allure.title("Попытка размещения заказа")
    def test_store_post_order(self, create_order):

        with allure.step("Проверка статуса ответа и данных созданного заказа"):
            order = create_order

## сначала в данном автотесте у меня была обычная структура без фикстуры
## но затем я решил попробовать автоматизировать с ее использованием

    @allure.title("Получение информации о заказе по ID")
    def test_store_get_order_by_id(self, create_order):

        with allure.step("Получение ID созданного заказа"):
            order_id = create_order["id"]

        with allure.step("Отправка запроса на получение информации о заказе по ID"):
            response = requests.get(url=f"{BASE_URL}/store/order/{order_id}")

        with allure.step("Проверка статуса ответа и данных питомца"):
            assert response.status_code == 200, "Код ответа не совпал с ожидаемым"
            assert response.json()["id"] == order_id


    @allure.title("Удаление заказа по ID")
    def test_store_delete_order_by_id(self, create_order):

        with allure.step("Получение ID созданного заказа"):
            order_id = create_order["id"]

        with allure.step("Отправка запроса на удаление заказа по ID"):
            response = requests.delete(url=f"{BASE_URL}/store/order/{order_id}")

        with allure.step("Проверка статуса ответа"):
            assert response.status_code == 200, "Код ответа не совпал с ожидаемым"

        with allure.step("Отправка запроса на получение информации о заказе по ID"):
            response = requests.get(url=f"{BASE_URL}/store/order/{order_id}")

        with allure.step("Проверка статуса ответа"):
            assert response.status_code == 404, "Код ответа не совпал с ожидаемым"


    @allure.title("Попытка получить информацию о несуществующем заказе")
    def test_store_get_nonexistent_order_by_id(self):
        with allure.step("Отправка запроса на получение информации о несуществующем заказе"):
            response = requests.get(url=f"{BASE_URL}/store/order/9999")

        with allure.step("Проверка статуса ответа"):
            assert response.status_code == 404, "Код ответа не совпал с ожидаемым"


    @allure.title("Получение инвентаря магазина")
    def test_store_get_inventory(self):
        with allure.step("Отправка запроса на получение инвентаря магазина"):
            response = requests.get(url=f"{BASE_URL}/store/inventory")

        with allure.step("Проверка статуса ответа и формата данных в ответе"):
            assert response.status_code == 200, "Код ответа не совпал с ожидаемым"
            response_json = response.json()
            assert isinstance(response_json, dict)

            # Хотел написать еще так, так вроде тоже можно было, но последний вариант наиболее подходящий
            # assert response.json() == {
            #     "approved": 50
            # }
