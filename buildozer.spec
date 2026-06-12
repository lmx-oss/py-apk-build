[app]

# 应用包名、名称、版本
title = PDF转TXT
package.name = pdf2txt
package.domain = org.pdf2txt
version = 1.0

# 运行入口
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# 权限：读取/写入手机存储（必须，否则无法选文件、保存文件）
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE
android.api = 30
android.ndk = 25b
android.sdk = 24
android.minapi = 24

# 依赖库（关键！把用到的库全部写上）
requirements = python3,kivy==2.2.1

# 关闭调试（正式包建议关闭）
android.debug = 0

# 横竖屏
orientation = portrait

p4a.local_recipes = /home/lmx/.buildozer/android/platform/python-for-android
p4a.source_dir = /home/lmx/.buildozer/android/platform/python-for-android