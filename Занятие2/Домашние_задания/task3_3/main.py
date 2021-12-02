if __name__ == "__main__":
    def decor_func(fn):
        def wrapper(*args, **kwargs):
            for i in args:
                if not hasattr(type(i), '__iter__'):
                    raise TypeError(f"Объект {i} не является итерируемым")
            for key, values in kwargs.items():
                if not hasattr(type(values), '__iter__'):
                    raise TypeError(f"Объект {key} равный {values} не является итерируемым")
            result = fn(*args, **kwargs)
            return result
        return wrapper

    @decor_func
    def some_func(*args, **kwargs):
        print(args)
        print(kwargs)

    list_ = [1, 2, 3, 4]
    tuple_ = (1, 2, 3)
    dict_ = {1: 'cat', 2: 'dog'}
    int_ = 123456
    str_ = 'Hello World'

    some_func(list_, tuple_, str_, a=1234)
