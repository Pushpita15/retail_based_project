$(document).ready(function() {
    $('#pincodeForm').submit(function(event) {
        event.preventDefault();
        var pincode = $('#pincodeInput').val();
        var fileInput = $('#jsonFileInput')[0].files[0];
        
  
        var formData = new FormData();
        formData.append('file', fileInput);
        
        
        $.ajax({
            url: '/upload_file', 
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
            
                $.ajax({
                    url: '/pincode_serviceability',
                    type: 'POST',
                    data: { pincode: pincode }, 
                    success: function(response) {
                        if (response.message === 'Service not available in this area') {
                            $('#result').html('<p>Service not available in this area</p>');
                        } else {
                            var vendors = response.vendors.join(', ');
                            $('#result').html('<p>Service available in this area. Vendors: ' + vendors + '</p>');
                        }
                    },
                    error: function(xhr, status, error) {
                        console.error('Error:', error);
                    }
                });
            },
            error: function(xhr, status, error) {
                console.error('Error:', error);
            }
        });
    });
});

