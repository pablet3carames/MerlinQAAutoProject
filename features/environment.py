from playwright.sync_api import sync_playwright
import os
import allure


def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()


def after_step(context, step):
    if step.status == "failed":
        screenshot_path = "screenshots/error.png"
        context.page.screenshot(path=screenshot_path, full_page=True)


def after_all(context):
    context.browser.close()
    context.playwright.stop()
