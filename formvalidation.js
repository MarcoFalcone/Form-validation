//form validation//
  $('#form').on('submit', function(e) {

    $.ajax({
      data : {
        name : $('#name').val(),
        email : $('#email').val(),
        message : $('#message').val()
    },
      type : 'POST',
      url : '/submit_form'
  })

    .done(function(data) {

      $('#name of the class with the message').show(); //or .fadeIn()//

  });

  e.preventDefault();
});
