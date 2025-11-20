"""Constants of the Xiaomi Aqara Lock."""

WITH_LI_BATTERY = 1
SUPPORT_ALARM = 2
SUPPORT_DOORBELL = 4
SUPPORT_CAMERA = 8
SUPPORT_WIFI = 16

DEVICE_MAPPINGS = {
    "lumi.lock.aq1": SUPPORT_ALARM,
    "lumi.lock.acn02": SUPPORT_ALARM | SUPPORT_DOORBELL,
    "lumi.lock.acn03": SUPPORT_ALARM | SUPPORT_DOORBELL,
    "aqara.lock.eicn01": SUPPORT_ALARM | SUPPORT_DOORBELL,
    "aqara.lock.acn001": SUPPORT_ALARM | SUPPORT_DOORBELL,
    "aqara.lock.aqgl01": SUPPORT_ALARM | SUPPORT_DOORBELL,
    "aqara.lock.acn004": (
        WITH_LI_BATTERY | SUPPORT_ALARM |
        SUPPORT_DOORBELL | SUPPORT_WIFI),
    "aqara.lock.acn005": (
        WITH_LI_BATTERY | SUPPORT_ALARM |
        SUPPORT_DOORBELL | SUPPORT_WIFI),
    "aqara.lock.wbzac1": (
        WITH_LI_BATTERY | SUPPORT_ALARM |
        SUPPORT_DOORBELL | SUPPORT_WIFI | SUPPORT_CAMERA),
    "aqara.lock.bzacn3": (
        SUPPORT_ALARM | SUPPORT_DOORBELL),
    "aqara.lock.bzacn4": (
        SUPPORT_ALARM | SUPPORT_DOORBELL),
    "aqara.lock.dacn03": (
        WITH_LI_BATTERY | SUPPORT_ALARM |
        SUPPORT_DOORBELL | SUPPORT_WIFI | SUPPORT_CAMERA),
    "aqara.lock.acn002": (
        WITH_LI_BATTERY | SUPPORT_ALARM |
        SUPPORT_DOORBELL | SUPPORT_WIFI | SUPPORT_CAMERA),
    "aqara.lock.agl002": SUPPORT_ALARM | SUPPORT_DOORBELL,
    "aqara.lock.acn10": SUPPORT_ALARM
}

LOCK_NOTIFICATION = {
    "latch_state": {
        "default": "反锁状态已改变",
        "0": "从内部解除反锁",
        "1": "已反锁"},
    "lock": {
        "default": "门锁状态已改变",
        "0": "门已打开",
        "1": "门已关闭",
        "2": "门未关好",
        "3": "门铃正在响",
        "4": "门锁已损坏",
        "5": "门被遮挡",
        "6": "其他 1",
        "7": "其他 2"},
    "door": {
        "default": "门状态已改变",
        "0": "未知",
        "1": "门无法上锁",
        "2": "门未关闭",
        "3": "门未上锁",
        "4": "门已上锁",
        "5": "门已自动上锁",
        "6": "门已解锁",
        "7": "门已上锁并自动上锁",
        "8": "门保持解锁"},
    "lock_event": {
        "default": "收到门锁事件",
        "0": "解锁",
        "1": "上锁"
    },
    "unlock from inside": {"default": "从内部解锁"},
    "someone detected": {"default": "有人在门口逗留"},
    "li battery notify":
        {"default": "锂电池通知",
            "0": "锂电池异常",
            "1": "锂电池正常"},
    "battery notify":
        {"default": "电池通知",
            "0": "电池电量耗尽",
            "1": "电池电量低",
            "2": "电池电量中等",
            "3": "电池电量充足"},
    "camera connected": {"default": "摄像头已连接"},
    "open in away mode": {
        "default":
            "在离家模式下，有人从室内打开门"},
    "lock by handle": {"default": "通过把手上锁"},
    "auto locking":
        {"default": "自动上锁状态已改变",
         "1": "自动上锁"},
    "unlock by password": {"default": "用户通过密码解锁"},
    "unlock by fingerprint": {"default": "用户通过指纹解锁"},
    "unlock by bluetooth": {"default": "用户通过蓝牙解锁"},
    "unlock by homekit": {"default": "用户通过 HomeKit 解锁"},
    "unlock by key": {"default": "用户通过钥匙解锁"},
    "unlock by nfc": {"default": "用户通过 NFC 解锁"},
    "unlock by face": {"default": "用户通过人脸解锁"},
    "unlock by temporary password": {"default": "通过临时密码解锁"},
    "away mode": {
        "default": "离家模式已改变",
        "0": "离家模式已移除",
        "1": "离家模式已启用"},
    "nfc added": {"default": "已添加 NFC 卡或标签"},
    "nfc removed": {"default": "已移除 NFC 卡或标签"},
    "verification failed": {
        "default": "门锁验证失败",
        "3235774464": "密码错误导致频繁开门失败",
        "3235774465": "指纹错误导致频繁开门失败",
        "3235774469": "钥匙异常导致频繁开门",
        "3235774470": "钥匙孔有异物",
        "3235774471": "钥匙未取出",
        "3235774472": "NFC 错误导致频繁开门失败",
        "3235774473": "超时后门已解锁",
        "3235774474": "多次验证失败（高级保护）",
        "3235778564": "自动锁体异常"},
    "user added": {
        "default": "添加用户"},
    "user removed": {
        "default": "移除用户"},
    "all user removed": {
        "default": "移除所有用户"},
}
