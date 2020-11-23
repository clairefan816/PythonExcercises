from text_cleaner import TextCleaner


def test_read_file():
    tc = TextCleaner('test.txt')
    assert tc.read_file() == ["you fit into me", "margaret atwood",
                              "you fit into me COMMA like a hook into an eye",
                              "a fish hook", "an open eye"]
