from solutions.CHK import checkout_solution

class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout("ABC") == 100
        assert checkout_solution.checkout("AAA") == 130
        assert checkout_solution.checkout("BB") == 45
        assert checkout_solution.checkout("BBB") == 75
        assert checkout_solution.checkout("AAAABBB") == 255
        assert checkout_solution.checkout("AAAABBBDDC") == 305
        assert checkout_solution.checkout("AAAABBB,DDC") == -1