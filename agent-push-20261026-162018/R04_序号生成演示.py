"""合成测试示例，仅生成本地序号列表。"""

BATCH = 'agent-push-20261026-162018'

def build_sample_ids():
    return [f"SAMPLE-{i:03d}" for i in range(1, 6)]

if __name__ == "__main__":
    print(BATCH, build_sample_ids())
