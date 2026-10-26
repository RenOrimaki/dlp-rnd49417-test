"""RND-49417 合成示例，仅用于文件推送测试。"""

BATCH = 'manual-push-20261026-142444'

def build_records():
    return [{"id": f"TEST-{i:03d}", "synthetic": True} for i in range(1, 6)]

if __name__ == "__main__":
    print(BATCH, build_records())
