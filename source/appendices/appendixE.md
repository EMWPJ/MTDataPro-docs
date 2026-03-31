# 附录E: 更新日志

## 版本 1.9.5 (当前版本)

**发布日期：** 2026年03月01日

**发布说明：** 功能优化，bug修复，aether兼容，MTU5兼容，部分重构（可能存在bug）

**主要功能：**

### 多仪器支持
- Phoenix MTU-5/5A TBL格式
- Phoenix MTU-5C/8A JSON格式
- Metronix ADU-06/ADU-07/MMS系列
- LEMI长周期仪器
- RMT/CASRMT格式
- Aether (ATTS) 格式
- EDI格式导入

### 数据处理
- FFT/DFT频谱计算
- 多锥谱分析（Multi-Taper）
- 系统响应标定
- 工频陷波滤波
- 高通/低通滤波
- 降采样处理（2x-4800x）

### 稳健估计
- Regression-M估计
- Repeated Median估计
- Bounded Influence估计
- Huber/Thomson预加权
- Robust+AI估计

### 参考道技术
- 远参考道处理
- 本地参考道
- 反向参考估计

### 智能筛选
- 多参数自动筛选
- 马氏距离筛选
- Rhoplus参考曲线
- 遗传算法筛选

### 导出功能
- EDI格式（标准/Spe/ZT/MTpy/PLT）
- KML/KMZ地理信息
- 时间序列导出（GMT/ATGMT格式）

---

## 版本 1.5

**主要功能：**
- Phoenix MTU-5/5A TBL格式支持
- Metronix、LEMI基本支持
- FFT计算
- 手动数据筛选
- Robust估计
- EDI导出

---

## 版本 1.0

**初始版本功能：**
- 基本工程管理
- Phoenix数据导入
- FFT处理
- 基本数据筛选
- EDI导出

---

## 已知问题

- 超大数据集（>10GB）时内存占用较高
- 某些显卡驱动可能与图表渲染冲突
- 极低频率（<0.001Hz）处理可能需要较长时间

---

## 系统要求

| 组件 | 要求 |
|-----|------|
| 操作系统 | Windows 10/11 64位 |
| 处理器 | Intel/AMD 64位处理器，4核心以上推荐 |
| 内存 | 8GB以上，16GB推荐 |
| 硬盘 | SSD推荐，至少10GB可用空间 |
| 显卡 | 支持OpenGL 3.0以上 |

---

## 技术支持

如需技术支持，请联系MTDP开发团队，提供：
- 软件版本号
- 问题描述
- 相关数据文件（如适用）
- 系统配置信息
