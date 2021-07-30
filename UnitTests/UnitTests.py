from RegexHandler import RegexHandler


class UnitTests:

    @staticmethod
    def test_known_output():
        regex_exp = ".*The.*Spain$"
        reg_pattern = RegexHandler.get_regex_pattern(regex_exp)
        dict_matching = RegexHandler.get_lines_matching_reg_pattern_in_txt_file(reg_pattern, "test.ascii")
        assert len(dict_matching.keys()) == 7
        dict_matching = RegexHandler.get_lines_matching_reg_pattern_in_txt_file(reg_pattern, "test2.ascii")
        assert len(dict_matching.keys()) == 20

if __name__ == "__main__":
    UnitTests.test_known_output()


