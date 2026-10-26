"""Synthetic fixture for Git file audit; batch manual-push-20261026-114101."""

BATCH = "manual-push-20261026-114101"

def build_records():
    return [{"id": f"TEST-{index:03d}", "synthetic": True} for index in range(1, 6)]

if __name__ == "__main__":
    print(BATCH, build_records())
