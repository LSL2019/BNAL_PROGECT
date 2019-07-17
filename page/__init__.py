from selenium.webdriver.common.by import By

"""以下配置数据为登录模块"""
# 我
login_me = By.ID, "com.yunmall.lc:id/tab_me"
# 已有账号去登录
login_account_exists = By.ID, "com.yunmall.lc:id/textView1"
# 账号
login_username = By.ID, "com.yunmall.lc:id/logon_account_textview"
# 密码
login_pwd = By.ID, "com.yunmall.lc:id/logon_password_textview"
# 登录按钮
login_btn = By.ID, "com.yunmall.lc:id/logon_button"
# 昵称
login_nickname = By.ID, "com.yunmall.lc:id/tv_user_nikename"
# 设置
login_setting = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
