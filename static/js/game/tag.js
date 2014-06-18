/**
 * Created by YJP on 2014/6/18.
 */


function  deleteTag(obj){

    if(!confirm("确认删除该标签？")){
        return false
    }
    var url = $(obj).attr('url');
    $.ajax({
        url: url,
        type: 'POST',
        dataType: 'JSON',
        success: function(ret){
            if(ret.success){
                messagebox("删除标签成功");
                location.reload();
            }else{
                messagebox("删除标签失败，" + ret.msg);
            }
        },
        error: function(){
            messagebox("删除标签失败，网络出现错误");
        }
    });

}