$(document).ready(function () {
    $("#example").DataTable({
        // fixedHeader: true,
        lengthChange: false,
        dom: 'Bfrtip',
        fixedColumns: {
            left: 2
        },
        // paging: false,
        scrollCollapse: true,
        scrollX: true,
        scrollY: 300,
        sScrollXInner: "100%",
        
        
        buttons: [
            
           
            'colvis',
            
            {
                // messageTop: 'LEMURIA Stock Report',
                extend: 'print',
                exportOptions: {
                    columns: ':visible'
                },
                title: '<center>LEMURIA Stock Report</center>'
                
            },
            {
                extend: 'pdfHtml5',
                exportOptions: {
                    columns: ':visible'
                }
            },
            
            // {
            //     extend: 'excelHtml5',
            //     exportOptions: {
            //         columns: ':visible'
            //     }
            // },
           
            
            
            
        ],
        exportOptions: {
            columns: ':visible'
        }
    });
    table.buttons().container()
    .appendTo( '#example .col-sm-6:eq(0)' );
});