$(function(){
   $(document).on('submit', '#query-form', function () {
       var tags = "";
       $(this).find(":checkbox[name=tag]:checked").each(function () {
           tags = strListAddItem($(this).val(), tags);
       });
       $(this).find(":hidden[name=tags]").val(tags);
       var categorys = "";
       $(this).find(":checkbox[name=category]:checked").each(function () {
           categorys = strListAddItem($(this).val(), categorys);
       });
       $(this).find(":hidden[name=categorys]").val(categorys);
   });

});

function  deleteGame(obj){

    if(!confirm("确认删除该游戏？")){
        return false
    }
    var url = $(obj).attr('url');
    $.ajax({
        url: url,
        type: 'POST',
        dataType: 'JSON',
        success: function(ret){
            if(ret.success){
                messagebox("删除游戏成功");
                $("#query-form").submit()
            }else{
                messagebox("删除游戏失败，" + ret.msg);
            }
        },
        error: function(){
            messagebox("删除游戏失败，网络出现错误");
        }
    });

}

function  stick(name, obj){

    if(!confirm("确认将该游戏在 [" +  name + "] 中置顶？")){
        return false
    }
    var url = $(obj).attr('url');
    $.ajax({
        url: url,
        type: 'POST',
        dataType: 'JSON',
        success: function(ret){
            if(ret.success){
                messagebox("置顶成功");
                $("#query-form").submit()
            }else{
                messagebox("置顶失败，" + ret.msg);
            }
        },
        error: function(){
            messagebox("置顶失败，网络出现错误");
        }
    });

}

