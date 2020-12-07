import dataclasses
import uk_mod_check


@dataclasses.dataclass
class TestCase:
    sort_code: int
    account_number: int
    expected_result: bool


TEST_CASES = [
    TestCase( 89999, 66374958, True),
    TestCase(107999, 88837491, True),
    TestCase(202959, 63748472, True),
    TestCase(871427, 46238510, True),
    TestCase(872427, 46238510, True),
    TestCase(871427,  9123496, True),
    TestCase(871427, 99123496, True),
    TestCase(820000, 73688637, True),
    TestCase(827999, 73988638, True),
    TestCase(827101, 28748352, True),
    TestCase(134020, 63849203, True),
    TestCase(118765, 64371389, True),
    TestCase(200915, 41011166, True),
    TestCase(938611,  7806039, True),
    TestCase(938600, 42368003, True),
    TestCase(938063, 55065200, True),
    TestCase(772798, 99345694, True),
    TestCase( 86090,  6774744, True),
    TestCase(309070,  2355688, True),
    TestCase(309070, 12345668, True),
    TestCase(309070, 12345677, True),
    TestCase(309070, 99345694, True),
    TestCase(938063, 15764273, False),
    TestCase(938063, 15764264, False),
    TestCase(938063, 15763217, False),
    TestCase(118764, 64371388, False),
    TestCase(203099, 66831036, False),
    TestCase(203099, 58716970, False),
    TestCase( 89999, 66374959, False),
    TestCase(107999, 88837493, False),
    TestCase( 74456, 12345112, True),
    TestCase( 70116, 34012583, True),
    TestCase( 74456, 11104102, True),
    TestCase(180002,      190, True),
]

for test in TEST_CASES:
    result = uk_mod_check.validate(test.sort_code, test.account_number)
    if result.result != test.expected_result:
        print(f"FAIL: S/C {test.sort_code} A/N {test.account_number} expected {test.expected_result} got {result}")
