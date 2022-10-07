import requests
from lxml import etree


class Dynamic(object):
    def __init__(self):
        self.url = "https://www.soogif.com/"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko)" "Chrome/104.0.0.0 Safari/537.36"}

    # 1.发送请求，获取数据
    def send_requests(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content

    # 2.数据清洗
    def data_cleansing(self, data, rel):
        element = etree.HTML(data)
        html_xpath = element.xpath(rel)
        print(html_xpath)

    # 3.保存数据
    def save_data(self):
        pass

    # 主要运行的方法
    def run(self):
        response_data = self.send_requests(self.url)
        img_xpath = '//div[@class="center"]/a/@href'
        self.data_cleansing(response_data, img_xpath)


if __name__ == '__main__':
    graph = Dynamic()
    graph.run()