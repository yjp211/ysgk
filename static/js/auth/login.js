/**
 * document on ready
 */
$(document).ready(function(){
    var loginForm = $("#login-form");
    loginForm.validation();
    $("#login-form button[type=submit]").bind('click', function(){
       loginForm.validate();
       return true;
    });
});