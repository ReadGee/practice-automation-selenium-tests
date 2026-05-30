from base.BaseElement import BaseElement

class Button(BaseElement):
    pass

class Text(BaseElement):
    pass

class Input(BaseElement):
    pass

class Checkbox(BaseElement):
    pass

class Radio(BaseElement):
    pass

class ContextMenu(BaseElement):
    pass

class Slider(BaseElement):
    def set_value(self, value: int):
        """Устанавливает значение слайдера через JavaScript и вызывает события изменения."""
        target_element = self.find()

        script = f"arguments[0].value = {value}; arguments[0].dispatchEvent(new Event('input')); arguments[0].dispatchEvent(new Event('change'));"
        self.driver.execute_script(script, target_element)

class Modal(BaseElement):
    pass

class Spinner(BaseElement):
    pass

class Other(BaseElement):
    pass

class Image(BaseElement):
    def is_broken(self) -> bool:
        target_element = self.find()
        is_valid_image = self.driver.execute_script(
            "return arguments[0].complete && "
            "typeof arguments[0].naturalWidth != 'undefined' && "
            "arguments[0].naturalWidth > 0;",
            target_element
        )
        return not is_valid_image