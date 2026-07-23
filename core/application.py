class Application:
    """
    قلب نرم افزار
    فقط یک نمونه از این کلاس در کل برنامه وجود دارد.
    """

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):

        if hasattr(self, "_initialized"):
            return

        self._initialized = True

        self.camera = None
        self.renderer = None
        self.viewport = None
        self.document = None
        self.command_manager = None
        self.input_manager = None