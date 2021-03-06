
var ec_right2 = echarts.init(document.getElementById("right-bottom"), "dark");

// 词云图
var datamessage = [];
var option_right2 = {
    title: {
        text: "今日疫情实时播报热词",
        textStyle: {
            color: 'white'
        },
        left: 'left'
    },
    tooltip: {
        show: false
    },
     //工具框，可以选择
    toolbox: {
        feature: {
            saveAsImage: {} //下载工具
        }
    },
    series: [{
        type: 'wordCloud',
        gridSize: 1,
        sizeRange: [12, 55], //文字范围
        //文本旋转范围，文本将通过rotationStep45在[-90,90]范围内随机旋转
        rotationRange: [-45, 0, 45, 90],
        // rotationStep: 45,
        // textRotation: [0, 45, 90, -45],
        // //形状
        // shape: 'circle',
        textStyle: {
            normal: {
                color: function () { //文字颜色的随机色
                    return 'rgb(' +
                        Math.round(Math.random() * 255) +
                        ',' + Math.round(Math.random() * 255) +
                        ',' + Math.round(Math.random() * 255) + ')'
                }
            }
        },
        right: null,
        bottom: null,
        data: datamessage
    }]
};
//使用制定的配置项和数据显示图表
ec_right2.setOption(option_right2);