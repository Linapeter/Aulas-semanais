
from exercises.exercise11_piglatin import translate

def test_word_beginning_with_a() -> None:
    assert translate("apple") == "appleay"

def test_word_beginning_with_e() -> None:
    assert translate("ear") == "earay"

def test_word_beginning_with_i() -> None:
    assert translate("igloo") == "iglooay"

def test_word_beginning_with_o() -> None:
    assert translate("object") == "objectay"

def test_word_beginning_with_u() -> None:
    assert translate("under") == "underay"

def test_word_beginning_with_a_vowel_and_followed_by_a_qu() -> None:
    assert translate("equal") == "equalay"

def test_word_beginning_with_p() -> None:
    assert translate("pig") == "igpay"

def test_word_beginning_with_k() -> None:
    assert translate("koala") == "oalakay"

def test_word_beginning_with_x() -> None:
    assert translate("xenon") == "enonxay"

def test_word_beginning_with_q_without_a_following_u() -> None:
    assert translate("qat") == "atqay"

def test_word_beginning_with_consonant_and_vowel_containing_qu() -> None:
    assert translate("liquid") == "iquidlay"

def test_word_beginning_with_ch() -> None:
    assert translate("chair") == "airchay"

def test_word_beginning_with_qu() -> None:
    assert translate("queen") == "eenquay"

def test_word_beginning_with_qu_and_a_preceding_consonant() -> None:
    assert translate("square") == "aresquay"

def test_word_beginning_with_th() -> None:
    assert translate("therapy") == "erapythay"

def test_word_beginning_with_thr() -> None:
    assert translate("thrush") == "ushthray"

def test_word_beginning_with_sch() -> None:
    assert translate("school") == "oolschay"

def test_word_beginning_with_yt() -> None:
    assert translate("yttria") == "yttriaay"

def test_word_beginning_with_xr() -> None:
    assert translate("xray") == "xrayay"

def test_y_is_treated_like_a_consonant_at_the_beginning_of_a_word() -> None:
    assert translate("yellow") == "ellowyay"

def test_y_is_treated_like_a_vowel_at_the_end_of_a_consonant_cluster() -> None:
    assert translate("rhythm") == "ythmrhay"

def test_y_as_second_letter_in_two_letter_word() -> None:
    assert translate("my") == "ymay"

def test_a_whole_phrase() -> None:
    assert translate("quick fast run") == "ickquay astfay unray"
