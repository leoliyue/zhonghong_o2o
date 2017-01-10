function newContentSql() {

}
function newContentUrl(form){
    if(form.url_blue.value=='') {
        alert("请输入蓝色后台地址!");
        form.url_blue.focus();
        return false;
    }
    if(form.url_red.value=='') {
        alert("请输入红色后台地址!");
        form.url_red.focus();
        return false;
    }
    if(form.url_type.value=='') {
        alert("类型不能为空!");
        form.url_type.focus();
        return false;
    }
    if(form.url_stuts.value=='') {
        alert("状态不能为空!");
        form.url_type.focus();
        return false;
    }
    if(form.sql_id.value=='') {
        alert("选择要数据库!");
        form.sql_id.focus();
        return false;
    }
}
function save_checkdata(form){
    //if ($(":checkbox[name=checkrequest_data]:checked").size() == 0) {
	//		alert("请至少选择一条记录进行删除操作！");
	//}
    checkrequest = form.checkrequest_data;
    var returncheck = new Array();
    for (var i = 0 ;i < checkrequest.length; i++){
        if (checkrequest[i].checked){
            returncheck.push(checkrequest[i].value)
        }
    }
    if (returncheck.length<=0){
        alert('未选择任何参数')
    }else{
        alert("已选参数 ID 包括 ：  "+returncheck);

        window.close();
    }
    //window.close()
}