# 附录C: 文件格式规范

## 工程文件结构

MTDP工程使用加密格式存储，扩展名为 `.MTDPE`。

### 工程目录结构

```
ProjectName/
├── ProjectName.MTDPE        # 工程主文件（加密）
├── Configurations/          # 配置文件
│   ├── MTDP.SETTING        # 软件设置
│   ├── ProjectInfos.XML    # 工程信息列表
│   └── Lang/               # 语言文件
├── CLB/                     # 电场盒标定
├── CLC/                     # 磁传感器标定
└── temp/                    # 临时文件
```

---

## EDI文件格式

EDI（Electrical Data Interchange）是MT数据的标准交换格式。

### EDI文件结构示例

```
>HEAD
  SITE NAME="MT001"
  LATITUDE=40:07:24.2 N
  LONGITUDE=116:34:04.1 E
  ELEVATION=150.5
>END

>FREQ UNITS=HZ
  0.001 0.002 0.005 0.01 0.02 0.05 0.1 0.2 0.5 1.0 2.0 5.0 10.0
>END

>ZXX UNITS=MV/KM/NT
  // |Zxx|, arg(Zxx), |Zxx|_err, arg(Zxx)_err
  0.00123, 45.2, 0.00012, 2.5
  0.00234, 43.8, 0.00023, 3.1
  ...
>END

>ZXY UNITS=MV/KM/NT
  // |Zxy|, arg(Zxy), |Zxy|_err, arg(Zxy)_err
  ...
>END
```

---

## 各仪器原始数据格式摘要

### Phoenix TBL格式

```
SITE_NAME: MT001
LATITUDE: 40.1234
LONGITUDE: 116.5678
ELEVATION: 150.5
SAMPLING_RATE: 256
NUM_CHANNELS: 5
START_TIME: 2024-01-15 08:00:00
END_TIME: 2024-01-16 08:00:00
```

### Phoenix JSON格式

```json
{
  "site": {
    "name": "MT001",
    "coordinates": {
      "latitude": 40.1234,
      "longitude": 116.5678,
      "elevation": 150.5
    }
  },
  "acquisition": {
    "sampling_rate": 256,
    "start_time": "2024-01-15T08:00:00Z",
    "duration_hours": 24
  }
}
```

### Metronix ATM格式

ATM文件为二进制格式，包含：
- 文件头：标识信息、版本号
- 通道配置：通道数、采样率
- 数据块：时间戳、采样数据

### LEMI格式

- 二进制时间序列
- 文本头文件
- 支持多种采样率

### ATTS格式

- 自定义二进制格式
- 高精度时间戳
- 多通道同步采集

---

## 标定文件格式

### CLB文件（电场盒标定）

记录电场采集盒的频率响应：
- 频率点
- 幅度响应
- 相位响应

### CLC文件（磁传感器标定）

记录磁传感器的频率响应：
- 传感器序列号
- 频率点
- 复数响应值

---

## 处理方案文件

处理方案可导出为XML或JSON格式，包含：
- 窗函数设置
- FFT参数
- 频率表
- 估计方法配置
- 自动筛选参数
