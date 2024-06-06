class Stack:
    """Provides stack container"""
    def __init__(self):
        self._stack = []

    def push(self, data):
        self._stack.append(data)

    def pop(self):
        if not self._stack:
            return None
        return self._stack.pop()

    def get(self):
        if not self._stack:
            return None
        return self._stack[-1]

    def length(self):
        return len(self._stack)

    def __str__(self):
        return f"Stack{self._stack}"

    def __repr__(self):
        return f"Stack{self._stack!r}"
