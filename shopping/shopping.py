# -*- coding: utf-8 -*-
# @Time    : 2018/9/27 9:14
# @Author  : 张广东
# @Email   : 1536335429@qq.com
# @File    : shopping.py
# @Software: PyCharm
from app import create_app
app = create_app()
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5052)
