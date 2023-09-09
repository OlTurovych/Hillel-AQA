import requests


def log(filename):
    def decorator(get_request):
        def wrapped(*args, **kwargs):
            r = get_request(*args, **kwargs)
            html_content = r.text
            with open(filename, "w") as f:
                f.write(html_content)
            return r

        return wrapped

    return decorator


@log("file_test.html")
def get_request(url):
    r = requests.get(url)
    return r


def main():
    url = "https://e-pandora.ua/product/792015c00_e043"
    response = get_request(url)
    html_content = response.text
    print(html_content)


if __name__ == "__main__":
    main()
