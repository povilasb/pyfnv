from hamcrest import assert_that, is_
import pytest

import fnv


def describe_hash():
    def describe_with_fnv_1a_algorithm():
        def it_returns_the_calculated_hash_for_specified_data():
            data = '\x01\x02\x03\x04'

            assert_that(
                fnv.hash(data, algorithm=fnv.fnv_1a),
                is_(136442159731806137627837275212626352805)
            )

        def it_allows_to_specify_hash_size_in_bits():
            data = '\x01\x02\x03\x04'

            assert_that(
                fnv.hash(data, algorithm=fnv.fnv_1a, bits=64),
                is_(13725386680924731485)
            )

def describe_fnv():
    @pytest.mark.parametrize('hash_bits,initial_hash_value,expected_hash_value', [
        (64, 14695981039346656037, 12638153115695167454),
        (128, 144066263297769815596495629667062367629, 279349696642264188298419300151331525758),
    ])
    def it_returns_the_calculated_hash_for_the_specified_byte(hash_bits,
            initial_hash_value, expected_hash_value):
        assert_that(
            fnv.fnv(initial_hash_value, '\x01', hash_bits),
            is_(expected_hash_value)
        )

def describe_ensure_bits_count():
    def it_returns_unaltered_specified_number_with_bits_count_more_than_number_bit_count():
        assert_that(fnv.ensure_bits_count(10, 16), is_(10))

    def it_returns_number_with_the_specified_bit_count_with_bits_count_less_than_number_bit_count():
        assert_that(fnv.ensure_bits_count(10, 2), is_(2))
