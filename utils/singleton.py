def singleton(cls):
    """
    Singleton class that will be used as a decorator to initialize any class only once
    """
    __instance = {}

    def wrapper(*args, **kwargs):
        if cls not in __instance:
            __instance[cls] = cls(*args, **kwargs)
        return __instance[cls]
    return wrapper
