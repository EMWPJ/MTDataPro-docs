# MTDataPro 数据导出与 Python 绘图教程

本章节介绍如何使用 MTDataPro 导出的数据配合 Python 脚本进行高质量科学绘图。

## 数据导出

在使用绘图脚本之前，需要先从 MTDataPro 导出绘图所需的数据文件。

### 导出步骤

1. 在工程树中选择测点（Site），或批量选择多个测点
2. 使用测点的导出功能（具体菜单路径请参考 `chapter4-测量数据导出`）
3. 选择导出内容：
   - 视电阻率数据（ρxy, ρyx）
   - 相位数据（φxy, φyx）
   - 误差数据
   - 倾子数据（Tx, Ty）
   - 相位张量参数（α, β, φmax, φmin）

### 导出文件命名规则

导出的数据文件遵循统一的命名规则 `{测点名}-{参数名}.dat`：

| 文件名 | 内容 | 说明 |
|:------|:-----|:-----|
| `{name}-rxy.dat` | 视电阻率 ρxy | 第1列：频率，第2列：数值 |
| `{name}-ryx.dat` | 视电阻率 ρyx | 第1列：频率，第2列：数值 |
| `{name}-zxyp.dat` | 相位 φxy | 第1列：频率，第2列：数值（度） |
| `{name}-zyxp.dat` | 相位 φyx | 第1列：频率，第2列：数值（度） |
| `{name}-rxyvar.dat` | ρxy 方差 | 误差数据 |
| `{name}-ryxvar.dat` | ρyx 方差 | 误差数据 |
| `{name}-tzxr.dat` | 倾子 Tx 实部 | 复数形式 |
| `{name}-tzxi.dat` | 倾子 Tx 虚部 | 复数形式 |
| `{name}-tzyr.dat` | 倾子 Ty 实部 | 复数形式 |
| `{name}-tzyi.dat` | 倾子 Ty 虚部 | 复数形式 |
| `{name}-alpha.dat` | 相位张量 α | 旋转角度 |
| `{name}-beta.dat` | 相位张量 β | 偏离角度 |
| `{name}-pmin.dat` | 相位张量 φmin | 最小主轴 |
| `{name}-pmax.dat` | 相位张量 φmax | 最大主轴 |

---

## Python 绘图环境配置

### 依赖库

```bash
pip install numpy matplotlib pdf2image PyPDF2 shapely pyproj
```

### matplotlib 学术绘图配置

建议在脚本开头添加以下配置以符合学术规范：

```python
import matplotlib.pyplot as plt
import numpy as np

# 设置 matplotlib 字体样式以符合学术规范
plt.rcParams.update({
    'font.size': 12,
    'font.family': 'serif',
    'font.serif': 'Times New Roman',
    'axes.titlesize': 18,   # 标题字体大小
    'axes.labelsize': 15,    # 轴标签字体大小
    'xtick.labelsize': 12,  # x轴刻度标签字体大小
    'ytick.labelsize': 12,   # y轴刻度标签字体大小
    'legend.fontsize': 12    # 图例字体大小
})
```

---

## 单测点视电阻率/相位曲线

绘制单个测点的视电阻率和相位曲线，支持误差棒显示。

### 脚本：PlotFullZ-Single.py

