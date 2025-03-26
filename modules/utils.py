from datetime import datetime

def log_to_markdown(text, file_path="cot-out.md", timestamp=False):
    with open(file_path, "a", encoding="utf-8") as f:
        if timestamp:
            time_str = datetime.now().strftime("Timestamp: %Y-%m-%d %H:%M:%S")
            f.write(f"\n---\n### {time_str}\n")
        f.write(text + "\n\n")
