function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function getCsrftoken(){
    return getCookie('csrftoken');
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", getCsrftoken());
        }
    }
});


function debug(msg){
    console.log(msg);
}

function messagebox(msg){
    debug(msg);
    alert(msg);
}

/**
 * 判断字符是否在一个以split作为分隔的字符串中
 * @param item： 要查找的项
 * @param org： 原始字串
 * @param split: 分隔方式，默认以逗号分隔
 */
function itemExistInStr(item, org){
    var split = arguments[2] ? arguments[2] : ',';
    var item = '' + item;
    return $.inArray(item, org.split(split)) >= 0;
}

/**
 * 将字符串添加到另一个字符串中，并且以split作为分隔
 * 'abc'添加到 'str1,str2,str3' ---> 'str1,str2,str3,abc'
 * @param item： 要添加的项
 * @param org： 原始字串
 * @param split: 分隔方式，默认以逗号分隔
 */
function strListAddItem(item, org){
    var split = arguments[2] ? arguments[2] : ',';
    var item = '' + item;
    if(itemExistInStr(item, org, split)){
        return true;
    }
    if(org.length == 0){
        return item;
    }
    return '' + org + split + item;
}

/**
 * 在一个以split分隔的字符串中删除一个指定的序列
 * @param item： 要添加的项
 * @param org：原始字符串
 * @param split：分隔符，默认为逗号
 */
function strListReItem(item, org){
    var split = arguments[2] ? arguments[2] : ',';
    var item = '' + item;
    var arr = org.split(split);
    var index = $.inArray(item, arr);
    if(index < 0){
        return org;
    }
    arr.splice(index, 1);
    var newStr = "";
    for(var i=0; i < arr.length; i++){
        if(i == 0){
            newStr = arr[i];
        }else{
            newStr += split + arr[i];
        }
    }
    return newStr;
}