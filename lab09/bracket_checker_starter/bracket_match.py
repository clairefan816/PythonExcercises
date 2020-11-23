from stack import Stack


class BracketMatch:
    """Class for evaluating parenthetical strings"""
    # TODO: Implement bracket matching functionality
    # as required by bracket_checker.py and by
    # bracket_match_test.py

    def is_match(self, char, top):
        if (char == ")" and top == "(") or (char == "]" and top == "[") or(
             char == "}" and top == "{"):
            return char
        else:
            return False

    def brackets_match(self, line):
        s = Stack()
        for char in line:
            if char in {"(", "[", "{"}:
                s.push(char)
            elif char in {")", "]", "}"}:
                top = s.peek()
                if self.is_match(char, top):
                    s.pop()
                else:
                    return False
        if s.peek():
            return False
        return True
