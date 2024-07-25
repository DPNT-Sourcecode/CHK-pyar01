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
        assert checkout_solution.checkout("AAAAA") == 200
        assert checkout_solution.checkout("AAAAAA") == 250
        assert checkout_solution.checkout("AAAAAAA") == 300
        assert checkout_solution.checkout("AAAAAAAA") == 330
        assert checkout_solution.checkout("AAAAAAAAA") == 380
        assert checkout_solution.checkout("AAAAAAAAAA") == 400
        assert checkout_solution.checkout("EEB") == 80
        assert checkout_solution.checkout("EEBBB") == 125

    def test_checkout_r3(self):
        assert checkout_solution.checkout("FFF") == 20
        assert checkout_solution.checkout("FF") == 20
        assert checkout_solution.checkout("F") == 10
        assert checkout_solution.checkout("FFFF") == 30

    def test_checkout_r4(self):
        assert checkout_solution.checkout("RRR") == 150
        assert checkout_solution.checkout("RRRQ") == 150
        assert checkout_solution.checkout("U") == 40
        assert checkout_solution.checkout("UU") == 80
        assert checkout_solution.checkout("UUU") == 120
        assert checkout_solution.checkout("UUUU") == 120

    def test_checkout_r5(self):
        assert checkout_solution.checkout("STX") == 45
        assert checkout_solution.checkout("STXX") == 62


