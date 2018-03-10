#coding=utf8

import os
import itchat

itchat.auto_login(True)
print('登陆成功!')
itchat.send_msg(u'这是您在 x factory 拍的志拍~', 'filehelper')
print('照骗发送中...')
itchat.send_image('./selfie.jpg', 'filehelper')
print('照骗已经发送到您的微信文件传输助手!')
itchat.send_msg(u'保存下来发个圈留个念吧', 'filehelper')
itchat.logout()
print('帐号已经登出!')
#itchat.run()