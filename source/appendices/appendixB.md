# 附录B: 参数说明表

## 处理方案参数

| 参数名 | 类型 | 默认值 | 说明 |
|-------|------|-------|------|
| Window | Integer | 2 | 窗函数类型（0=矩形,1=汉明,2=汉宁） |
| FFTDFT | Boolean | False | FFT/DFT选择 |
| SingleFrequencyCalculationWay | Integer | 0 | 单频计算方式 |
| ZeroPadding | Double | 0 | 零填充因子 |
| MultiTaper | Integer | 0 | 多锥谱分析锥数 |
| SearchBand | Double | 0.1 | 搜索带宽 |
| ReferenceEstimator | Integer | 0 | 参考道估计方法 |
| RobustEstimator | Integer | 1 | 稳健估计方法 |

---

## FFT参数

| 参数名 | 类型 | 默认值 | 说明 |
|-------|------|-------|------|
| SampleLength | Double | 4096 | 样本长度（FFT长度） |
| Overlap | Double | 0.5 | 重叠率（0-0.75） |
| MaxXPR | Integer | 100 | 最大XPR值 |
| GroupingType | Integer | 0 | 分组类型 |

---

## 稳健估计参数

| 参数名 | 类型 | 默认值 | 说明 |
|-------|------|-------|------|
| maxiters | Integer | 100 | 最大迭代次数 |
| eps | Double | 0.01 | 迭代步长容差 |
| epslast | Double | 0.0001 | 最终收敛容差 |
| r0 | Double | 1.5 | 调谐参数（λ） |
| ainuin | Double | 0.9999 | 有界影响上界 |
| ainlin | Double | 0.0001 | 有界影响下界 |

---

## 参考道估计方法

| 值 | 方法 | 代码 |
|---|------|-----|
| 0 | Local E | LE |
| 1 | Local H | LH |
| 2 | Local E/H | LEH |
| 3 | Remote E | RE |
| 4 | Remote H | RH |
| 5 | Remote E/H | REH |
| 6 | Remote E/Local H | RELH |

---

## 稳健估计方法

| 值 | 方法 | 说明 |
|---|------|------|
| 0 | LeastSquares | 标准最小二乘法 |
| 1 | Regression-M | M估计回归法 |
| 2 | Repeated Median | 重复中位数法（高抗噪性） |
| 3 | Bounded Influence | 有界影响估计 |
| 4 | Huber Pre-Weighted | Huber预加权估计 |
| 5 | Thomson Pre-Weighted | Thomson预加权估计 |
| 6 | Robust+AI | 稳健估计结合AI预测 |

---

## 自动筛选参数

| 参数名 | 类型 | 默认值 | 说明 |
|-------|------|-------|------|
| MaxProportion | Double | 0.9 | 最大保留比例 |
| MinProportion | Double | 0.1 | 最小保留比例 |
| ExitError | Double | 0.01 | 退出误差阈值 |
| AutoPrecent | Double | 0.5 | 自动选择百分比 |

---

## 马氏距离参数

| 参数名 | 类型 | 默认值 | 说明 |
|-------|------|-------|------|
| RobustC | Double | 4.0 | Huber权函数阈值 |
| MaxIterations | Integer | 5 | 最大迭代次数 |

---

## 遗传算法参数

| 参数名 | 类型 | 默认值 | 说明 |
|-------|------|-------|------|
| PopulationSize | Integer | 100 | 种群大小 |
| Generations | Integer | 200 | 最大进化代数 |
| CrossoverRate | Double | 0.8 | 交叉概率 |
| MutationRate | Double | 0.1 | 变异概率 |

---

## 降采样参数

| 参数名 | 类型 | 可选值 | 说明 |
|-------|------|-------|------|
| Factor | Enum | 2x-4800x | 降采样因子 |
| FilterType | Enum | FIR/CIC | 抗混叠滤波器类型 |
| BoundaryMethod | Enum | Zero/Mirror/Constant | 边界处理方法 |
| PowerLineFilter | Boolean | True/False | 是否启用工频滤波 |
| PowerLineFreq | Integer | 50/60 | 工频频率 |
| PowerLineHarmonics | Integer | 1-9 | 谐波数量 |

---

## 工频滤波参数

| 参数名 | 类型 | 默认值 | 说明 |
|-------|------|-------|------|
| SampleRate | Double | -- | 采样率（Hz） |
| BaseFreq | Integer | 50 | 基频（50或60Hz） |
| HarmonicCount | Integer | 9 | 谐波数量（含基频） |

---

## Rhoplus参数

| 参数名 | 类型 | 默认值 | 说明 |
|-------|------|-------|------|
| DefaultLayerCount | Integer | 20 | 默认层数 |
| nfre | LongInt | -- | 频率点数 |
| lcount | Integer | 20 | 输出层数 |

---

## AI预测参数

| 方法 | 说明 | 适用场景 |
|-----|------|---------|
| ModelPredict | ZPredict深度学习 | 一般数据预测 |
| ModelPredict1 | 中值滤波（窗口3） | 简单平滑 |
| ModelPredict2 | 迭代优化（最多100次） | 精细预测 |

---

## 测点排序方式

| 值 | 排序方式 | 说明 |
|---|---------|------|
| 0 | 按纬度 | 从南到北 |
| 1 | 按经度 | 从西到东 |
| 2 | 按名称 | 字母顺序 |
| 3 | 按开始时间 | 时间先后 |
| 4 | 按结束时间 | 时间先后 |

---

## 仪器类型代码

| 代码 | 类型 | 文件特征 |
|-----|------|---------|
| 0 | Phoenix Site | .tbl |
| 1 | LEMI Site | .lemi |
| 2 | Metronix Site | .mxsite |
| 3 | SBF Site | .sbf |
| 4 | CASRMT Site | .rmtjson, .json |
| 5 | MTU Site | recmeta.json |
| 6 | RMT Site | .tr1, .tr2, .tr3 |
| 7 | ATTS Site | .atts, .atinfo |
| 8 | AGEXXL Site | .dat |
| -1 | Synthetic Site | .timeseries |
| 100+ | Source Site | 源站点 |
| 200+ | Multiple Site | 多文件合并站点 |

---

## 数据质量等级

| 等级 | 说明 | 建议处理 |
|-----|------|---------|
| 0 | 未评估 | 需要评估 |
| 1 | 优秀 | 可直接使用 |
| 2 | 良好 | 轻度筛选 |
| 3 | 一般 | 需要筛选 |
| 4 | 较差 | 建议重采或舍弃 |

---

## MT参数类型

| 参数 | 说明 |
|-----|------|
| MT_fre | 频率 |
| MT_Zxxr/Zxxi | Zxx实部/虚部 |
| MT_Zxyr/Zxyi | Zxy实部/虚部 |
| MT_Zyxr/Zyxi | Zyx实部/虚部 |
| MT_Zyyr/Zyyi | Zyy实部/虚部 |
| MT_Tzxr/Tzxi | Tzx实部/虚部 |
| MT_Tzyr/Tzyi | Tzy实部/虚部 |
| MT_Rxx/Rxy/Ryx/Ryy | 视电阻率 |
| MT_Pxx/Pxy/Pyx/Pyy | 相位 |
| MT_Coh* | 相干度 |
| MT_SNR* | 信噪比 |
| MT_alpha/beta | 相位张量参数 |
| MT_PtMax/PtMin | 相位张量最大/最小值 |
| MT_Skew1D/Skew2D | 相位张量偏斜度 |
