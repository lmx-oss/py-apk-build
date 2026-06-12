[app]

# 包名，随便改
package.name = myapp
package.domain = org.myapp

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas

# 启动入口
main.py = main

requirements = python3,kivy

# 关闭不需要的功能
android.permissions = INTERNET
android.api = 33
android.ndk = 25c

# 关闭无用配置
# 删掉所有 app.android.sdk=xxx
