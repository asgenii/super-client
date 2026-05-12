import requests, zipfile, json, shutil

def run(args):
    if args[0] == "download":
        r = requests.get(f"http://158.220.126.85:8000/download/{args[0]}")

        with open(f"temp/{args[0]}.zip", "wb") as f:
            f.write(r.content)

        with open(f"temp/{args[0]}.zip", "rb") as f:
            with zipfile.ZipFile(f) as zip_ref:
                zip_ref.extractall(f"temp/{args[0]}")

        with open(f"temp/{args[0]}/{args[0]}/metadata.json", "r") as f:
            metadata = json.load(f)

        if metadata["package"]["type"] == "command":
            shutil.move(f"temp/{args[0]}/{args[0]}", f"commands/user/{args[0]}")

        return None