```python
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# ===== 配置参数 =====
path = r'E:\MTData\Project\SiteData'  # 数据文件夹路径
ymax = 1e4   # 视电阻率 y 轴最大值
ymin = 1e0   # 视电阻率 y 轴最小值
xmax = 1e3   # 频率 x 轴最大值
xmin = 1e-5  # 频率 x 轴最小值

# 获取所有测点文件夹
names = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]

for name in names:
    print(f'Processing: {name}')
    
    # 读取数据
    fre = np.loadtxt(f'{path}\\{name}\\{name}-rxx.dat')[:, 0]
    rxy = np.loadtxt(f'{path}\\{name}\\{name}-rxy.dat')[:, 1]
    ryx = np.loadtxt(f'{path}\\{name}\\{name}-ryx.dat')[:, 1]
    pxy = np.loadtxt(f'{path}\\{name}\\{name}-zxyp.dat')[:, 1]
    pyx = np.loadtxt(f'{path}\\{name}\\{name}-zyxp.dat')[:, 1]
    
    # 读取误差数据
    rxy_var = np.loadtxt(f'{path}\\{name}\\{name}-rxyvar.dat')[:, 1]
    ryx_var = np.loadtxt(f'{path}\\{name}\\{name}-ryxvar.dat')[:, 1]
    pxy_var = np.loadtxt(f'{path}\\{name}\\{name}-pxyvar.dat')[:, 1]
    pyx_var = np.loadtxt(f'{path}\\{name}\\{name}-pyxvar.dat')[:, 1]
    
    # 创建图形和子图
    fig, axs = plt.subplots(2, 1, figsize=(8, 7), sharex='all', constrained_layout=True)
    
    # 视电阻率子图
    ax = axs[0]
    ax2 = ax.twinx()
    
    # 误差转换到对数坐标
    log_rxy = np.log10(rxy)
    log_ryx = np.log10(ryx)
    log_rxy_var = rxy_var / (rxy * np.log(10))
    log_ryx_var = ryx_var / (ryx * np.log(10))
    
    ax2.errorbar(fre, log_rxy, yerr=log_rxy_var, fmt='ro', label='XY', markerfacecolor='none')
    ax2.errorbar(fre, log_ryx, yerr=log_ryx_var, fmt='bs', label='YX', markerfacecolor='none')
    ax2.set_ylim(np.log10(ymin), np.log10(ymax))
    ax2.invert_xaxis()
    ax2.legend(loc='upper right', bbox_to_anchor=(1.2, 0.8))
    
    ax.set_ylim(ymin, ymax)
    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.set_xlim(xmin, xmax)
    ax.invert_xaxis()
    ax.grid(True, which='major', linestyle='--', linewidth=0.5)
    ax.set_ylabel(r'$\rho\;(\Omega \cdot m)$')
    
    # 相位子图
    ax = axs[1]
    ax.errorbar(fre, pxy, yerr=pxy_var, fmt='ro', label='XY', markerfacecolor='none')
    ax.errorbar(fre, pyx, yerr=pyx_var, fmt='bs', label='YX', markerfacecolor='none')
    ax.set_ylim(-180, 180)
    ax.set_yticks(np.arange(-180, 181, 90))
    ax.set_xscale('log')
    ax.set_xlabel('Frequency (Hz)')
    ax.set_ylabel(r'$\varphi\;(\degree)$')
    ax.grid(True, which='major', linestyle='--', linewidth=0.5)
    
    # 保存图形
    plt.savefig(f'{path}\\{name}_Site.png', dpi=300, bbox_inches='tight')
    plt.savefig(f'{path}\\{name}_Site.pdf', format='pdf', dpi=300, bbox_inches='tight')
    plt.close()

print('Finished!')
```

### 输出效果

生成的图像包含两个子图：
- 上图：视电阻率 ρxy（红色）和 ρyx（蓝色）随频率变化
- 下图：对应的相位 φxy 和 φyx

---

## 多测点联合对比图

将多个测点的曲线绘制在同一张图中，便于对比分析。

### 脚本：PlotFullZ-All.py

