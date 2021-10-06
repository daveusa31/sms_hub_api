import typing

class Activation:
    def __init__(
            self,
            activation_id: typing.Union[str, int],
            number: typing.Union[str, int] = None,
    ):
        self.activation_id = activation_id
        self.number = number
