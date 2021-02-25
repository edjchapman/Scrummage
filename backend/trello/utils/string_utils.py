import re


def get_est(text: str) -> str:
    """
    Extract estimate from text by matching numbers between brackets.
    """
    match = re.findall('\(*[.?0-9 ]+\)', text)
    if match:
        match = match[0]
        match = match.strip("( )")
    return match or ""