```python
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# ===== 配置参数 =====
path = r'F:\ZhangYeAMT\MTDPProject\ZhangYe\0901'
nrows = 8   # 网格行数（每个测点占2行：电阻率+相位）
ncols = 5    # 网格列数
ymax = 1e4
ymin = 1e-1
xmax = 1e3
xmin = 1e-4

# 获取所有测点文件夹
names = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]

# 创建大图形
fig, axs = plt.subplots(nrows=nrows*2, ncols=ncols, figsize=(25, 40), sharex='all', constrained_layout=True)

for i, name in enumerate(names):
    print(f'\rProcessing {name}', end='')
    
    # 读取数据
    fre = np.loadtxt(f'{path}\\{name}\\{name}-rxx.dat')[:, 0]
    rxy = np.loadtxt(f'{path}\\{name}\\{name}-rxy.dat')[:, 1]
    ryx = np.loadtxt(f'{path}\\{name}\\{name}-ryx.dat')[:, 1]
    pxy = np.loadtxt(f'{path}\\{name}\\{name}-zxyp.dat')[:, 1]
    pyx = np.loadtxt(f'{path}\\{name}\\{name}-zyxp.dat')[:, 1]
    
    # 计算子图位置
    row = (i // ncols) * 2
    col = i % ncols
    
    # 视电阻率子图
    ax = axs[row, col]
    ax2 = ax.twinx()
    
    log_rxy = np.log10(rxy)
    log_ryx = np.log10(ryx)
    log_rxy_var = rxy_var / (rxy * np.log(10))
    log_ryx_var = ryx_var / (ryx * np.log(10))
    
    ax2.errorbar(fre, log_rxy, yerr=log_rxy_var, fmt='ro', label='XY', markerfacecolor='none')
    ax2.errorbar(fre, log_ryx, yerr=log_ryx_var, fmt='bs', label='YX', markerfacecolor='none')
    ax2.set_ylim(np.log10(ymin), np.log10(ymax))
    ax2.invert_xaxis()
    ax2.set_yticklabels([])
    
    ax.set_ylim(ymin, ymax)
    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.set_xlim(xmin, xmax)
    ax.invert_xaxis()
    ax.grid(True, which='major', linestyle='--', linewidth=0.5)
    ax.text(0.5, 0.88, name, ha='center', va='bottom', transform=ax.transAxes, 
            fontsize=12, fontweight='bold')
    
    if col == 0:
        ax.set_ylabel(r'$\rho\;(\Omega \cdot m)$', fontsize=8)
    
    # 相位子图
    ax = axs[row + 1, col]
    ax.errorbar(fre, pxy, fmt='ro', label='XY', markerfacecolor='none')
    ax.errorbar(fre, pyx, fmt='bs', label='YX', markerfacecolor='none')
    ax.set_ylim(-180, 180)
    ax.set_yticks(np.arange(-180, 181, 90))
    ax.set_xscale('log')
    ax.grid(True, which='major', linestyle='--', linewidth=0.5)
    
    if row + 1 == nrows * 2 - 1:
        ax.set_xlabel('Frequency (Hz)', fontsize=8)
    if col == 0:
        ax.set_ylabel(r'$\varphi\;(\degree)$', fontsize=8)

fig.subplots_adjust(hspace=0.4, wspace=0.4)
plt.savefig(f'{path}\\All_Sites.png', dpi=300, bbox_inches='tight')
plt.savefig(f'{path}\\All_Sites.pdf', dpi=300, bbox_inches='tight')
plt.savefig(f'{path}\\All_Sites.svg', dpi=300, bbox_inches='tight')

print('\nFinished!')
```

---

## 测点对比分析

比较两个测点或两组数据的差异，计算 RMS 误差。

### 脚本：PlotFullZ-Compare.py

