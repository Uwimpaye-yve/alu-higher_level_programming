# 4-hidden_discovery.py
import hidden_4

# Print only names that do not start with an underscore
for name in dir(hidden_4):
    if not name.startswith("_"):
        print(name)
