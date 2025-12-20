import pathlib
import requests


def get_aoc_url(year : int, day : int) -> str:
    return f"https://adventofcode.com/{year}/day/{day}"

def get_aoc_code_path(year : int, day : int) -> str:
    return pathlib.Path() / "src" / f"aoc_{year}" / f"aoc_{year}_{day:02d}"

def get_aoc_input_path(year : int, day : int) -> str:
    return pathlib.Path() / "src" / "input" / f"aoc_{year}"

def fetch_input(path, file, url) -> str | None:
    session_cookie = "53616c7465645f5fde600dfcffa65a86fcb9c30fb7340728a958dc5183dc97e1bb50211a0e348e5c97f0a10a361f115974d239fc602c711123009af02ccd188d"
    input_data = ""

    pathlib.Path.mkdir(path, parents=True, exist_ok=True)
    cookies = {'session': session_cookie}

    try:
        response = requests.get(url, cookies=cookies)
        response.raise_for_status()
        input_data = response.text
        with open(file, "w") as f:
            f.write(input_data)

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        print("Double-check your SESSION_COOKIE, YEAR, and DAY values.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except OSError as e:
        print(    f"OS Error: {e}")

    return input_data

def permutations_iter(elements, length: int):
    for i in range(len(elements)):
        if length == 1:
                yield (elements[i],)
        else:
            for next in permutations_iter(elements, length -1):
                yield (elements[i], ) + next
    pass

def import_input(year : int, day : int) -> str | None:
    path =  get_aoc_input_path(year, day)
    file =  path / f"aoc_{year}_{day:02d}_input.txt"


    if not file.exists():
        url =  get_aoc_url(year, day) + "/input"
        input_data = fetch_input(path, file, url)

    else:
        try:
            with open(file, 'r') as f:
                input_data = f.read()
        except OSError as e:
            print(f"OS Error: {e}")

    return input_data