```python
import os
import numpy as np
import matplotlib.pyplot as plt

def plotMTDP(path, name1, name2):
    """绘制两个测点的对比图"""
    
    # 配置参数
    ymax = 1e3
    ymin = 1e0
    xmax = 1e3
    xmin = 5e-4
    
    # 创建输出目录
    out_dir = os.path.join(path, 'Compare')
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    
    # 读取测点1数据
    fre1 = np.loadtxt(f'{path}\\{name1}\\{name1}-rxy.dat')[:, 0]
    rxy1 = np.loadtxt(f'{path}\\{name1}\\{name1}-rxy.dat')[:, 1]
    ryx1 = np.loadtxt(f'{path}\\{name1}\\{name1}-ryx.dat')[:, 1]
    pxy1 = np.loadtxt(f'{path}\\{name1}\\{name1}-zxyp.dat')[:, 1]
    pyx1 = np.loadtxt(f'{path}\\{name1}\\{name1}-zyxp.dat')[:, 1]
    
    # 读取测点2数据
    fre2 = np.loadtxt(f'{path}\\{name2}\\{name2}-rxy.dat')[:, 0]
    rxy2 = np.loadtxt(f'{path}\\{name2}\\{name2}-rxy.dat')[:, 1]
    ryx2 = np.loadtxt(f'{path}\\{name2}\\{name2}-ryx.dat')[:, 1]
    pxy2 = np.loadtxt(f'{path}\\{name2}\\{name2}-zxyp.dat')[:, 1]
    pyx2 = np.loadtxt(f'{path}\\{name2}\\{name2}-zyxp.dat')[:, 1]
    
    # 计算 RMS 误差
    endindex = 39
    rxyerror = (rxy1[0:endindex] - rxy2[0:endindex]) / rxy1[0:endindex]
    rxyrms = np.sqrt(np.mean(rxyerror**2) / 2)
    
    ryxerror = (ryx1[0:endindex] - ryx2[0:endindex]) / ryx1[0:endindex]
    ryxrms = np.sqrt(np.mean(ryxerror**2) / 2)
    
    pxyerror = (pxy1[0:endindex] - pxy2[0:endindex]) / pxy1[0:endindex]
    pxyrms = np.sqrt(np.mean(pxyerror**2) / 2)
    
    pyxerror = (pyx1[0:endindex] - pyx2[0:endindex]) / pyx1[0:endindex]
    pyxrms = np.sqrt(np.mean(pyxerror**2) / 2)
    
    print(f'RMS Error Rxy: {rxyrms*100:.1f}%, Ryx: {ryxrms*100:.1f}%')
    print(f'RMS Error Pxy: {pxyrms*100:.1f}%, Pyx: {pyxrms*100:.1f}%')
    
    # 创建 2x2 子图
    fig, axs = plt.subplots(2, 2, figsize=(10, 6), sharex='all', constrained_layout=True)
    
    # ρxy
    axs[0,0].loglog(fre1, rxy1, 'r', label=name1)
    axs[0,0].loglog(fre2, rxy2, 'b', label=name2)
    axs[0,0].set_ylim(ymin, ymax)
    axs[0,0].set_xlim(xmin, xmax)
    axs[0,0].invert_xaxis()
    axs[0,0].set_ylabel(r'$\rho\;(\Omega \cdot m)$')
    axs[0,0].set_title(r'$\rho_{xy}$ RMS = ' + f'{rxyrms*100:.1f}%')
    axs[0,0].grid(True, which='major', linestyle='--', linewidth=0.5)
    axs[0,0].legend()
    
    # ρyx
    axs[0,1].loglog(fre1, ryx1, 'r', label=name1)
    axs[0,1].loglog(fre2, ryx2, 'b', label=name2)
    axs[0,1].set_ylim(ymin, ymax)
    axs[0,1].set_xlim(xmin, xmax)
    axs[0,1].invert_xaxis()
    axs[0,1].set_title(r'$\rho_{yx}$ RMS = ' + f'{ryxrms*100:.1f}%')
    axs[0,1].grid(True, which='major', linestyle='--', linewidth=0.5)
    axs[0,1].legend()
    
    # φxy
    axs[1,0].semilogx(fre1, pxy1, 'r', label=name1)
    axs[1,0].semilogx(fre2, pxy2, 'b', label=name2)
    axs[1,0].set_ylim(-180, 180)
    axs[1,0].set_yticks(np.arange(-180, 181, 90))
    axs[1,0].set_xlim(xmin, xmax)
    axs[1,0].invert_xaxis()
    axs[1,0].set_xlabel('Frequency (Hz)')
    axs[1,0].set_ylabel(r'$\varphi\;(\degree)$')
    axs[1,0].set_title(r'$\varphi_{xy}$ RMS = ' + f'{pxyrms*100:.1f}%')
    axs[1,0].grid(True, which='major', linestyle='--', linewidth=0.5)
    axs[1,0].legend()
    
    # φyx
    axs[1,1].semilogx(fre1, pyx1, 'r', label=name1)
    axs[1,1].semilogx(fre2, pyx2, 'b', label=name2)
    axs[1,1].set_ylim(-180, 180)
    axs[1,1].set_yticks(np.arange(-180, 181, 90))
    axs[1,1].set_xlim(xmin, xmax)
    axs[1,1].invert_xaxis()
    axs[1,1].set_xlabel('Frequency (Hz)')
    axs[1,1].set_title(r'$\varphi_{yx}$ RMS = ' + f'{pyxrms*100:.1f}%')
    axs[1,1].grid(True, which='major', linestyle='--', linewidth=0.5)
    axs[1,1].legend()
    
    # 保存
    fig.savefig(os.path.join(out_dir, f'{name1}-{name2}.png'), dpi=300, bbox_inches='tight')
    fig.savefig(os.path.join(out_dir, f'{name1}-{name2}.pdf'), dpi=300, bbox_inches='tight')
    fig.savefig(os.path.join(out_dir, f'{name1}-{name2}.svg'), dpi=300, bbox_inches='tight')
    plt.close()


# ===== 使用示例 =====
path = r'D:\DataProcess\JianghanPlain\MTDPProject\Consistency'
comparison_pairs = [
    ['JHMT41SA', 'JHMT41SB'],
    ['JHMT45SA', 'JHMT45SB'],
    ['JHMT46SA', 'JHMT46SJ'],
]

for name1, name2 in comparison_pairs:
    print(f'Processing {name1} vs {name2}')
    plotMTDP(path, name1, name2)

print('Done!')
```

---

## 全阻抗与相位张量图

