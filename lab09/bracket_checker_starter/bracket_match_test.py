from bracket_match import BracketMatch


def test_brackets_match():
    """Test brackets_match method"""
    # Include the following cases in your test:
    # "()" should succeed
    # "a(a[a])a({a})" should succeed
    # "(" should not succeed
    # "(}" should not succeed
    # "a(a(a)a(a)" should not succeed
    # "aa(a))a(a)" should not succeed
    case = BracketMatch()
    assert case.brackets_match("()")
    assert case.brackets_match("a(a[a])a({a})")
    assert not case.brackets_match("(")
    assert not case.brackets_match("(}")
    assert not case.brackets_match("a(a(a)a(a)")
    assert not case.brackets_match("aa(a))a(a)")
