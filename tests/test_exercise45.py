from requests import get

from exercises.exercise45_PE22 import names_scores

# with open(Path(join(Path(__file__).parent, "data", "exercise45.txt"))) as file:
#     content = file.read()
#     names = content.replace('"', '').split(',')

url = "https://projecteuler.net/resources/documents/0022_names.txt"
response = get(url)
raw_text = response.text
names = raw_text.replace('"', "").split(",")


def test_exercise45() -> None:
    assert names_scores(names) == 871_198_282
