/**
 * Created by YJP on 2014/6/18.
 */


function  deleteCategory(obj){

    if(!confirm("确认删除该系列？")){
        return false
    }
    var url = $(obj).attr('url');
    $.ajax({
        url: url,
        type: 'POST',
        dataType: 'JSON',
        success: function(ret){
            if(ret.success){
                messagebox("删除系列成功");
                location.reload();
            }else{
                messagebox("删除系列失败，" + ret.msg);
            }
        },
        error: function(){
            messagebox("删除系列失败，网络出现错误");
        }
    });

}