绘制包含完整阻抗张量、倾子和相位张量的综合图件。

### 脚本：PlotFullZ-Site.py

```python
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from matplotlib.collections import EllipseCollection
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# ===== 配置参数 =====
path = r'D:\Thesis\Chapter5\MTDPProject\LModel\A'
name = 'A'

# ===== 读取数据 =====
fre = np.loadtxt(f'{path}/{name}-rxx.dat')[:, 0]
rxx = np.loadtxt(f'{path}/{name}-rxx.dat')[:, 1]
rxy = np.loadtxt(f'{path}/{name}-rxy.dat')[:, 1]
ryx = np.loadtxt(f'{path}/{name}-ryx.dat')[:, 1]
ryy = np.loadtxt(f'{path}/{name}-ryy.dat')[:, 1]

pxx = np.loadtxt(f'{path}/{name}-zxxp.dat')[:, 1]
pxy = np.loadtxt(f'{path}/{name}-zxyp.dat')[:, 1]
pyx = np.loadtxt(f'{path}/{name}-zyxp.dat')[:, 1]
pyy = np.loadtxt(f'{path}/{name}-zyyp.dat')[:, 1]

# 倾子数据
tzxr = np.loadtxt(f'{path}/{name}-tzxr.dat')[:, 1]
tzxi = np.loadtxt(f'{path}/{name}-tzxi.dat')[:, 1]
tzyr = np.loadtxt(f'{path}/{name}-tzyr.dat')[:, 1]
tzyi = np.loadtxt(f'{path}/{name}-tzyi.dat')[:, 1]

# ===== 配置坐标范围 =====
yfmin, yfmax = 2, 35
y_min = 1e-1
y_max = 1e5
x_min = np.min(fre)
x_max = np.max(fre)
xdelta = (np.log(x_max) - np.log(x_min)) / 10
x_min = np.exp(np.log(x_min) - xdelta)
x_max = np.exp(np.log(x_max) + xdelta)

# ===== 绘图 =====
fig, axs = plt.subplots(4, 1, figsize=(8, 10), sharex='all',
                        gridspec_kw={'height_ratios': [4, 4, 2, 2]},
                        constrained_layout=True)

# 1. 视电阻率
ax = axs[0]
ax.loglog(fre, rxx, 'mx', label='XX', markerfacecolor='none')
ax.loglog(fre, rxy, 'ro', label='XY', markerfacecolor='none')
ax.loglog(fre, ryx, 'bs', label='YX', markerfacecolor='none')
ax.loglog(fre, ryy, 'c+', label='YY', markerfacecolor='none')
ax.set_ylim(y_min, y_max)
ax.set_yscale('log')
ax.set_xlim(x_min, x_max)
ax.invert_xaxis()
ax.set_ylabel(r'$\rho\;(\Omega \cdot m)$')
ax.grid(True, which='major', linestyle='--', linewidth=0.5)
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1.0))

# 2. 相位
ax = axs[1]
ax.semilogx(fre, pxx, 'mx', label='XX', markerfacecolor='none')
ax.semilogx(fre, pxy, 'ro', label='XY', markerfacecolor='none')
ax.semilogx(fre, pyx, 'bs', label='YX', markerfacecolor='none')
ax.semilogx(fre, pyy, 'c+', label='YY', markerfacecolor='none')
ax.set_ylim(-180, 180)
ax.set_yticks(np.arange(-180, 181, 90))
ax.set_ylabel(r'$\varphi\;(\degree)$')
ax.grid(True, which='major', linestyle='--', linewidth=0.5)
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1.0))

# 3. 倾子
ax = axs[2]
ax.semilogx(fre, tzxr, 'rv', label='Xr', markerfacecolor='none')
ax.semilogx(fre, tzxi, 'r^', label='Xi', markerfacecolor='none')
ax.semilogx(fre, tzyr, 'bo', label='Yr', markerfacecolor='none')
ax.semilogx(fre, tzyi, 'bs', label='Yi', markerfacecolor='none')
ax.set_ylim(-0.5, 0.5)
ax.set_ylabel('Tipper')
ax.grid(True, which='major', linestyle='--', linewidth=0.5)
ax.legend(loc='upper right', bbox_to_anchor=(1.15, 1.0))

# 4. 相位张量椭圆
ax = axs[3]
axLinear = ax.twiny()
axLinear.set_xscale('linear')
axLinear.set_xlim(np.log10(x_min), np.log10(x_max))
axLinear.invert_xaxis()

# 相位张量参数
beta = np.loadtxt(f'{path}/{name}-beta.dat')[:, 1]
alpha = np.loadtxt(f'{path}/{name}-alpha.dat')[:, 1]
pmin = np.abs(np.loadtxt(f'{path}/{name}-pmin.dat')[:, 1])
pmax = np.abs(np.loadtxt(f'{path}/{name}-pmax.dat')[:, 1])

# 归一化椭圆尺寸
midp = 1
ptscale = 1 / (np.log10(x_max) - np.log10(x_min))
pmax = pmax / midp * ptscale
pmin = pmin / midp * ptscale
pmax[pmax > 3 * ptscale] = 3 * ptscale

# 绘制相位张量椭圆
cmap = plt.get_cmap('rainbow')
tmpbeta = np.abs(beta.copy())
tmpbeta[tmpbeta > 10] = 10
tmpbeta = tmpbeta / 10

ellipses = EllipseCollection(
    widths=pmax, heights=pmin, angles=alpha - beta,
    units='xy', offsets=np.column_stack((np.log10(fre), np.ones_like(fre) * 0.5)),
    transOffset=axLinear.transData, facecolor=cmap(tmpbeta), lw=0
)
axLinear.add_collection(ellipses)
axLinear.get_xaxis().set_visible(False)

# 添加色标
norm = Normalize(vmin=0, vmax=10)
cax = inset_axes(axs[3], width="5%", height="100%", loc='upper right',
                 bbox_to_anchor=(0.1, 0., 1, 1), bbox_transform=axs[3].transAxes)
cb = plt.colorbar(ScalarMappable(cmap=cmap, norm=norm), cax=cax, orientation='vertical')
cb.set_label(r'$|\beta|$')

ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Phase Tensor')

# 保存
plt.savefig(f'{path}/{name}-Z.png', dpi=300, bbox_inches='tight')
plt.savefig(f'{path}/{name}-Z.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.show()
```

