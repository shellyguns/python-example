class Phone:
    number = None
    model = None
    weight = None
    name = None
    calling_number = None

    def __init__(self, number: str, model: str, weight: str):
        self.number = number
        self.model = model
        self.weight = weight

    def __str__(self):
        return 'number = '+self.number + ', model = '+self.model + ', weight = '+self.weight

    def receive_call(self, name: str, calling_number: str = None):
        if not isinstance(name, str):
            raise TypeError(f'Argument "name" must be a string, not {type(name)}')
        if calling_number is None:
            return f'{name} is calling on {self.model}'
        else:
            if not isinstance(calling_number, str):
                raise TypeError(f'Argument "calling_number" must be a string, not {type(calling_number)}')
            return f'{name} is calling on {self.model} with number {calling_number}'

    def get_number(self):
        return self.number

    def send_message(self, *numbers: str):
        for number in numbers:
            if not isinstance(number, str):
                raise TypeError(f'Argument "number" must be a string, not {type(number)}')
        return f'{self.model} sends message on the following number(s): {numbers}'


if __name__ == '__main__':
    iphone = Phone("0935553535", "iPhone", "100")
    samsung = Phone("0685553535", "Samsung", "110")
    sony = Phone("0955553535", "SONY", "120")
    print(iphone)
    print(samsung)
    print(sony)
    print(iphone.receive_call("Volodya", "88005553535"))
    print(iphone.get_number())
    print(samsung.receive_call("Volodya"))
    print(samsung.get_number())
    print(sony.receive_call("Volodya"))
    print(sony.get_number())
    print(sony.send_message("88005553535", "0957851590"))
    print(iphone.send_message("88005553535"))
