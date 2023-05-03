import json


def generate_json_file():
    files = {
        "404": "404",
        "/": "index",
        #    "/1": "1",
        #    "/2": "2",
        #    "/3": "3",
    }
    result = {}
    for file in files:
        print("Generating " + file + "...")
        with open("www/" + files[file] + ".html", "r") as f:
            body = str(f.read()).replace("\n", "")
            result[file] = body

    print("Exporting All Pages...")

    with open("files.json", "w") as f:
        f.write(json.dumps(result))

    print("Done!")


if __name__ == "__main__":
    generate_json_file()
