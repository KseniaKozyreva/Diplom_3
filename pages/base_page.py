from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Элемент не найден в DOM за {timeout} сек: {locator}"
        )

    def wait_for_element_visible(self, locator, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент не стал видимым за {timeout} сек: {locator}"
        )

    def click_via_js(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def get_element_text_as_int(self, locator, timeout=5):
        try:
            element = self.wait_for_element_visible(locator, timeout)
            return int(element.text)
        except (TimeoutException, ValueError):
            return 0

    def drag_and_drop_via_js(self, source_locator, target_locator):
        source = self.wait_for_element(source_locator)
        target = self.wait_for_element(target_locator)
        
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", source)
        
        js_script = """
        var src = arguments[0];
        var tgt = arguments[1];
        var dataTransfer = new (window.DataTransfer || src.ownerDocument.defaultView.DataTransfer)();
        
        var emit = function(target, type) {
            var event = target.ownerDocument.createEvent('CustomEvent');
            event.initCustomEvent(type, true, true, null);
            event.dataTransfer = dataTransfer;
            target.dispatchEvent(event);
        };
        
        emit(src, 'dragstart');
        emit(tgt, 'dragenter');
        emit(tgt, 'dragover');
        emit(tgt, 'drop');
        emit(src, 'dragend');
        """
        self.driver.execute_script(js_script, source, target)

    def is_element_visible(self, locator, timeout=10):
        try:
            self.wait_for_element_visible(locator, timeout)
            return True
        except TimeoutException:
            return False

    def is_element_invisible(self, locator, timeout=5):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.common.exceptions import TimeoutException
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def refresh_page(self):
        self.driver.refresh()
