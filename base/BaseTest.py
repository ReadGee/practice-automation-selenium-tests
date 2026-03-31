import pytest
import random
from string import ascii_letters

@pytest.mark.usefixtures("driver")
class BaseTest:

    @property
    def get_invalid_email(self) -> str:
        is_symbol = bool(random.getrandbits(1))
        one_part = "".join(random.choices(ascii_letters, k=random.randrange(3, 15)))
        two_part = "".join(random.choices(ascii_letters, k=random.randrange(2, 5)))
        three_part = "".join(random.choices(ascii_letters, k=random.randrange(0, 5)))
        return f"{one_part}{"@" if is_symbol else ""}{two_part}{"." if not is_symbol else ""}{three_part}"

    @property
    def get_valid_email(self) -> str:
        one_part = "".join(random.choices(ascii_letters, k=random.randrange(3, 15)))
        two_part = "".join(random.choices(ascii_letters, k=random.randrange(2, 5)))
        three_part = "".join(random.choices(ascii_letters, k=random.randrange(1, 5)))
        return f"{one_part}@{two_part}.{three_part}"

    @property
    def get_invalid_username(self) -> str:
        username = "".join(random.choices(ascii_letters, k=random.randrange(0, 3)))
        return username

    @property
    def get_valid_username(self) -> str:
        username = "".join(random.choices(ascii_letters, k=random.randrange(4, 12)))
        return username

    @property
    def get_invalid_password(self) -> str:
        password = "".join(random.choices(ascii_letters, k=random.randrange(0, 6)))
        return password

    @property
    def get_valid_password(self) -> str:
        password = "".join(random.choices(ascii_letters, k=random.randrange(6, 15)))
        return password

    def get_random_text(self, length: int) -> str:
        text = "".join(random.choices(ascii_letters, k=random.randrange(0, length)))
        return text
