var baseUrl = 'http://127.0.0.1:8000/';

var APIURL = {
    //	查询
    get_trans:"index/get_trans"
}


/*
 *ajax公用方法
 * @url:请求路径
 * @method:请求类型
 * @params:参数
 * @callback:回调方法
 * @iswait:是否有遮盖框
 * @waitword：遮盖框文字
 * */
function apiAjax(url,method,params,callback){
    $.ajax({
        url: baseUrl + url,
        type: method,
        ContentType: "application/json",
        dataType: "json",
        // dataType:"text",
        async: false,
        processData: true,
        timeout: 20,
        data: params,
        success: function(ret) {
            console.log("success")
            console.log(ret)
            if(ret.code == 1){
                callback(ret);
            }else{
                alert(ret.err_msg);
            }
        },
        error: function(err) {
            console.log("error")
            console.log(err)
        }
    })
}

