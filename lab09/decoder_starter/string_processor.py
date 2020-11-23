from stack import Stack


class StringProcessor:
    """Class for processing strings"""

    def process_string(self, line):
        st = Stack()
        solution = ""

        for char in line:
            if char == "*":
                solution += (st.pop())
            elif char == "^":
                solution += (st.pop())
                solution += (st.pop())
            else:
                st.push(char)
        return solution
