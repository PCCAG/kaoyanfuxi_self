def overload(func):
    func_dict = {}

    def wrapper(*args, **kwargs):
        key = (func.__name__, len(args), tuple(arg.__class__ for arg in args))
        if key in func_dict:
            return func_dict[key](*args, **kwargs)
        else:
            raise TypeError(f"No matching function for {func.__name__}")

    def register(*types):
        def decorator(overloaded_func):
            key = (func.__name__, len(types), types)
            func_dict[key] = overloaded_func
            return wrapper

        return decorator

    wrapper.register = register
    return wrapper


@overload
def example_function(arg):
    print(f"Single argument: {arg}")


@example_function.register(int)
def example_function_int(arg):
    print(f"Integer argument: {arg}")


@example_function.register(str)
def example_function_str(arg):
    print(f"String argument: {arg}")


@example_function.register(int, str)
def example_function_int_str(arg1, arg2):
    print(f"Integer and String arguments: {arg1}, {arg2}")


# Test the overloaded function
example_function(42)
example_function("Hello")
example_function(42, "World")  # type: ignore
