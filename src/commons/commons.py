import pathlib
import requests


def import_input(YEAR : str, DAY : str) -> str | None:
    path = pathlib.Path() / f"input/aoc_{YEAR}_day{DAY}_input.txt"
    input_data = None

    if not path.exists():
        url = f"https://adventofcode.com/{YEAR}/day/{DAY}/input"
        session_cookie = "53616c7465645f5f94c0f974ea29e8964ec9e4222e1b5614105a5b78b57f1f7868d0bc93f0942f23c725e3433e1315c4c6a9d1ce3997a4f20aa400ad6b414001"
        cookies = {'session': session_cookie}

        try:
            response = requests.get(url, cookies=cookies)
            response.raise_for_status()
            input_data = response.text
            with open(path, "w") as f:
                f.write(input_data)

        except requests.exceptions.HTTPError as e:
            print(f"❌ HTTP Error: {e}")
            print("Double-check your SESSION_COOKIE, YEAR, and DAY values.")

        except requests.exceptions.RequestException as e:
            print(f"❌ An error occurred: {e}")

        except OSError as e:
            print(f"❌ OS Error: {e}")

    else:
        try:
            with open(path, 'r') as f:
                input_data = f.read()

        except OSError as e:
            print(f"❌ OS Error: {e}")

    return input_data