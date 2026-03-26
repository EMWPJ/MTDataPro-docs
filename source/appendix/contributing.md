# 贡献指南

感谢您对 MTDataPro 文档的关注与支持！

## 如何贡献

1. **发现问题**：浏览 [Issue 列表](https://github.com/EMWPJ/MTDataPro-docs/issues) 或报告新问题
2. **Fork 仓库**：创建您自己的副本
3. **进行修改**：编辑 Markdown 源文件
4. **本地预览**：构建文档验证修改
5. **提交 Pull Request**：您的修改将被审核并合并

## 文档结构

```
docs/
├── source/
│   ├── conf.py           # Sphinx 配置
│   ├── index.md          # 主页面
│   ├── chapters/         # 章节文件 (chapter1-10)
│   ├── appendices/       # 附录文件 (appendixA-F)
│   ├── intro/            # 入门指南
│   ├── tutorial/         # 进阶教程
│   └── gallery/          # 实例展示
└── requirements.txt      # Python 依赖
```

## 本地构建

```bash
# 安装依赖
pip install -r requirements.txt

# 构建 HTML 文档
sphinx-build -b html source _build/html

# 预览文档
open _build/html/index.html
```

## 写作规范

- 使用清晰、简洁的语言
- 适当包含代码示例
- 用户面向的内容使用中文编写
- 保持标题结构的一致性
- 公式使用 LaTeX 格式
- Mermaid 图表用于流程说明

## 注意事项

- 提交前请确保文档可以正常构建
- 确保所有链接都有效
- 图片请使用相对路径引用
- 代码块请指定正确的语言以获得语法高亮
