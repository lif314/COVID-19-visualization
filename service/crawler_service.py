import json
import requests
import time
from selenium.webdriver import Chrome, ChromeOptions


# 爬虫获取腾讯数据
def get_tencent_data():
    url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_other"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }

    r = requests.get(url, headers)

    res = json.loads(r.text)

    data_all = json.loads(res["data"])

    # 获取中国每天疫情数据
    history = {}
    for day in data_all["chinaDayList"]:
        ds = day['y'] + "." + day['date']
        tup = time.strptime(ds, "%Y.%m.%d")  # 匹配时间
        ds = time.strftime("%Y-%m-%d", tup)  # 改变时间格式
        confirm = day["confirm"]
        suspect = day["suspect"]
        heal = day["heal"]
        dead = day["dead"]
        history[ds] = {"confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead}
    # 全国每日新增数据
    for i in data_all["chinaDayAddList"]:
        ds = i['y'] + "." + i['date']
        tup = time.strptime(ds, "%Y.%m.%d")  # 匹配时间
        ds = time.strftime("%Y-%m-%d", tup)  # 改变时间格式
        confirm = i["confirm"]
        suspect = i["suspect"]
        heal = i["heal"]
        dead = i["dead"]
        if ds in history.keys():
            history[ds].update({"confirm_add": confirm, "suspect_add": suspect, "heal_add": heal, "dead_add": dead})

    # 各省地区今天数据每日数据信息
    details = []
    for pro_infos in data_all['statisGradeCityDetail']:
        update_time = pro_infos['mtime']
        province = pro_infos["province"]
        city = pro_infos['city']
        confirm = pro_infos["confirm"]
        confirm_add = pro_infos["confirmAdd"]
        heal = pro_infos["heal"]
        dead = pro_infos["dead"]
        details.append([update_time, province, city, confirm, confirm_add, heal, dead])
    return history, details


# 获取百度实时播报数据
def get_baidu_Realtime_broadcast():
    # 为什么要执行两次才有数据？ 第一次就直接报错？
    option = ChromeOptions()
    option.add_argument('--headless')  # 隐藏浏览器
    option.add_argument('--no-sandbox')  # linux禁用沙盘

    chrome_path = r"../chromedriver/chromedriver.exe"
    url = "https://voice.baidu.com/act/newpneumonia/newpneumonia#tab1"

    browser = Chrome(executable_path=chrome_path, options=option)

    browser.get(url)

    # 展开全部按钮
    button = browser.find_element_by_css_selector('#ptab-1 > div.Virus_1-1-350_2SKAfr > div.Common_1-1-350_3lDRV2')
    button.click()  # 点击展开
    time.sleep(1)  # 等待1s
    c = browser.find_elements_by_xpath('//*[@id="ptab-1"]/div[3]/div/div[2]/a/div')
    realtime_list = []
    # 解析数据
    for i in c:
        realtime_list.append(i.text)
    return realtime_list


if __name__ == '__main__':
    # history, details = get_tencent_data()
    # print(history.keys())
    # print(len(details))
    realtime_hot = get_baidu_Realtime_broadcast()
    print(realtime_hot)
