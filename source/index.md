# MTDataPro 中文手册

欢迎来到 **MTDataPro** —— 大地电磁（MT）数据处理软件。

MTDataPro 是地球科学领域广泛使用的专业 MT 数据处理软件之一。本手册由 MTDataPro 开发团队维护整理，详尽介绍了 MTDataPro 的用法并提供了大量实用示例，既可以作为初学者的入门读物，也可以作为日常使用的参考书。

---

## 手册学习指南

本手册主要包含如下三个部分：

1. **MTDataPro 入门**：介绍 MTDataPro 的功能特点、安装方法，并为初学者提供快速入门教程。初学者应完整阅读"入门"章节，并通过练习掌握 MTDataPro 的基本用法。

2. **MTDataPro 实例**：包含丰富的实用脚本和处理案例，可以作为日常数据处理参考。

3. **MTDataPro 进阶**：详细介绍各功能模块的使用方法和参数配置，可以作为参考书查阅。

---

## 快速链接

```{grid} 2 2 3 3
:gutter: 2

```{grid-item-card} 快速入门
:link: intro/quickstart
:link-type: doc

10 分钟完成第一次数据处理
```

```{grid-item-card} 安装指南
:link: intro/install
:link-type: doc

安装、配置与授权
```

```{grid-item-card} 处理流程
:link: chapters/chapter4
:link-type: doc

时间序列处理详解
```

```{grid-item-card} 仪器支持
:link: chapters/chapter3
:link-type: doc

Phoenix、Metronix、LEMI
```

```{grid-item-card} 数据导出
:link: chapters/chapter6
:link-type: doc

EDI、J-format 格式
```

```{grid-item-card} 常见问题
:link: appendices/appendixD
:link-type: doc

FAQ 与故障排除
```

```

---

## 快速开始

1. 安装软件并完成授权
2. 创建或打开工程
3. 导入仪器数据
4. 执行 FFT 处理
5. 数据筛选与阻抗估计
6. 导出 EDI 结果

---

## 文档下载

- [MTDataPro 中文手册源码](https://github.com/EMWPJ/MTDataPro-docs)
- [MTDataPro 中文手册 PDF](https://github.com/EMWPJ/MTDataPro-docs/releases)（即将提供）

---

## 外部链接

- [MTDataPro GitHub 仓库](https://github.com/EMWPJ/MTDataPro)
- [参与讨论](https://github.com/EMWPJ/MTDataPro-docs/discussions)

---

## 引用 MTDataPro

如果您在科研工作中使用了 MTDataPro，请引用：

```bibtex
@software{mtdp2026,
  title = {MTDataPro: A Professional Magnetotelluric Data Processing Software},
  author = {MTDataPro Development Team},
  year = {2026},
  version = {1.9.4},
  url = {https://github.com/EMWPJ/MTDataPro}
}
```

---

```{toctree}
:hidden:
:caption: MTDataPro 入门
:maxdepth: 2

intro/index
intro/install
intro/quickstart
tutorial/index
```

```{toctree}
:hidden:
:caption: MTDataPro 实例
:maxdepth: 2

gallery/index
```

```{toctree}
:hidden:
:caption: MTDataPro 进阶
:maxdepth: 2

chapters/chapter1
chapters/chapter2
chapters/chapter3
chapters/chapter4
chapters/chapter5
chapters/chapter6
chapters/chapter7
chapters/chapter8
chapters/chapter9
chapters/chapter10
```

```{toctree}
:hidden:
:caption: 附录

appendices/appendixA
appendices/appendixB
appendices/appendixC
appendices/appendixD
appendices/appendixE
appendices/appendixF
appendix/contributing
```

---

&copy; 版权所有 2026, MTDataPro 开发团队。最后更新于 {sub-ref}`today`。

利用 [Sphinx](https://www.sphinx-doc.org/) 构建，使用的 [sphinx_rtd_theme 主题](https://github.com/readthedocs/sphinx_rtd_theme) 由 [Read the Docs](https://readthedocs.org) 开发。
