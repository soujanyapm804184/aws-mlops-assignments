from flask import Flask, request, jsonify
import boto3

app = Flask(__name__)

BUCKET_NAME = "tiger-mle-pg"
BASE_PREFIX = "home/soujanya.puranmatt/"

s3 = boto3.client("s3", region_name="ap-south-1")


@app.route("/")
def home():
    return """
    <h1>S3 File Listing Application</h1>
    <p>Use the following URLs:</p>
    <ul>
        <li>/files?folder=A</li>
        <li>/files?folder=B</li>
        <li>/files?folder=C</li>
    </ul>
    """


@app.route("/files")
def list_files():

    folder = request.args.get("folder")

    if not folder:
        return (
            jsonify(
                {"error": "Please provide a folder name. Example: /files?folder=A"}
            ),
            400,
        )

    folder = folder.upper()

    if folder not in ["A", "B", "C"]:
        return jsonify({"error": "Invalid folder. Choose A, B, or C."}), 400

    prefix = f"{BASE_PREFIX}{folder}/"

    response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=prefix)

    files = []

    for obj in response.get("Contents", []):
        key = obj["Key"]

        if key != prefix:
            files.append(key.replace(prefix, ""))

    return jsonify({"folder": folder, "files": files})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8085, debug=True)
