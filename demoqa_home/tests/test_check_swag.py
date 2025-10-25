from pages.swag_labs import SwagLabs


def test_check_icon(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    swag_labs_page.exist_icon()
    swag_labs_page.exist_icon_username()
    swag_labs_page.exist_icon_password()