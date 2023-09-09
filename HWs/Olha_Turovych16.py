import html
import requests


def decorator(get_request):
    def wrapped(*args, **kwargs):
        r = requests.get(*args, **kwargs)
        html_content = r.text
        with open("eighth_lesson/Olha_Turovych.html", "w") as f:
            f.write(html_content)
        return get_request(*args, **kwargs)

    return wrapped


url = "https://e-pandora.ua/product/792015c00_e043"


@decorator
def get_request(url):
    r = requests.get(url)
    html_content = r.text
    print(html_content)


def main():
    get_request(url)


if __name__ == "__main__":
    main()
