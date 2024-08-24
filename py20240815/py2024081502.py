import requests  # 导入requests库，这是一个用于发送HTTP请求的第三方库。


def get_wechat_articles():  # 定义一个函数，名为get_wechat_articles，它接受一个参数access_token。
    # 假设的API URL（在现实中，你需要替换为微信提供的实际API URL）
    #api_url = f"https://api.weixin.qq.com/cgi-bin/some/articles?access_token={access_token}"  # 使用f-string格式化字符串，将access_token插入到URL中。
    api_url=f"https://mp.weixin.qq.com/cgi-bin/appmsgpublish?sub=list&begin=0&count=10&token=1505477827&lang=zh_CN"
    # 发送GET请求到上面构建的URL
    response = requests.get(api_url)  # 使用requests库的get方法发送HTTP GET请求，并将响应存储在response变量中。

    # 检查响应状态码，确保请求成功
    if response.status_code == 200:  # 检查HTTP响应的状态码是否为200，这通常表示请求成功。
        # 解析JSON数据
        data = response.json()  # 调用response对象的json方法，将响应体中的JSON字符串解析为Python字典。
        # 假设返回的data是一个包含文章列表的字典，并且有一个键为'articles'
        articles = data.get('articles', [])  # 使用get方法尝试从data字典中获取键为'articles'的值，如果键不存在，则返回空列表[]。
        for article in articles:  # 遍历articles列表中的每个元素（每个元素代表一篇文章）。
            # 假设每篇文章的字典中有'title'和'publish_time'键
            print(f"标题: {article['title']}, 发表时间: {article['publish_time']}")  # 打印每篇文章的标题和发表时间。
    else:  # 如果状态码不是200，
        print("请求失败，状态码:", response.status_code)  # 打印失败的状态码。


# 获取访问令牌（在现实中，你需要通过你的AppID和AppSecret来获取，此处省略）
#access_token = "1505477827"  # 这里应该是一个通过某种方式（如调用另一个API）获取的access_token字符串。

# 调用函数，传入access_token
get_wechat_articles()  # 执行函数，并传入之前获取的access_token。
