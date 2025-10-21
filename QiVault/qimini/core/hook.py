def hook(meta):
    return {
        "id": meta["app"]["id"],
        "name": meta["app"]["name"],
        "entry": meta["app"]["entry"],
        "ver": meta["app"]["ver"],
        "out": meta["app"]["out"],
        "mode": meta["app"]["mode"],
    }
