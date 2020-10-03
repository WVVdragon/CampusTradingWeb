# CampusTradingWeb 校园二手交易网站

技术方案：django + react + ant

预期功能：
	1. 登录，注册
	2. 首页：浏览商品、筛选品类/价格
	3. 商品详情页：商品详情、评论、交易

2020/09/30 确定选型，初步启动

2020/10/03 首页：筛选功能完成、界面排版完成
调整了前端代码，目前可读性良好\n
	-index.js "export Container" 包含首页的所有组件、以及连接后端的ajax请求函数
	-indexPage/searchBlock.js "export searchBlock" 搜索组件，包含搜索框和条件筛选器
	-indexPage/commodityExhibiton.js "export Exhibiton" 商品展示组件

近期遇到的问题：
	1. ajax跨域请求报错，原因是前后端分离。 
	解决方法：在django的setting.py中添加CORS设置：
		CORS_ALLOW_CREDENTIALS = True
		CORS_ORIGIN_WHITELIST = [
		'http://localhost:3000/'  #前端的ip地址，因为目前是本地调试，所以ip是localhost
		]
	2. 复杂sql请求
	解决方法：使用connection.cursor()功能，可以直接用熟悉的sql语句进行请求。
	3. 