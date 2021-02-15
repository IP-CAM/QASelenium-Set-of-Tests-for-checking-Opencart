import pytest

from pages.LoginPage import LoginPage


@pytest.fixture
def right_user():
    return "user", "bitnami"


@pytest.fixture
def product_page(base_url, right_user, browser):
    url = f"{base_url}/admin/"
    login_page = LoginPage(browser, url)
    login_page.open()
    page = login_page.login(*right_user)
    page.get_top_item_in_left_menu_by_name('Catalog > Products')
    return page


def test_title_of_product(product_page):
    """проверка заголовка страницы"""
    assert product_page.get_title() == 'Products'


def test_count_of_column(product_page):
    """проверка количества колонок в таблице товаров"""
    assert len(product_page.get_product_table_headers()) == 8


def test_name_column_of_products_table(product_page):
    """проверка наименования колонок в таблице"""
    names = ["Image", "Product Name", "Model", "Price", "Quantity", "Status", "Action"]
    for idx, col in enumerate(product_page.get_product_table_headers()[1:]):
        assert names[idx] in col.text
