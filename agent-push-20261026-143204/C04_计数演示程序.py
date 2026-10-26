"""合成示例：只计算本地测试条目数量。"""

BATCH = 'agent-push-20261026-143204'

def count_demo_items():
    items = [{"key": f"DEMO-{i:03d}"} for i in range(1, 6)]
    return len(items)

if __name__ == "__main__":
    print(BATCH, count_demo_items())
