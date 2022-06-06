<!--    获取当前时间: 以服务器的时间为主-->
function getTime() {
    $.ajax({
        url: '/time',
        timeout: 10000,
        success: function (data) {
            $('#time').html(data)
        },
        error: function (xhr, type, errorThrown) {
            console.log("获取时间失败：", errorThrown)
        }
    })
}
// 1s更新一次时间
// setInterval(getTime, 1000)
getTime()

// 获取全国数据
function get_center_top() {
    $.ajax({
        url: "/center_top",
        success: function (data) {
            $('.num h1').eq(0).text(data.confirm)
            $('.num h1').eq(1).text(data.suspect)
            $('.num h1').eq(2).text(data.heal)
            $('.num h1').eq(3).text(data.dead)
        },
        error: function (xhr, type, errorThrown) {
            console.log("获取时间失败：", errorThrown)
        }
    })
}
// setInterval(get_center_top, 1000)
get_center_top()