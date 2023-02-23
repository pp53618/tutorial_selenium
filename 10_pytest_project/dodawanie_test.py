import pytest


@pytest.mark.parametrize("skladnik, suma", [(5,8), (2,6)])
def test_dodawania(skladnik, suma):
    assert skladnik+skladnik == suma, "Suma dwoch takich samych skladników powinna byc równa " + str(skladnik+skladnik)
