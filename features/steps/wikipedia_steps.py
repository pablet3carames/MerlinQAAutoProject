from behave import given, when, then
from pages.wikipedia_page import WikipediaPage
import allure


@given("el usuario navega a Wikipedia")
@allure.step("Navigate to Wikipedia")
def step_open_wikipedia(context):
    context.wikipedia_page = WikipediaPage(context.page)
    context.wikipedia_page.open()
    context.wikipedia_page.accept_cookies_if_present()
    screenshot_path = "screenshots/navigate.png"
    context.page.screenshot(path=screenshot_path, full_page=True)
    allure.attach.file(
        screenshot_path, name="Screenshot after navigating to Wikipedia", attachment_type=allure.attachment_type.PNG
    )


@when('busca la palabra "automatización"')
@allure.step('Search for the word "automatización"')
def step_search_word(context):
    context.wikipedia_page.search("automatización")
    screenshot_path = "screenshots/search.png"
    context.page.screenshot(path=screenshot_path, full_page=True)
    allure.attach.file(
        screenshot_path,
        name="Screenshot after searching for 'automatización'",
        attachment_type=allure.attachment_type.PNG,
    )


@then("se muestra el año del primer proceso automatico")
@allure.step("Validate the year of the first automatic process")
def step_validate_year(context):
    context.wikipedia_page.validate_first_automation_year()
    screenshot_path = "screenshots/validate.png"
    context.page.screenshot(path=screenshot_path, full_page=True)
    allure.attach.file(
        screenshot_path, name="Screenshot after validating the year", attachment_type=allure.attachment_type.PNG
    )


@then("se toma una captura de la pagina")
@allure.step("Take a screenshot of the page")
def step_take_screenshot(context):
    context.wikipedia_page = WikipediaPage(context.page)
    context.wikipedia_page.take_screenshot()
    allure.attach.file(
        "screenshots/wikipedia_automatizacion.png",
        name="Wikipedia Screenshot",
        attachment_type=allure.attachment_type.PNG,
    )
