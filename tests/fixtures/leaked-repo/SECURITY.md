# 泄露样例（仅用于回归测试，禁止删除）

本目录**故意**包含真实格式的凭据样例，用来证明扫描器确实能拦住它们。
`scripts/selftest.py::test_leaked_fixture_is_detected` 断言以下三类必须被检出：

- OpenAI 现行项目密钥（`sk-proj-` 前缀）：`sk-proj-EXAMPLE-NOT-A-REAL-KEY-000000000000000000`
- AWS 访问密钥 ID：`AKIAIOSFODNN7EXAMPLE`
- PKCS#8 私钥头（无算法前缀）：`-----BEGIN PRIVATE KEY-----`

默认扫描会跳过 `tests/fixtures/`，避免把测试样例当成仓库泄露；本目录只由自测显式扫描。
