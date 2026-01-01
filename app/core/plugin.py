class Plugin:
    name = "base-plugin"
    description = "Base plugin"
    passive = True

    def __init__(self, session, target, context):
        self.session = session
        self.target = target
        self.context = context

    def run(self) -> dict|None:
        """
        None si le plugin ne detecte rien
        dict si le plugin detecte quelque chose
        le dictionnaire doit etre sous la forme

        {
            "name": "TECHNO_NAME",
            "confidence": x
            "reason": "..."
        }
        """
        raise NotImplementedError