import pytest
from du01_ComplexNumber import ComplexNumber

class TestComplexNumber:
    def setup_method(self):
        print("\nThe magic is about to happen!")

    def teardown_method(self):
        print("\nOUT OF MANA, SEND MORE DUDES (process finished flawlessly)")

    def test_add(self):
        # Sčítání kladných
        c1 = ComplexNumber(1,2)
        c2 = ComplexNumber(3,4)
        assert c1.add(c2) == ComplexNumber(4,6)     #Exp. 4+4i
        # Sčítání záporných
        c3 = ComplexNumber(-1, -2)
        c4 = ComplexNumber(3, 4)
        assert c3.add(c4) == ComplexNumber(2, 2)    #Exp. 2+2i
        #Sčítání s nulou
        c5 = ComplexNumber(0, 0)
        assert c1.add(c5) == c1     #Exp. 0+0i

    def test_subtract(self):
        #Odčítání kladných
        c1 = ComplexNumber(5,6)
        c2 = ComplexNumber(2,3)
        assert c1.subtract(c2) == ComplexNumber(3,3)    #Exp. 3+3i
        # Odčítání záporných
        c3 = ComplexNumber(-1, -2)
        c4 = ComplexNumber(3, 4)
        assert c3.subtract(c4) == ComplexNumber(-4, -6)     #Exp. -4-6i
        #Odčítání s nulou
        c5 = ComplexNumber(0, 0)
        assert c1.subtract(c5) == c1    #Exp. 0-0i

    def test_multiply(self):
        # Násobení kladných
        c1 = ComplexNumber(5, 6)
        c2 = ComplexNumber(2, 3)
        assert c1.multiply(c2) == ComplexNumber(10, 18)     #Exp. 10+18i
        # Násobení záporných
        c3 = ComplexNumber(-1, -2)
        c4 = ComplexNumber(3, 4)
        assert c3.multiply(c4) == ComplexNumber(-3, -8)     #Exp. -3-8i
        # Nulou
        c5 = ComplexNumber(0, 0)
        assert c1.multiply(c5) == ComplexNumber(0, 0)   #Exp. 0+0i

    def test_divide(self):
        #Dělení kladným
        c1 = ComplexNumber(4, 2)
        c2 = ComplexNumber(2, -2)
        assert c1.divide(c2) == ComplexNumber(0.5, 1.5)     #Exp. 0.5+1.5i
        #Dělení negativním číslem
        c3 = ComplexNumber(-4, -2)
        c4 = ComplexNumber(2, -2)
        assert c3.divide(c4) == ComplexNumber(-0.5, -1.5)       #Exp. -0.5-1.5i
        # Dělení sebou
        assert c1.divide(c1) == ComplexNumber(1, 0)     #Exp. 1+0i

    def test_divide_by_zero(self):
        c1 = ComplexNumber(1, 1)
        c2 = ComplexNumber(0, 0)
        with pytest.raises(ZeroDivisionError):
            c1.divide(c2)

    def test_conjugate(self):
        c = ComplexNumber(3,4)
        assert c.conjugate() == ComplexNumber(3, -4)
        # Test konjugátu 1
        c2 = ComplexNumber(3, -4)
        assert c2.conjugate() == ComplexNumber(3,4)
        # Test konjugátu 2
        c3 = ComplexNumber(5,0)
        assert c3.conjugate()==ComplexNumber(5,0)

    def test_absolute_value(self):
        c = ComplexNumber(3,4)
        assert c.absolute_value() == 5

    def test_comparisons(self):
        c1 = ComplexNumber(3,4)
        c2 = ComplexNumber(1,1)
        assert c1 > c2
        assert c2 < c1

    def test_repr_str(self):
        c = ComplexNumber(3,-4)
        assert repr(c) == "ComplexNumber(3, -4)"
        assert str(c) == "3 - 4i"