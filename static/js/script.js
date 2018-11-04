

               var table = $('#patlist').DataTable({
                    cache: true,
                    bProcessing: false, sAjaxSource: '/tab', "order": [[0, "asc"]], bFilter: false, bInfo: false, lengthChange: false, scrollY: '250px', scrollCollapse: false, bPaginate: false,
                         columns: [
             { "data": "id", "visible": false },
             { "data": "name", "width": "2%" }

             ]

                   })
