from os import environ
from typing import Final


class TgKeys:
    TOKEN: Final = environ.get('TOKEN', 'define me!')
    ID_FOR_ANSWER: Final = environ.get('ID_FOR_ANSWER', 'define me!')


