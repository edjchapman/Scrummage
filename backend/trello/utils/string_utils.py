import re


def get_est(text, bracket_style="()"):
    """
    Extract estimate from text by matching numbers between brackets.
    """
    est = None
    pattern = "\\[[0-9.]*\\]" if bracket_style == "[]" else "\\([0-9.]*\\)"
    try:
        match = re.findall(pattern, text)
        if match:
            est = match[0]
            est = est.strip(bracket_style)
            est = float(est)
    except Exception:
        est = None
    return est
