$(function () {

    /**
     * upload warp中的上传按钮激活时，
     * 在wrap前插入一个holder，并触发hodler file元素点击事件
     */
    $(document).on('click', '.upload-wrap .wrap :button', function(){
        var uploadWarp = $(this).parent('.wrap').parent('.upload-wrap');
        var file_name = uploadWarp.attr('file-name');
        var max_upload = parseInt(uploadWarp.attr('max-upload'));
        var cur_node = uploadWarp.children('.holder').length;
        if(max_upload > 1){
            file_name = file_name + (cur_node + 1);
        }
        var html = '<div class="holder hidden">'
                        + '<input type="file" name="' + file_name + '" class="hidden">'
                        + '<div class="preview"></div>'
                        + '<span class="glyphicon glyphicon-remove remove" title="移除"></span>'
                        + '<div class="progress  progress-striped active">'
                        +   '<div class="progress-bar" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" >'
                        +   '</div>'
                        + '</div'
                +  '</div>';

        $(this).parent('.wrap').before(html);
        var file = $(this).parent('.wrap').prev('.holder').children(':input[type=file]').click();


        if(cur_node + 1 >= max_upload){
            uploadWarp.children('.wrap').hide();
        }
    });


    /**
     * file元素内容改动时，读取文件
     * file元素的最上层upload wrap定义了两个属性
     * max-upload：  表示最多可以上传几个同类文件，>1时需要为下次上传做准备
     * is-image：上传的是否是图片，是：图片预览，否：显示文件的基本信息
     */
    $(document).on('change', '.upload-wrap .holder :input[type=file]', function(){
        //获取到最顶层的upload-wrap
        //upload-wrap有两个属性参数
        var uploadWarp = $(this).parent('.holder').parent('.upload-wrap');
        var is_image = uploadWarp.attr('is-image') == "true";
        var holder = $(this).parent('.holder');
        var preview = holder.children('.preview');
        var progress = $(this).nextAll('.progress').children('.progress-bar');
        var file = this.files[0];

        if(is_image){

            var reader = new FileReader();
            reader.onload = function (event) {
                var image = new Image();
                image.src = event.target.result;
                preview.append(image);
                holder.removeClass('hidden');
                uploadFile(file, progress);
            };

            reader.readAsDataURL(file);
        }else{
            preview.append('<p>' + file.name + ' :: ' + (file.size ? (file.size / 1024 | 0) + 'K' : ''));
            holder.removeClass('hidden');
            uploadFile(file, progress);
        }

    });



    /**
     * 上传文件
     * 不会有多个文件同时上传的情况
     * @param obj， file元素
     * @param progress， 进度条
     */
    function uploadFile(file, progress){
        var formData = new FormData();
        formData.append('file', file);
        progress.css('width', '40%');

        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/game/upload_file/');
        xhr.responseType = 'json';
        xhr.setRequestHeader("X-CSRFToken", getCsrftoken());



        //上传失败
        xhr.onerror = function (event) {
           progress.css('width', '40%');
           progress.addClass('progress-bar-danger');
        };

        //上传之中
        xhr.upload.onprogress = function (event) {
            if (event.lengthComputable) {
                var complete = (event.loaded / event.total * 100 | 0) + '%';

                $('.container').prepend('<div>' + complete + '</div>');
                progress.css('width', complete);
            }
        };

         //上传完成
        xhr.onload = function (event) {
           progress.css('width', '100%');
           progress.addClass('progress-bar-success');
           progress.parent().hide();
        };

        xhr.send(formData);

    }

    /**
     * 删除按钮的点击事件
     * file元素的最上层upload wrap定义了两个属性
     * max-upload：  表示最多可以上传几个同类文件，>1时需要为下次上传做准备
     * is-image：上传的是否是图片，是：图片预览，否：显示文件的基本信息
     *
     *
     */
    $(document).on('click', '.upload-wrap .holder span.remove', function(){
        $(this).parent('.holder').nextAll('.wrap').show();
        $(this).parent('.holder').remove();
    });


    //将表单中所有的元素根据name, value收集到一个字典中
    function collectFrom(obj){
        var dict = {};
        //收集所有的文本信息
        obj.find(":hidden, :text, :password, textarea, select").each(function(){
            if(typeof($(this).attr('name')) != "undefined"){
                dict[$(this).attr('name')] = $(this).val();
            }
        });

        //收集所有的选中checkbox，注意因为是多选，所以要用逗号分隔
        $(obj).find(":checkbox:checked").each(function(){
            if(typeof($(this).attr('name')) != "undefined") {
                var name = $(this).attr('name');
                if (typeof(dict[name]) == 'undefined') {
                    dict[name] = '';
                }
                dict[name] += $(this).val() + ',';
            }
        });

        //收集所有的选中radio
        $(obj).find(":radio:checked").each(function(){
            if(typeof($(this).attr('name')) != "undefined") {
                dict[$(this).attr('name')] = $(this).val();
            }
        });

        //收集所有的文件
        $(obj).find(":file").each(function(){
            if(typeof($(this).attr('name')) != "undefined") {
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
    $(document).on('click', '#subBtn', function(){
        var xhr = new XMLHttpRequest();
        var form = $("#game_form");
        var formData = new FormData();

        var dict = collectFrom(form);

        for(var key in dict){
            formData.append(key, dict[key]);
        }

        //收集所有的文件

        xhr.open('POST', form.attr('action'));
        xhr.send(formData);
        return false;
    });

    /**
     *
     */


/**
    function readfiles(files, holder) {
        var formData = tests.formdata ? new FormData() : null;
        for (var i = 0; i < files.length; i++) {
            if (tests.formdata) formData.append('file', files[i]);
            previewfile(files[i]);
        }

        // now post a new XHR request
        if (tests.formdata) {
            var xhr = new XMLHttpRequest();
            xhr.open('POST', '/devnull.php');
            xhr.onload = function () {
                progress.value = progress.innerHTML = 100;
            };

            if (tests.progress) {
                xhr.upload.onprogress = function (event) {
                    if (event.lengthComputable) {
                        var complete = (event.loaded / event.total * 100 | 0);
                        progress.value = progress.innerHTML = complete;
                    }
                }
            }

            xhr.send(formData);
        }
    }


    var holder = document.getElementById('holder'),
        tests = {
            filereader: typeof FileReader != 'undefined',
            dnd: 'draggable' in document.createElement('span'),
            formdata: !!window.FormData,
            progress: "upload" in new XMLHttpRequest
        },
        support = {
            filereader: document.getElementById('filereader'),
            formdata: document.getElementById('formdata'),
            progress: document.getElementById('progress')
        },
        acceptedTypes = {
            'image/png': true,
            'image/jpeg': true,
            'image/gif': true
        },
        progress = document.getElementById('uploadprogress'),
        fileupload = document.getElementById('upload');

    "filereader formdata progress".split(' ').forEach(function (api) {
        if (tests[api] === false) {
            support[api].className = 'fail';
        } else {
            // FFS. I could have done el.hidden = true, but IE doesn't support
            // hidden, so I tried to create a polyfill that would extend the
            // Element.prototype, but then IE10 doesn't even give me access
            // to the Element object. Brilliant.
            support[api].className = 'hidden';
        }
    });

    function previewfile(file) {
        if (tests.filereader === true && acceptedTypes[file.type] === true) {
            var reader = new FileReader();
            reader.onload = function (event) {
                var image = new Image();
                image.src = event.target.result;
                image.width = 250; // a fake resize
                holder.appendChild(image);
            };

            reader.readAsDataURL(file);
        } else {
            holder.innerHTML += '<p>Uploaded ' + file.name + ' ' + (file.size ? (file.size / 1024 | 0) + 'K' : '');
            console.log(file);
        }
    }



    if (tests.dnd) {
        holder.ondragover = function () {
            this.className = 'hover';
            return false;
        };
        holder.ondragend = function () {
            this.className = '';
            return false;
        };
        holder.ondrop = function (e) {
            this.className = '';
            e.preventDefault();
            readfiles(e.dataTransfer.files);
        }
    } else {
        fileupload.className = 'hidden';
        fileupload.querySelector('input').onchange = function () {
            readfiles(this.files);
        };
    }
 */
});
