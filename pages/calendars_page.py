import random

from utils.EnumBy import By
from base.Elements import Text, Input, Button
from base.BasePage import BasePage
from conftest import driver
from datetime import datetime, timedelta
import calendar



class CalendarsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def text_input(self):
        return Input(self.driver, By.ID, 'g1065-1-selectorenteradate')

    @property
    def submit_button(self):
        return Button(self.driver, By.CLASS_NAME, 'pushbutton-wide')

    @property
    def next_button(self):
        return Button(self.driver, By.CLASS_NAME, 'dp-next')

    @property
    def prev_button(self):
        return Button(self.driver, By.CLASS_NAME, 'dp-prev')

    @property
    def days_button(self):
        return Button(self.driver, By.CLASS_NAME, 'dp-day').find_all()

    @property
    def year_button(self):
        return Button(self.driver, By.CLASS_NAME, 'dp-cal-year')

    @property
    def month_button(self):
        return Button(self.driver, By.CLASS_NAME, 'dp-cal-month')

    @property
    def data_text(self):
        return Text(self.driver, By.CLASS_NAME, 'field-value')

    @property
    def get_months(self) -> dict[str, int]:
        months = list(calendar.month_name)
        result = {}
        for index, name in enumerate(months):
            if name:
                result[name] = index

        return result

    def skip_next_number_of_months(self, count_months: int):
        for index in range(count_months):
            self.next_button.click()

    def skip_prev_number_of_months(self, count_months: int):
        for index in range(count_months):
            self.prev_button.click()

    @staticmethod
    def get_random_date(start_year=2020, end_year=2026):
        start_date = datetime(start_year, 1, 1)
        end_date = datetime(end_year, 12, 31)

        # Считаем разницу в днях и выбираем случайное число
        days_between = (end_date - start_date).days
        random_days = random.randint(0, days_between)

        # Прибавляем дни к начальной дате
        rand_date = start_date + timedelta(days=random_days)

        return {
            "year": rand_date.year,
            "month": rand_date.month,
            "day": rand_date.day
        }

    @staticmethod
    def get_scroll_count(start_year: int, start_month: int, end_year: int, end_month: int) -> tuple[int, str]:
        start_total = start_year * 12 + start_month
        end_total = end_year * 12 + end_month

        diff = end_total - start_total

        if diff > 0:
            return diff, "Right"
        elif diff < 0:
            return abs(diff), "Left"
        else:
            return 0, "Stay"

