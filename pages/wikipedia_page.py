import re


class WikipediaPage:

    def __init__(self, page):
        self.page = page
        self.search_box = 'form#searchform input[type="search"]'

    def open(self):
        self.page.goto("https://es.wikipedia.org/wiki/Wikipedia:Portada")

    def accept_cookies_if_present(self):
        try:
            self.page.get_by_role("button", name="Accept all").click(timeout=3000)
        except:
            pass

    def search(self, text):
        self.page.fill(self.search_box, "automatización")

        search_form = self.page.locator("#searchform")

        search_form.locator('ul[role="listbox"]').wait_for()

        search_form.get_by_role("option").nth(0).click()

    def validate_first_automation_year(self):
        content = self.page.text_content("body")
        assert "1785" in content, "El año 1785 no se encontró en la página"

    def take_screenshot(self):
        self.page.screenshot(path="screenshots/wikipedia_automatizacion.png", full_page=True)
