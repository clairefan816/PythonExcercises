from string_processor import StringProcessor


def test_process_string():
    """Test for process_string function"""
    # Include the following cases
    # "ab" should yield "" as ouptut
    # "ab*" should yield "b" as output
    # "ab^" should yield "ba" as output
    # "^" should yield "" as output
    case = StringProcessor()
    assert case.process_string("ab") == ""
    assert case.process_string("ab*") == "b"
    assert case.process_string("ab^") == "ba"
    assert case.process_string("ab^") == "ba"
    assert case.process_string("^") == ""
