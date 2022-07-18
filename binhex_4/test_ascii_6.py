import pytest
from BinHex4 import convert_ASCII_6
import binascii
# binascii encodes when numbers are repeated more than 3 times.

class Test_ASCII_6():

    def test_case_01(self):
        input = [0x1, 0x2, 0x90, 0x90, 0x90, 0x90]
        output = convert_ASCII_6(input)
        assert output == binascii.b2a_hqx(bytearray(input)).decode("utf-8")
    
    def test_case_02(self):
        input = [0x1, 0xFF, 0x23, 0x32, 0x90, 0x55, 0x55, 0x55, 0x55]
        output = convert_ASCII_6(input)
        assert output == binascii.b2a_hqx(bytearray(input)).decode("utf-8")

if __name__ == "__main__":
    exit_code = pytest.main()
    print(exit_code)