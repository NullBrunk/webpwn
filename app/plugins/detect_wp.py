from core.plugin import Plugin

class DetectWordpress(Plugin):
    name = "WordPress"
    description = "Wordpress detection plugin"
    passive = True

    def run(self):
        if "/wp-login.php" in self.context.endpoints:
            return {
                "tech": "WordPress",
                "confidence": 1,
                "reason": "Found /wp-login.php"
            }
        
        if(self.session.get("/wp-login.php").status_code == 200):
            return {
                "tech": "WordPress",
                "confidence": 1,
                "reason": "Found /wp-login.php"
            }

        return None