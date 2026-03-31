from utils.EnumBy import By
from base.Elements import Text, Button, Input, Modal
from base.BasePage import BasePage
from conftest import driver


class ModalPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    #region simple modal

    @property
    def simple_modal_button(self):
        return Button(self.driver, By.ID, "simpleModal")

    @property
    def simple_modal(self):
        return Modal(self.driver, By.ID, "popmake-1318")

    @property
    def simple_modal_text(self):
        return Text(self.simple_modal, By.CLASS_NAME, "pum-content.popmake-content")

    @property
    def simple_modal_close_button(self):
        return Button(self.simple_modal, By.CLASS_NAME, "pum-close.popmake-close")

    #endregion

    #region form modal

    @property
    def form_modal_button(self):
        return Button(self.driver, By.ID, "formModal")

    @property
    def form_modal(self):
        return Modal(self.driver, By.ID, "popmake-674")

    @property
    def name_form_modal_input(self):
        return Input(self.form_modal, By.ID, "g1051-name")

    @property
    def email_form_modal_input(self):
        return Input(self.form_modal, By.ID, "g1051-email")

    @property
    def message_form_modal_input(self):
        return Input(self.form_modal, By.ID, "contact-form-comment-g1051-message")

    @property
    def submit_form_modal_button(self):
        return Button(self.form_modal, By.CLASS_NAME, "pushbutton-wide")

    @property
    def form_modal_text(self):
        return Text(self.form_modal, By.CLASS_NAME, "field-value").find_all()

    #endmodal