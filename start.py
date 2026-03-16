import os
from ww_login.main import main
from ww_login import lsettings  # 导入配置模块，用于覆盖端口

# 核心：适配 Vercel 强制分配的 PORT 环境变量
# 覆盖 lsettings 中的端口配置，确保与 Vercel 环境兼容
lsettings.port = int(os.getenv("PORT", lsettings.port))
# Vercel 要求必须监听 0.0.0.0（而非 127.0.0.1）
lsettings.host = "0.0.0.0"

if __name__ == "__main__":
    main()
