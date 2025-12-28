from core.target import Target
from core.context import Context

t = Target("http://localhost")
c = Context()

t.add_stack("php")
c.add_endpoint("/login")
c.add_param("/login", "username")

print(dict(c))
print(dict(t))
