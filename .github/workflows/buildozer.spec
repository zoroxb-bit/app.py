[app]
# (str) Title of your application
title = C711 Maintenance Manager

# (str) Package name
package.name = c711manager

# (str) Package domain (needed for android packaging)
package.domain = org.engineering.c711

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,json

# (list) Application requirements
# Note: pillow is required for images, pandas for data handling
requirements = python3,kivy,pillow,pandas,openpyxl

# (str) Supported orientation
orientation = portrait

# (list) Permissions (Required for Camera and Maintenance Logs)
android.permissions = CAMERA, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Android API to use (33 is stable for modern devices)
android.api = 33
android.minapi = 21

# (bool) Use the unfree or free license
android.accept_sdk_license = True

# (str) The Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
# (int) Log level (2 = error only, 1 = info, 0 = debug)
log_level = 2
warn_on_root = 1
