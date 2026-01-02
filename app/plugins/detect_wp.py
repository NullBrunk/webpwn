from core.plugin import Plugin

class DetectWordpress(Plugin):
    name = "WordPress"
    description = "Wordpress detection plugin"
    passive = False

    def run(self):
        score = 0
        evidence = []

        # ========= PASSIVE CHECKS =========
        homepage = self.session.get("/")
        if homepage and "text/html" in homepage.headers.get("Content-Type", ""):
            html = homepage.text.lower()

        if "wp-content" in html:
            score += 2
            evidence.append("wp-content found in HTML")

        if "wp-includes" in html:
            score += 2
            evidence.append("wp-includes found in HTML")

        if "wp-emoji-release.min.js" in html:
            score += 1
            evidence.append("wp-emoji script found")

        if 'name="generator"' in html and "wordpress" in html:
            score += 3
            evidence.append("meta generator WordPress")

        # Header Link wp-json
        link_header = homepage.headers.get("Link", "")
        if "wp-json" in link_header:
            score += 2
            evidence.append("wp-json found in Link header")

         # ========= ACTIVE CHECKS =========
        paths = [
            "/wp-login.php",
            "/wp-admin/",
            "/wp-content/",
            "/wp-includes/",
        ]

        for path in paths:
            r = self.session.get(path, timeout=5)
            if not r:
                continue

            if r.status_code in (200, 301, 302, 403):
                score += 2
                evidence.append(f"{path} reachable ({r.status_code})")

        
        # ========= DECISION =========
        if score >= 4:
            return {
                "cms": "WordPress",
                "confidence": min(score * 10, 100),
                "score": score,
                "evidence": evidence
            }

        return None