import realtime_service
from apscheduler.schedulers.background import BackgroundScheduler

"""
apscheduler  定时任务
"""


def scheduler():
    # 配置调度器
    scheduler = BackgroundScheduler()

    scheduler.start()

    # 每天 2 点运行，指定 jobstore 与 executor，默认都为 default
    scheduler.add_job(
        realtime_service.update_history(),
        trigger='cron',
        hour=2,
        jobstore='mem',
        executor='processpool'
    )

    # 每 3 小时运行一次
    scheduler.add_job(
        realtime_service.update_hotsearch(),
        trigger='interval',
        hours=3
    )

    # 每天 3 点运行，指定 jobstore 与 executor，默认都为 default
    scheduler.add_job(
        realtime_service.update_details(),
        trigger='cron',
        hour=3,
        jobstore='mem',
        executor='processpool'
    )
