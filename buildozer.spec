[app]
# 应用显示名称
title = MyPythonApp
# 版本号
package.version = 0.1
# 包标识（随便填，唯一即可）
package.name = mypyapp
package.domain = org.mypy.app

# 源码目录，根目录就是 .
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas

# 入口文件
main.py = main

# 依赖库
requirements = python3,kivy

# Android 配置
android.api = 33
android.ndk = 25c
android.permissions = INTERNET
