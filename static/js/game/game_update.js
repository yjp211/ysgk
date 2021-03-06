$(function () {

    /**
     * upload warp中的上传按钮激活时，
     * 在wrap前插入一个holder，并触发hodler file元素点击事件
     */
    $(document).on('click', '.upload-wrap .wrap :button', function () {
        $(this).prev(':file').click();
    });


    /**
     * file元素内容改动时，读取文件
     * file元素的最上层upload wrap定义了两个属性
     * is-image：上传的是否是图片，是：图片预览，否：显示文件的基本信息
     * 在预览文件完成后开始ajax上传文件，上传文件后将后台返回的文件ID保存到文件"for"属性指代的hidden元素中
     */
    $(document).on('change', '.upload-wrap .wrap :file', function () {
        //获取到最顶层的upload-wrap
        //upload-wrap有两个属性参数
        var upload_warp = $(this).parent('.wrap').parent('.upload-wrap');
        var max_upload = parseInt(upload_warp.attr('max-upload'));
        var cur_node = upload_warp.children('.holder').length;

        //上传图片的个数已经达到数目，隐藏上传按钮。
        if (cur_node + 1 >= max_upload) {
            upload_warp.children('.wrap').hide();
        }

        var is_image = upload_warp.attr('is-image') == "true";
        var upload_for = upload_warp.attr('for');
        var for_obj = upload_warp.prev(":input[name='" + upload_for + "']");
        var html = '<div class="holder hidden">'
            + '<div class="preview"></div>'
            + '<span class="glyphicon glyphicon-remove remove" title="移除"></span>'
            + '<div class="progress  progress-striped active">'
            + '<div class="progress-bar" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100">'
            + '</div>'
            + '</div>'
            + '</div>';

        $(this).parent('.wrap').before(html);


        var holder = $(this).parent('.wrap').prev('.holder');
        var preview = holder.children('.preview');
        var progress_obj = holder.children('.progress').children('.progress-bar');
        var file = this.files[0];

        if (is_image) {
            var reader = new FileReader();
            reader.onload = function (event) {
                var image = new Image();
                image.src = event.target.result;
                preview.append(image);
                holder.removeClass('hidden');
                uploadFile(file, progress_obj, for_obj, preview);
            };
            reader.readAsDataURL(file);
        } else {
            preview.append('<p>' + file.name + ' :: ' + (file.size ? (file.size / 1024 | 0) + 'K' : ''));
            holder.removeClass('hidden');
            uploadFile(file, progress_obj, for_obj, preview);
        }
        $(this).val('');
    });


    /**
     * 上传文件
     * 不会有多个文件同时上传的情况
     * @param file， file文件
     * @param progress， 进度条
     * @param for_obj, 上传成功后文件ID保存的目标元素
     * @param preview, 标记预览的元素是否上传
     */
    function uploadFile(file, progress, for_obj, preview) {
        var formData = new FormData();
        formData.append('use_on', for_obj.attr('name'));
        formData.append('file', file);
        progress.css('width', '40%');

        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/misc/upload_file/');
        xhr.responseType = 'json';
        xhr.setRequestHeader("X-CSRFToken", getCsrftoken());

        //上传之中
        xhr.upload.onprogress = function (event) {
            if (event.lengthComputable) {
                var complete = (event.loaded / event.total * 100 | 0) + '%';
                progress.css('width', complete);
            }
        };

        //上传完成
        xhr.onload = function (event) {
            if(xhr.status == 200) {
                var ret = xhr.response;
                if (ret['success']) {
                    progress.css('width', '100%');
                    progress.addClass('progress-bar-success');
                    progress.parent().hide(); //上传完成后隐藏进度条
                    var file_id = ret['data']['file_id'];
                    preview.attr('file_id', file_id);
                    var cur_val = for_obj.val();
                    for_obj.val(strListAddItem(file_id, cur_val));
                } else {
                    progress.css('width', '40%');
                    progress.addClass('progress-bar-danger');
                    messagebox("上传文件失败，" + ret['msg']);
                }
            }else{
                progress.css('width', '40%');
                progress.addClass('progress-bar-danger');
                messagebox("上传文件失败，服务器异常响应");
            }


        };

        //上传失败
        xhr.onerror = function (event) {
            progress.css('width', '40%');
            progress.addClass('progress-bar-danger');
        };

        xhr.send(formData);


    }
    /**
     * 删除按钮的点击事件
     * 删除图片时根据holder中的file元素判断该元素是否上传成功，
     * 1. 如果上传成功，先删除掉服务器上的文件，再删除对应的for_obj中该文件ID，再进行第二步
     * 2. 上传失败则将隐藏的上传按钮显示，并删除掉该holder
     */
    $(document).on('click', '.upload-wrap .holder span.remove', function () {
        var _this = this;
        var preview = $(this).prevAll('.preview');
        var file_id = preview.attr('file_id');

        //上传成功删除远程文件
        if(typeof(file_id) != "undefined" ){
            $.ajax({
                url: '/misc/delete_file/',
                type: 'POST',
                data: {'file_id': file_id},
                dataType: 'JSON',
                success: function(){
                    var upload_warp = $(_this).parent('.holder').parent('.upload-wrap');
                    var upload_for = upload_warp.attr('for');
                    var for_obj = upload_warp.prev(":input[name='" + upload_for + "']");
                    var cur_val = for_obj.val();
                    for_obj.val(strListReItem(file_id, cur_val));
                    $(_this).parent('.holder').nextAll('.wrap').show();
                    $(_this).parent('.holder').remove();
                },
                error: function(){
                    messagebox("删除文件失败，网络出现错误");
                }
            });

        }else{
            $(_this).parent('.holder').nextAll('.wrap').show();
            $(_this).parent('.holder').remove();
        }
    });


    //将表单中所有的元素根据name, value收集到一个字典中
    function collectFrom(obj) {
        var dict = {};
        //收集所有的文本信息
        obj.find(":hidden, :text, :password, textarea, select").each(function () {
            if (typeof($(this).attr('name')) != "undefined") {
                dict[$(this).attr('name')] = $(this).val();
            }
        });

        //收集所有的选中checkbox，注意因为是多选，所以要用逗号分隔
        $(obj).find(":checkbox:checked").each(function () {
            if (typeof($(this).attr('name')) != "undefined") {
                var name = $(this).attr('name');
                if (typeof(dict[name]) == 'undefined') {
                    dict[name] = '';
                }
                dict[name] += $(this).val() + ',';
            }
        });

        //收集所有的选中radio
        $(obj).find(":radio:checked").each(function () {
            if (typeof($(this).attr('name')) != "undefined") {
                dict[$(this).attr('name')] = $(this).val();
            }
        });

        //收集所有的文件
        $(obj).find(":file").each(function () {
            if (typeof($(this).attr('name')) != "undefined") {
                dict[$(this).attr('name')] = this.files[0];
            }
        });
        return dict;
    }

    /**
     * 表单提交事件
     * 不要直接让表单进行提交，而是包装成一个html5 FormData进行提交
     *
     */
    $(document).on('click', '#subBtn', function () {
        var xhr = new XMLHttpRequest();
        var form = $("#game_form");
        var formData = new FormData();

        var dict = collectFrom(form);

        for (var key in dict) {
            formData.append(key, dict[key]);
        }

        //收集所有的文件

        xhr.open('POST', form.attr('action'));
        xhr.responseType = 'json';
        xhr.setRequestHeader("X-CSRFToken", getCsrftoken());
        //上传完成
        xhr.onload = function (event) {
            if(xhr.status == 200) {
                var ret = xhr.response;
                if (ret['success']) {
                    messagebox("操作成功");
                    window.location.href = '/game/list/';
                } else {
                    messagebox("操作失败，" + ret['msg']);
                }
            }else{
                messagebox("操作失败，服务器异常响应");
            }

        };

        //上传失败
        xhr.onerror = function (event) {
            messagebox("操作失败，网络出现异常");
        };
        xhr.send(formData);
        return false;
    });


});
