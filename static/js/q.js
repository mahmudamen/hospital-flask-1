$(document).ready(function() {
$("#refresh").click(function(event){
        console.log("adfsdaf");
    });
 var table = $('#patlist').DataTable({
                cache: true,
                bProcessing: false,
                sAjaxSource: '/tab', "order": [[0, "desc"]], bFilter: false, bInfo: false, lengthChange: false, scrollY: '300px', scrollCollapse: false, bPaginate: false,
                columns: [
             { "data": "id", "visible": false },
             { "data": "name", "visible": false }
            ]
            });
});

