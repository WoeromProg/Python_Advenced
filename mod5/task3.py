class BlockErrors:
    def __init__(self, err_types):
        self.err_types = err_types

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            if True not in [issubclass(exc_type, err_types) for err_types in self.err_types]:
                print(f"Ignored error of type '{exc_type.__name__}': {exc_val}")
                return False
        return True

