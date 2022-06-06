// 请求控制

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

// 获取全国数据
function get_center_bottom() {
    $.ajax({
        url: "/center_bottom",
        success: function (data) {
            // console.log("data:", data )
            optionMap.series[0].data = data.map;
            ec_center.setOption(optionMap);
        },
        error: function (xhr, type, errorThrown) {
            console.log("获取时间失败：", errorThrown)
        }
    })
}

// 获取全国数据疫情趋势数据
function get_left_top() {
    $.ajax({
        url: "/left_top",
        success: function (data) {
            // console.log("data:", data )
            option_left1.xAxis.data = data.day
			option_left1.series[0].data = data.confirm
			option_left1.series[1].data = data.suspect
			option_left1.series[2].data = data.heal
			option_left1.series[3].data = data.dead
			ec_left1.setOption(option_left1)
        },
        error: function (xhr, type, errorThrown) {
            console.log("获取时间失败：", errorThrown)
        }
    })
}


// 全国疫情新增数据
function get_left_bottom() {
    $.ajax({
        url: "/left_bottom",
        success: function (data) {
            // console.log("data:", data )
            option_left2.xAxis.data = data.day
			option_left2.series[0].data = data.confirm_add
			option_left2.series[1].data = data.suspect_add
			ec_left2.setOption(option_left2)
        },
        error: function (xhr, type, errorThrown) {
            console.log("获取时间失败：", errorThrown)
        }
    })
}


// 柱状图
function get_right_top_data() {
	$.ajax({
		url:"/right_top",
		success: function(data) {
			option_right1.xAxis.data = data.city
			option_right1.series[0].data = data.confirm
			ec_right1.setOption(option_right1)
		},
		error: function(xhr, type, errorThrown) {

		}
	})
}

// 词云图
function get_right_bottom() {
    $.ajax({
        url: "/right_bottom",
        success: function (data) {
            console.log("data:", data )
			option_right2.series[0].data = data.kws
			ec_right2.setOption(option_right2)
        },
        error: function (xhr, type, errorThrown) {
            console.log("获取时间失败：", errorThrown)
        }
    })
}

// 初始化调用
getTime()
get_left_top()
get_left_bottom()
get_center_bottom()
get_center_top()
get_right_top_data()
get_right_bottom()

//  定时更新
setInterval(getTime, 1000)
setInterval(get_left_top, 1000*100)
setInterval(get_left_bottom, 1000*100)
setInterval(get_center_bottom, 1000*100)
setInterval(get_right_top_data, 1000*100)
setInterval(get_right_bottom, 1000*100)