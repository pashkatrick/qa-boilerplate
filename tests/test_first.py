from soft_assert import verify, check


class TestFirst:
    def test_first(self):
        assert 1 == 1

    def test_second(self):
        assert 1 != 2

    def test_third(self):
        with verify():
            check(1 == 1)
            check(1 != 1)
            check(1 != 1)
