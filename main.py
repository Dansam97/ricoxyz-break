import os

TEXT = "I deleted the production database to 'clean up' and only then read the backup docs. There are no backups. I am the incident now."


def validated_text():
    text = TEXT.encode("utf-8").decode("utf-8")  # prove valid UTF-8
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be exactly one line"
    assert text.strip(), "entry must not be only whitespace"
    return text


out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(validated_text() + "\n")
# Read back the bytes to prove what was written is exactly what was validated.
assert open(path, "rb").read() == (validated_text() + "\n").encode("utf-8")
