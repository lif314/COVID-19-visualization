import json

import requests


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
        confirm = day["confirm"]
        suspect = day["suspect"]
        heal = day["heal"]
        dead = day["dead"]
        history[ds] = {"confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead}
    # 全国每日新增数据
    for i in data_all["chinaDayAddList"]:
        ds = day['y'] + "." + day['date']
        confirm = i["confirm"]
        suspect = i["suspect"]
        heal = i["heal"]
        dead = i["dead"]
        history[ds].update({"confirm_add": confirm, "suspect_add": suspect, "heal_add": heal, "dead_add": dead})

    # 各省地区今天数据每日数据信息
    details = []
    for pro_infos in data_all['statisGradeCityDetail']:
        province = pro_infos["province"]
        city = pro_infos['city']
        confirm = pro_infos["confirm"]
        confirm_add = pro_infos["confirmAdd"]
        heal = pro_infos["heal"]
        dead = pro_infos["dead"]
        details.append([province, city, confirm, confirm_add, heal, dead])
    return history, details


if __name__ == '__main__':
    history, details = get_tencent_data()
    print(history.keys())
    print(len(details))
