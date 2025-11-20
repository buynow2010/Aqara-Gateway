# Aqara Gateway for Home Assistant（中文汉化版）

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)
[![Version](https://img.shields.io/badge/version-0.3.2-blue.svg)](https://github.com/buynow2010/Aqara-Gateway)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2023.9%2B-green.svg)](https://www.home-assistant.io/)

Aqara Gateway 的 Home Assistant 集成，支持小米/绿米 Aqara 网关及其子设备。本仓库为完整中文汉化版，所有用户界面、状态、选项均已汉化，便于国内用户使用。

**原版仓库**: [niceboygithub/AqaraGateway](https://github.com/niceboygithub/AqaraGateway)

## 🚀 快速开始

[![添加HACS仓库](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=buynow2010&repository=Aqara-Gateway&category=integration)

**一键安装**: 点击上方徽章，直接在 HACS 中添加此仓库

## 功能特性

### 🌟 完整中文化

- ✅ **配置界面汉化** - 所有配置步骤、字段名称全部中文
- ✅ **设备状态汉化** - 门锁、传感器、开关等所有状态中文显示
- ✅ **动作汉化** - 按钮动作（单击、双击、长按等）全部中文
- ✅ **选择项汉化** - 所有下拉选择、模式切换均为中文

### 🎯 支持设备

#### 网关设备
- Aqara Camera Hub G2H (ZNSXJ12LM / CH-H01)
- Aqara Camera Hub G2H Pro (ZNSXJ15LM)
- Aqara Camera Hub G3 (ZNSXJ13LM / CH-H03)
- Aqara Hub E1 (ZHWG16LM / HE1-G01)
- Aqara Hub M1S (ZHWG15LM / HM1S-G01)
- Aqara Hub M1S 2022 (ZHWG20LM)
- Aqara Hub M2 (ZHWG12LM / HM2-G01)
- Aqara Hub M2 2022 (ZHWG19LM)
- Aqara Hub M3 (ZHWG24LM / HM-G01D)
- Aqara Smart Hub H1 (QBCZWG11LM)
- Aqara AirCondition P3 (KTBL12LM)
- 更多型号...

#### 子设备类型
- 🚪 **门窗传感器** - 门窗状态检测
- 🏃 **人体传感器** - 移动检测、存在感应
- 💡 **灯光设备** - 智能灯泡、LED 控制器
- 🔌 **插座开关** - 智能插座、墙壁开关
- 🌡️ **温湿度传感器** - 温度、湿度、气压监测
- 🔐 **智能门锁** - 多种解锁方式、状态监控
- 🪟 **窗帘电机** - 窗帘、百叶窗控制
- 🔘 **无线开关** - 单键、双键、魔方等
- 💧 **水浸传感器** - 漏水检测
- 🔥 **烟雾报警器** - 烟雾、燃气检测
- 更多设备类型...

### ✨ 核心功能

- 🔄 **自动发现** - 自动发现网关及子设备
- 🎨 **状态实时更新** - 设备状态实时同步
- 🌈 **完整功能支持** - 支持设备所有功能
- ⚡ **性能优异** - 轻量级设计，响应迅速
- 🔧 **易于配置** - UI 配置界面，无需手动编写 YAML

## 系统要求

### Home Assistant

- 版本：2023.9.0+
- 已安装 HACS（推荐）

### 网关要求

- 支持的 Aqara 网关型号（见上方列表）
- 已开启 Telnet 功能（首次配置需要）
- 网关已连接至局域网

## 安装方式

### 方法一：通过 HACS 安装（推荐）

[![添加HACS仓库](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=buynow2010&repository=Aqara-Gateway&category=integration)

**一键安装（推荐）**：点击上方徽章，直接在 HACS 中添加此仓库

**手动添加**：

1. 确保已安装 [HACS](https://hacs.xyz/)
2. 在 HACS 中点击右上角菜单 → **自定义存储库**
3. 添加仓库地址：`https://github.com/buynow2010/Aqara-Gateway`
4. 类别选择：**集成（Integration）**
5. 点击 **添加**
6. 在 HACS 中搜索 "**Aqara Gateway**"
7. 点击 **下载**
8. 重启 Home Assistant

### 方法二：手动安装

1. 下载本仓库的所有文件
2. 将 `aqara_gateway` 文件夹复制到你的 Home Assistant 配置目录下的 `custom_components/` 目录
3. 目录结构应该是：`custom_components/aqara_gateway/`
4. 重启 Home Assistant

### 版本更新说明

**当前版本**: `v0.3.2`

**更新步骤**：

1. 通过 HACS 更新或手动下载新版本文件
2. 替换 `custom_components/aqara_gateway/` 目录
3. 重启 Home Assistant

## 配置说明

### 首次配置

1. 在 Home Assistant 中进入：**设置** → **设备与服务** → **添加集成**
2. 搜索 "**Aqara Gateway**"
3. 输入网关信息：
   - **主机地址**：网关的 IP 地址
   - **访问令牌（Token）**：仅首次开启 Telnet 时需要
   - **密码**：Telnet 密码（可选）
   - **型号**：选择网关型号
4. 点击提交，等待设备自动发现

### 开启 Telnet

首次使用需要开启网关的 Telnet 功能：

**适用网关**：M1S、P3、E1 等

**开启步骤**：

1. 将网关设置为米家 Home 模式
2. 获取网关 Token，方法参考：[xiaomi-cloud-tokens-extractor](https://github.com/piotrmachowski/xiaomi-cloud-tokens-extractor)
3. 在配置时输入 Token
4. 如果已开启 Telnet，则不需要再输入 Token

### 配置选项

配置完成后，可以在集成选项中调整：

- **调试模式** - 开启详细日志
- **统计信息** - 显示网关统计数据
- **忽略离线消息** - 忽略设备离线通知

## 使用示例

### 门锁状态监控

门锁的所有状态和通知均已汉化：

- **解锁方式**：通过密码解锁、通过指纹解锁、通过 NFC 解锁等
- **门状态**：门已打开、门已关闭、门未关好
- **锁状态**：已上锁、已解锁、已反锁
- **电池状态**：电池电量低、电池电量中等、电池电量充足

### 按钮动作

无线开关的所有动作均为中文：

- **单击** - 按一次
- **双击** - 快速按两次
- **长按** - 持续按住
- **三击** / **四击** - 多次点击
- **顺时针** / **逆时针** - 旋钮旋转

### 魔方动作

魔方的所有动作均为中文：

- **翻转90度** / **翻转180度**
- **移动**、**敲击**、**摇晃**
- **旋转**、**长按旋转**

### 窗帘控制

窗帘状态和充电信息：

- **未充电**、**充电中**、**停止充电**、**充电失败**
- **无行程**、**行程已设置**

## 故障排除

### 无法发现设备

**检查网关连接**：

```bash
ping <网关IP地址>
```

**确认 Telnet 已开启**：

```bash
telnet <网关IP地址>
```

**查看日志**：

```
设置 → 系统 → 日志
```

搜索 `aqara_gateway` 相关错误

### 设备离线

1. 检查网关是否在线
2. 检查子设备电池电量
3. 尝试重新配对设备
4. 重启网关和 Home Assistant

### Token 获取失败

参考官方文档获取 Token：

- [xiaomi-cloud-tokens-extractor](https://github.com/piotrmachowski/xiaomi-cloud-tokens-extractor)
- [小米 IoT 开发者平台](https://iot.mi.com/)

### 更新后配置丢失

1. 备份配置文件（`custom_components/aqara_gateway/`）
2. 重新安装集成
3. 恢复备份
4. 重启 Home Assistant

### 网关统计信息

可在配置选项中开启统计功能，查看：

- Telnet 连接状态
- MQTT 代理连接状态
- Zigbee 设备统计

## 汉化内容

### 配置界面
- 所有配置步骤描述
- 字段名称：主机地址、密码、访问令牌、型号等
- 错误提示信息

### 设备状态
- **门锁**：所有锁状态、门状态、解锁方式、通知信息
- **传感器**：未知状态、电池状态等
- **开关按钮**：单击、双击、长按、旋转等动作
- **魔方**：翻转、移动、敲击、摇晃等动作
- **窗帘**：充电状态、电机行程状态

### 选择项
- 风扇模式：低风、中风、高风
- 摆风模式：启用、禁用
- 运行模式：制暖、干燥、风扇、排气
- 监控模式：无方向、左右
- 接近距离：近、中、远
- 其他设备相关选项

## 更新日志

### v0.3.2 (2025-11-20)

- ✅ 完整中文化所有用户界面
- ✅ 汉化配置流程和字段名称
- ✅ 汉化所有设备状态和选择项
- ✅ 汉化门锁通知和解锁方式
- ✅ 汉化按钮动作和魔方动作
- ✅ 汉化窗帘充电状态
- ✅ 保持与原版功能完全兼容

## 支持与反馈

- **问题反馈**: [GitHub Issues](https://github.com/buynow2010/Aqara-Gateway/issues)
- **功能请求**: [GitHub Issues](https://github.com/buynow2010/Aqara-Gateway/issues)
- **讨论交流**: [GitHub Discussions](https://github.com/buynow2010/Aqara-Gateway/discussions)

## 友情链接

### 🏠 Home Assistant 中文网

[![Home Assistant 中文网](https://img.shields.io/badge/Home%20Assistant-%E4%B8%AD%E6%96%87%E7%BD%91-blue?style=for-the-badge&logo=home-assistant)](https://www.hasscn.top/)

[**Home Assistant 中文网 (hasscn.top)**](https://www.hasscn.top/) - 最全面的免费 Home Assistant 中文站点，提供：

- 🚀 **Home Assistant OS 极速版** - 专为中国优化的加速版系统
- ⚡ **HACS 极速版** - 使用国内镜像加速插件下载
- 📚 **中文文档教程** - 详细的安装配置指南
- 💬 **社区支持** - 微信公众号：老王杂谈说

**特别适合国内用户使用，解决下载慢、连接困难等问题！**

## 许可证

MIT License - 详见 [LICENSE](LICENSE)

## 致谢

- [niceboygithub/AqaraGateway](https://github.com/niceboygithub/AqaraGateway) - 原作者项目
- [Home Assistant](https://www.home-assistant.io/) - 开源智能家居平台
- [HACS](https://hacs.xyz/) - Home Assistant 社区商店

---

**如果本项目对你有帮助，欢迎 Star 支持！** ⭐


## 🔧 最新更新 (2025-11-20)

**修复遗漏的属性名称汉化** - 感谢用户反馈！

已补充汉化以下属性名称：
- ✅ 智能马桶：清洁方向、水温、清洗等级、暖风干燥
- ✅ 存在感应器：监控模式、接近距离、反转模式
- ✅ 温控设备：当前温度、目标温度、风扇模式等
- ✅ 其他设备属性全部汉化

详见 [修复说明](FIX_SUMMARY.md)

