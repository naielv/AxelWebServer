import json
import sys

def generate_json_file(ver):
    files = {
        "404": "404",
        "/": "index",
        #    "/1": "1",
        #    "/2": "2",
        #    "/3": "3",
    }
    result = {"_version": ver}
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
    if "Rev." in sys.argv[-1]:
        ver = sys.argv[-1]
    else:
        ver = "N/A"
    generate_json_file(ver)
    if ver == "N/A":
        print('Hint: Run with "Rev. ___" to set the "_version" file')