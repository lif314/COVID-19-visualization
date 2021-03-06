import random
import string
from jieba.analyse import extract_tags
from flask import Flask, render_template, request, jsonify
from flask_apscheduler import APScheduler

import service.time_service as time_service
import service.db_service as db_service
import service.realtime_service as realtime_service


class Config(object):
    SCHEDULER_API_ENABLED = True


app = Flask(__name__, template_folder=r"./templates")
scheduler = APScheduler()


# @scheduler.task('interval', id='do_job_1', seconds=30, misfire_grace_time=900) # 测试
@scheduler.task('cron', id='do_job_1', hour=10, misfire_grace_time=900) # 每天10点更新
def job_update_history():
    print("更新历史数据")
    realtime_service.update_history()


# @scheduler.task('interval', id='do_job_2', seconds=30, misfire_grace_time=900) # 测试
@scheduler.task('cron', id='do_job_2', hour=10, misfire_grace_time=900) # 每天10点更新
def job_update_details():
    print("更新详细数据")
    realtime_service.update_details()


# @scheduler.task('interval', id='do_job_3', seconds=5, misfire_grace_time=900) # 测试
@scheduler.task('interval', id='do_job_3', seconds=60 * 60 * 5, misfire_grace_time=900) # 每3小时更新一次
def job_update_hot():
    print("更新词云图数据")
    # TODO Message: 'chromedriver.exe' executable needs to be in PATH. Windows系统问题，部署时可以解决
    # realtime_service.update_hotsearch()


@app.route("/")
def hello():
    return render_template('main.html')


# 获取服务器当前时间
@app.route("/time", methods=["GET"])
def get_time():
    time = time_service.get_current_time()
    return time


# 全国疫情重要数据
@app.route("/center_top", methods=["GET"])
def get_center_top_data():
    data = db_service.get_center_top_data()
    return jsonify({"confirm": int(data[0]), "suspect": int(data[1]), "heal": int(data[2]), "dead": int(data[3])})


# 全国疫情地图数据
@app.route("/center_bottom", methods=["GET"])
def get_center_bottom_data():
    res = []
    data = db_service.get_center_bottom_data()
    for tup in data:
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"map": res})


# 全国累计趋势数据
@app.route("/left_top", methods=["GET"])
def get_left_top_data():
    data = db_service.get_left_top_data()
    day, confirm, suspect, heal, dead = [], [], [], [], []
    for a, b, c, d, e in data:
        day.append(a.strftime("%m-%d"))
        confirm.append(b)
        suspect.append(c)
        heal.append(d)
        dead.append(e)
    return jsonify({"day": day, "confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead})


# 全国新增趋势数据
@app.route("/left_bottom", methods=["GET"])
def get_left_bottom_data():
    data = db_service.get_left_bottom_data()
    day, confirm_add, suspect_add, heal_add, dead_add = [], [], [], [], []
    for a, b, c, d, e in data:
        day.append(a.strftime("%m-%d"))
        confirm_add.append(b)
        suspect_add.append(c)
        heal_add.append(d)
        dead_add.append(e)
    return jsonify({"day": day, "confirm_add": confirm_add, "suspect_add": suspect_add, "heal_add": heal_add,
                    "dead_add": dead_add})


# 柱状图数据
@app.route("/right_top", methods=["GET"])
def get_right_top_data():
    data = db_service.get_right_top_data()
    city = []
    confirm = []
    for k, v in data:
        city.append(k)
        confirm.append(int(v))
    return jsonify({"city": city, "confirm": confirm})


# 词云图
@app.route("/right_bottom", methods=["GET"])
def get_right_bottom_data():
    data = db_service.get_right_bottom_data()
    d = []
    num = 0
    for i in data:
        k = i[0].rstrip(string.digits)
        v = i[0][len(k):]
        ks = extract_tags(k)
        for j in ks:
            if not j.isdigit() and num < 50:
                v = random.randint(1, 1000)
                d.append({"name": j, "value": v})
                num = num + 1
    return jsonify({"kws": d})


@app.route("/ajax", methods=["POST"])
def ajax():
    id = request.values.get("id")
    name = request.values.get("name")
    print("收到消息：", id, name)
    return "100"


if __name__ == '__main__':
    scheduler.init_app(app)
    scheduler.start()
    app.run(host="127.0.0.1", port=5000, debug=True)
