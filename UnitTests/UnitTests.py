import sys
import os
sys.path.append(os.getcwd())
from RegexHandler import RegexHandler


class UnitTests:

    @staticmethod
    def functionality_test_should_pass():
        '''
        This test should pass, tests full flow
        :return: None
        '''
        regex_exp = ".*The.*Spain$"
        reg_pattern = RegexHandler.get_regex_pattern(regex_exp)
        dict_matching = RegexHandler.get_lines_matching_reg_pattern_in_txt_file(reg_pattern, "UnitTests/test.ascii")
        assert len(dict_matching.keys()) == 7
        dict_matching = RegexHandler.get_lines_matching_reg_pattern_in_txt_file(reg_pattern, "UnitTests/test2.ascii")
        assert len(dict_matching.keys()) == 20

    @staticmethod
    def test_should_fail_file_not_found():
        '''
        Negative test - should fail, no file exists
        :return: None
        '''
        regex_exp = ".*The.*Spain$"
        reg_pattern = RegexHandler.get_regex_pattern(regex_exp)
        dict_res = RegexHandler.get_lines_matching_reg_pattern_in_txt_file(reg_pattern, "UnitTests/test4.ascii")
        assert dict_res is FileNotFoundError

    @staticmethod
    def functionality_test_should_pass_no_match():
        '''
        This test should pass, tests full flow but verify that the results are 0
        :return: None
        '''
        regex_exp = ".*fne*sse$"
        reg_pattern = RegexHandler.get_regex_pattern(regex_exp)
        dict_matching = RegexHandler.get_lines_matching_reg_pattern_in_txt_file(reg_pattern, "UnitTests/test.ascii")
        assert len(dict_matching.keys()) == 0
        dict_matching = RegexHandler.get_lines_matching_reg_pattern_in_txt_file(reg_pattern, "UnitTests/test2.ascii")
        assert len(dict_matching.keys()) == 0


if __name__ == "__main__":
    UnitTests.functionality_test_should_pass()
    UnitTests.test_should_fail_file_not_found()
    UnitTests.functionality_test_should_pass_no_match()


