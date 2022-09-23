# -----------------------------all the py-----------------------------
# 文件相关
RB_MODE = 'rb'
WB_MODE = 'wb'
NEW_IMAGE_PATH = 'images/new_pic.png'
OLD_IMAGE_PATH = 'images/old_pic.png'
# logging 日志需记录的常量
LOG_ERROR_ONE = "连接校园网Error："
LOG_WARN_ONE = "可能切换了QQ窗口：进行一次覆盖"
LOG_WARN_TWO = "邮件发送：Fail"
LOG_WARN_TREE = "尝试连接校园网失败..."
LOG_WARN_FOUR = "Try again"
LOG_INFO_ONE = "发现新消息：Send"
LOG_INFO_TWO = "邮件发送：Success"
LOG_INFO_TREE = "\n"
LOG_INFO_FOUR = "图片相似度大于99%->判定为信息重复：本次不发送邮件提醒"
LOG_INGO_FIVE = "成功连接校园网"


# -----------------------------get_sms.py-----------------------------
LOG_LEVEL = "DEBUG"
A_MODE = "a"
UTF_8 = "utf-8"
LOG_RESULT_PATH = "result/results.log"
PRINT_START = "程序开始监控QQ聊天窗口"
PRINT_END = "程序结束监控QQ意外退出"
TIME_FORMAT = "%Y-%m-%d %H:%M"
QQ_WINDOW_NAME = '团结的火药桶'


# -----------------------------engine.py-----------------------------
# send_qq 函数
SMTP_QQ_COM = "smtp.qq.com"
SEND_EMAIL_ERROR = "发送QQ邮件Error："

# make_mail 函数
MY_NAME = 'Lns-XueFeng'
EMAIL_SUBJECT = "来消息啦"
FORM, TO, SUBJECT, DATE = 'From', 'To', 'Subject', 'Date'
MIME_NAME, MIME_FORMAT = 'image', 'png'
CONTENT_DISPOSITION, ATTACHMENT = 'Content-Disposition', 'attachment'
CONTENT_ID, NEW_PIC_CLUE = 'Content-ID', "<new_pic.png>"
X_ATTACHMENT_ID, NEW_PIC_PNG = 'X-Attachment-Id', 'new_pic.png'

# run 函数
WINDOW_CLASS_NAME = 'TXGuiFoundation'
WINDOW_NAME = "消息"


# -----------------------------compare.py-----------------------------
SAME_RATE = "图片相似度："
NO_SAME_RATE = "图片不相似度："
PERCENT_SIGN = "%"


# -----------------------------internet.py-----------------------------
PING_BAIDU = "ping baidu.com -n 1"
