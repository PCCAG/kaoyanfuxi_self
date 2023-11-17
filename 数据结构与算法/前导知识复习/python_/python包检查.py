# import importlib.metadata

# installed_packages = importlib.metadata.distributions()
# for package in installed_packages:
#     if package.metadata["name"] == "pip":
#         print(
#             f"{package.metadata['name']}=={package.version}, {package.locate_file('')}"
#         )

import shutil

# (模块)shutil
# 用于复制和归档文件和目录树的实用程序函数。
# 这里的函数不复制Mac上的资源分支或其他元数据。
from distutils.sysconfig import get_python_lib

# 返回包含Python库(标准或站点添加)的目录。
# 如果'plat_specific'为true，返回包含平台特定模块的目录，即来自非纯python模块发行版的任何模块;否则，返回平台共享库目录。
# 如果'standard_lib'为true，返回包含标准Python库模块的目录;否则，返回站点特定模块的目录。
# 如果提供了'prefix'，使用它代替sys。Base_prefix或sys。Base_exec_prefix——即忽略'plat_specific'。
pip_path = shutil.which("pip")
# 给定一个命令、模式和一个PATH字符串，返回PATH上符合给定模式的路径，如果没有这样的文件则返回None。
# 模式默认为os。F_OK | os.X_OK。
# path默认为os. environment .get(" path ")的结果，或者可以用自定义搜索路径覆盖。
pip_site_packages = get_python_lib(prefix=pip_path, plat_specific=True)

print(f"Pip executable path: {pip_path}")
print(f"Pip site-packages path: {pip_site_packages}")

# import importlib.metadata

# # 获取已安装的包列表
# installed_packages = importlib.metadata.distributions()

# # 遍历每个包并输出其名称、版本和位置
# for package in installed_packages:
#     package_name = package.metadata["name"]
#     package_version = package.version
#     package_location = package.locate_file("")

#     print(f"{package_name}=={package_version}")
#     print(f"Package location: {package_location}\n")
