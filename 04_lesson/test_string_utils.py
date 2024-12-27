import pytest
from StringUtils import StringUtils


# Utils №1
@pytest.mark.parametrize(
    "input_text, result", [
        ("house", "House"),
        ("my house", "My house"),
        ("House", "House")
    ])
def test_capitilize_positive(input_text, result):
    string_utils = StringUtils()
    assert string_utils.capitilize(input_text) == result


@pytest.mark.parametrize(
    "input_text, result", [
        pytest.param("", "", marks=pytest.mark.xfail),
        pytest.param(" ", " ", marks=pytest.mark.xfail),
        pytest.param("123", "123", marks=pytest.mark.xfail)
    ])
def test_capitilize_negative(input_text, result):
    string_utils = StringUtils()
    assert string_utils.capitilize(input_text) == result


# Utils №2
@pytest.mark.parametrize(
    "input_text, result", [
        (" house", "house"),
        ("  house", "house"),
        ("house", "house"),
        (" 123", "123")
    ])
def test_trim_positive(input_text, result):
    string_utils = StringUtils()
    assert string_utils.trim(input_text) == result


@pytest.mark.parametrize(
    "input_text, result", [
        pytest.param("", "", marks=pytest.mark.xfail)
    ])
def test_trim_negative(input_text, result):
    string_utils = StringUtils()
    assert string_utils.trim(input_text) == result


# Utils №3
@pytest.mark.parametrize(
    "input_text, delimeter, result", [
        ("city,street", ",", ["city", "street"]),
        ("18,11,24", ",", ["18", "11", "24"]),
        ("8;1;4", ";", ["8", "1", "4"]),
        ("8/1/4", "/", ["8", "1", "4"]),
        ("2,5,7,9", ",", ["2", "5", "7", "9"])
    ])
def test_to_list_positive(input_text, delimeter, result):
    string_utils = StringUtils()
    assert string_utils.to_list(input_text, delimeter) == result


@pytest.mark.parametrize(
    "input_text, delimeter, result", [
        pytest.param("", "", [""], marks=pytest.mark.xfail)
    ])
def test_to_list_negative(input_text, delimeter, result):
    string_utils = StringUtils()
    assert string_utils.to_list(input_text, delimeter) == result


# Utils №4
@pytest.mark.parametrize(
    "input_text, symbol, result", [
        ("house", "u", True),
        ("my house", "o", True),
        ("House", "i", False)
    ])
def test_contains_positive(input_text, symbol, result):
    string_utils = StringUtils()
    assert string_utils.contains(input_text, symbol) == result


# Utils №5
@pytest.mark.parametrize(
    "input_text, symbol, result", [
        ("house", "u", "hose"),
        ("my house", "my ", "house"),
        ("29.11.1995", ".1995", "29.11"),
        ("football", "", "football")
    ])
def test_delete_symbol_positive(input_text, symbol, result):
    string_utils = StringUtils()
    assert string_utils.delete_symbol(input_text, symbol) == result


@pytest.mark.parametrize(
    "input_text, symbol, result", [
        pytest.param("house", "k", "", marks=pytest.mark.xfail)
    ])
def test_delete_symbol_negative(input_text, symbol, result):
    string_utils = StringUtils()
    assert string_utils.delete_symbol(input_text, symbol) == result


# Utils №6
@pytest.mark.parametrize(
    "input_text, symbol, result", [
        ("House", "H", True),
        ("my house", "h", False),
        ("29.11.1995", "9", False),
        ("Football", "F", True)
    ])
def test_starts_with_positive(input_text, symbol, result):
    string_utils = StringUtils()
    assert string_utils.starts_with(input_text, symbol) == result


@pytest.mark.parametrize(
    "input_text, symbol, result", [
        pytest.param("House", None, "", marks=pytest.mark.xfail),
        pytest.param("House", "", "", marks=pytest.mark.xfail)
    ])
def test_starts_with_negative(input_text, symbol, result):
    string_utils = StringUtils()
    assert string_utils.starts_with(input_text, symbol) == result


# Utils №7
@pytest.mark.parametrize(
    "input_text, symbol, result", [
        ("House", "e", True),
        ("my house", "h", False),
        ("29.11.1995", "9", False),
        ("Football club", "b", True)
    ])
def test_end_with_positive(input_text, symbol, result):
    string_utils = StringUtils()
    assert string_utils.end_with(input_text, symbol) == result


@pytest.mark.parametrize(
    "input_text, symbol, result", [
        pytest.param("Football", None, "", marks=pytest.mark.xfail),
        pytest.param("House", "", "", marks=pytest.mark.xfail)
    ])
def test_end_with_negative(input_text, symbol, result):
    string_utils = StringUtils()
    assert string_utils.end_with(input_text, symbol) == result


# Utils №8
@pytest.mark.parametrize(
    "string, result", [
        ("", True),
        (" ", True),
        ("    ", True),
        ("Football club", False),
        ("123", False),
        (".", False)
    ])
def test_is_empty_positive(string, result):
    string_utils = StringUtils()
    assert string_utils.is_empty(string) == result


@pytest.mark.parametrize(
    "string, result", [
        pytest.param(None, "", marks=pytest.mark.xfail)
    ])
def test_is_empty_negative(string, result):
    string_utils = StringUtils()
    assert string_utils.is_empty(string) == result


# Utils №9
@pytest.mark.parametrize(
    "list, joiner, result", [
        (["city", "street", "house"], ", ", "city, street, house"),
        (["18", "11", "24"], ", ", "18, 11, 24"),
        (["красно", "синий"], "-", "красно-синий"),
        (["Football", "club"], " ", "Football club")
    ])
def test_list_to_string_positive(list, joiner, result):
    string_utils = StringUtils()
    assert string_utils.list_to_string(list, joiner) == result


@pytest.mark.parametrize(
    "list, joiner, result", [
        pytest.param([""], ", ", "", marks=pytest.mark.xfail),
        pytest.param([None], ", ", "", marks=pytest.mark.xfail),
        pytest.param(["Football", "club"], "", "", marks=pytest.mark.xfail)
    ])
def test_list_to_string_negative(list, joiner, result):
    string_utils = StringUtils()
    assert string_utils.to_list(list, joiner) == result