---

## PDF 合并工具

将多个 PDF 文件合并为一个。

### 脚本：MergerAllZPDF.py

```python
import os
from PyPDF2 import PdfMerger

# 配置参数
path = r'D:\Research\MT3D\Figures'
output_name = 'ALL'

# 获取所有 PDF 文件
pdf_files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.pdf')]

# 合并 PDF
merger = PdfMerger()
for pdf_file in pdf_files:
    merger.append(pdf_file)

# 保存
output_path = os.path.join(path, f'{output_name}.pdf')
merger.write(output_path)
merger.close()

print(f'Combined PDF saved: {output_path}')
```

---

## 坐标转换工具

在 GIS 应用中，可能需要将 MTDataPro 导出的坐标转换为不同的坐标系。

### 脚本：coorConvert.py

```python
from shapely.geometry import Point
from pyproj import CRS, Transformer

# WGS84 坐标
wgs84_point = Point(120.5, 30.25)  # (经度, 纬度)

# 转换到目标坐标系（如 Web Mercator）
target_crs = CRS("EPSG:3857")
transformer = Transformer.from_crs(CRS("EPSG:4326"), target_crs)

# 执行转换
x, y = transformer.transform(wgs84_point.x, wgs84_point.y)
print(f'转换后坐标: {x}, {y}')

# 支持的坐标系
# EPSG:4326 - WGS84
# EPSG:3857 - Web Mercator
# EPSG:4490 - China Geodetic Coordinate System 2000
# EPSG:4549 - China TM-3 117E
```

---

## 常见问题

### Q: 绘图的频率范围如何设置？

A: 根据您的数据频率范围调整 `xmin` 和 `xmax`：
- AMT 数据：通常 10 Hz ~ 10 kHz
- MT 数据：通常 0.001 Hz ~ 100 Hz
- 远参考 MT：可低至 0.0001 Hz

### Q: 误差棒不显示？

A: 确保从 MTDataPro 导出了误差数据文件（`*-rxyvar.dat` 等）。误差在对数坐标下需要转换：
```python
log_error = error / (value * np.log(10))
```

### Q: 如何调整图形尺寸？

A: 修改 `figsize` 参数：
```python
fig, axs = plt.subplots(2, 1, figsize=(10, 8))  # 宽10英寸，高8英寸
```

### Q: 中文标签显示为方块？

A: 使用系统支持的中文字体：
```python
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
```
建议使用英文标签以确保跨平台兼容性。
