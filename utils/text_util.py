def escape_for_markdown(text: str):
    return text.replace("&", "&amp;") \
        .replace("<", "&lt;") \
        .replace(">", "&gt;") \
        .replace('"', "&quot;") \
        .replace("'", "&apos;")

