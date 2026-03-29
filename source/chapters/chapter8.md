# 工具集

本章介绍MTDP提供的各种实用工具。

---

## 🛠️ 工具菜单完整列表

MTDataPro提供丰富的工具菜单，支持时间序列处理、格式转换、数据修复等功能。

### 标定与查看工具

| 菜单项 | 功能说明 |
|-------|---------|
| 标定查看 (CalViewMenu) | 查看和校准仪器标定数据 |
| TS查看 (TSViewMenu) | 时间序列数据查看器 |

### Phoenix时间序列工具

| 菜单项 | 功能说明 |
|-------|---------|
| Phoenix TS分割 (SplitPhoenixTSMenu) | 分割Phoenix格式时间序列 |
| Phoenix TS修复 (PhoneixTSRepairMenu) | 修复损坏的Phoenix TS文件 |
| Phoenix TS合并 (MergePhoneixTSMenu) | 合并多个Phoenix TS文件 |
| Phoenix通道重排 (PhoenixChannelRearrenageMenu) | 重新排列Phoenix通道顺序 |
| TBL坐标修复 (TBLCoorFixMenu) | 修复TBL格式坐标数据 |
| TBL参数替换 (TBLParameterReplaceMenu) | 批量替换TBL参数 |

### 时间序列转换工具 (TSConvertMenu)

| 子菜单项 | 功能说明 |
|---------|---------|
| TXT→TSN (PhoneixTxt2TSNMenu) | Phoenix文本格式转换为TSN |
| TSN→DAT (PhoenixTSN2DatMenu) | TSN格式转换为DAT |
| DAT→TSN (PhoenixDat2TSNMenu) | DAT格式转换为TSN |
| TSN→GMT (PhoneixTSN2GMTMenu) | TSN格式转换为GMT |
| 时间序列→GMT (TimeSeries2GMTMenu) | 通用时间序列转GMT |
| 时间序列→ATGMT (TimeSeries2ATGMTMenu) | 时间序列转ATGMT格式 |

### LEMI工具

| 菜单项 | 功能说明 |
|-------|---------|
| LEMI测点合并 (LEMISiteMergeMenu) | 合并LEMI格式测点数据 |
| LEMI H自动恢复 (LEMISiteHAutoRestoreMenu) | 自动恢复LEMI H通道数据 |

### Metronix工具

| 菜单项 | 功能说明 |
|-------|---------|
| Metronix测点合并 (MetronixSiteMergeMen) | 合并Metronix格式测点数据 |
| Metronix ATS→DAT (MetronixAtsToDatMenu) | Metronix ATS格式转换为DAT |

### WEM数据处理

| 菜单项 | 功能说明 |
|-------|---------|
| WEM数据处理 (WEMDataProcessMenu) | WEM格式数据处理工具 |

### EDI处理工具

| 菜单项 | 功能说明 |
|-------|---------|
| EDI修复 (EDIRepairMenu) | 修复损坏的EDI文件 |
| EDI转换相干度 (EDIConvertCOHMenu) | 转换EDI相干度数据 |
| 旧版MT→EDI (OldMT2EdiMenu) | 旧版MT格式转换为EDI |

### Phoenix格式转换工具 (PhoenixConvertMenu)

| 子菜单项 | 功能说明 |
|---------|---------|
| CLB→JSON (CLB2JSONMenu) | CLB标定文件转JSON |
| CLC→JSON (CLC2JSONMenu) | CLC标定文件转JSON |
| JSON→CLB (JSON2CLBMenu) | JSON转CLB标定文件 |
| JSON→CLC (JSON2CLCMenu) | JSON转CLC标定文件 |
| TBL→JSON (TBL2JSONMenu) | TBL参数文件转JSON |
| JSON→TBL (JSON2TBLMenu) | JSON转TBL参数文件 |

---

## 💡 使用建议

### 工具选择建议

- 根据数据格式选择合适的转换工具
- 批量处理时建议先备份原始数据
- 定期清理临时文件以节省磁盘空间

### 常见问题处理

| 问题 | 解决方案 |
|-----|---------|
| 转换失败 | 检查原始文件格式是否正确 |
| 路径不存在 | 确认标定文件搜索路径设置正确 |
| 数据丢失 | 使用备份文件重新处理 |
