from core.plugin import Plugin
import importlib
import pkgutil

class Detector:
    def __init__(self, session, target, context):
        self.session = session
        self.target = target
        self.context = context
        self.results = {}

    def run(self):
        import plugins

        for _, module_name, _ in pkgutil.iter_modules(plugins.__path__):
            module = importlib.import_module(f"plugins.{module_name}")

            for attr in dir(module):
                obj = getattr(module, attr)

                if (
                    isinstance(obj, type)
                    and issubclass(obj, Plugin)
                    and obj is not Plugin
                ):
                    plugin = obj(self.session, self.target, self.context)

                    print(f"[+] Running plugin: {plugin.name}")

                    try:
                        result = plugin.run()
                    except Exception as e:
                        print(f"[-] Plugin {plugin.name} crashed: {e}")
                        continue

                    if result:
                        self.results[plugin.name] = result

