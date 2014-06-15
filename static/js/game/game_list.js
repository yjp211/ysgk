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