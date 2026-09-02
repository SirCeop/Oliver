[app]

title = Oliver
package.name = oliver
package.domain = org.oliver

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy,plyer
orientation = portrait

fullscreen = 0

android.permissions = RECORD_AUDIO
android.accept_sdk_license = True
p4a.branch = master

[buildozer]

log_level = 2

warn_on_root = 1
