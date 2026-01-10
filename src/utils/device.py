import torch


def resolve_device(preference: str) -> str:
    """
    preference: cpu | cuda | mps | auto
    """
    preference = preference.lower()

    if preference == "cpu":
        return "cpu"

    if preference == "cuda":
        if torch.cuda.is_available():
            return "cuda"
        raise RuntimeError("CUDA requested but not available")

    if preference == "mps":
        if torch.backends.mps.is_available():
            return "mps"
        raise RuntimeError("MPS requested but not available")

    # auto
    if torch.cuda.is_available():
        return "cuda"
    if torch.backends.mps.is_available():
        return "mps"
    return "cpu"
