$(document).ready(function() {
  // Initialize SimpleMDE Markdown editor
  var simplemde = new SimpleMDE({ element: document.getElementById("memoryText") });

  // Function to fetch and display cards
  function fetchCards() {
    $.ajax({
      url: 'http://localhost:8000/memory/',
      method: 'GET',
      success: function(data) {
        const cardContainer = $('#cardContainer');
        cardContainer.empty();
        data.forEach(memory => {
          const card = `
            <div class="card mb-3">
              <div class="card-header d-flex justify-content-between">
                <span>${memory.created_by}</span>
                <span>${memory.memory_date}</span>
              </div>
              <div class="card-body">
                <div class="row">
                  <div class="col-md-4">
                    <img src="${memory.file_url}" class="img-fluid" alt="Image">
                  </div>
                  <div class="col-md-8">
                    <div class="card-text">${(memory.memory)}</div>
                  </div>
                </div>
              </div>
            </div>
          `;
          cardContainer.append(card);
        });
      },
      error: function(error) {
        console.error('Error fetching data', error);
      }
    });
  }

  // Fetch cards on page load
  fetchCards();

  // Handle drawer opening
  $('#addNewCardButton').click(function() {
    $('#drawer').addClass('open');
  });

  // Handle drawer closing
  $('#closeDrawerButton').click(function() {
    $('#drawer').removeClass('open');
  });

  // Handle file upload and preview
  $('#fileUpload').change(function(event) {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function(e) {
        $('#filePreview').attr('src', e.target.result).show();
      }
      reader.readAsDataURL(file);
    } else {
      $('#filePreview').hide();
    }
  });

  // Handle form submission
  $('#newCardForm').submit(function(event) {
    console.log(event)
    event.preventDefault();
    const memoryDate = $('#memoryDate').val();
    const memoryText = simplemde.value();
    const fileUpload = $('#fileUpload')[0].files[0];
    const formData = new FormData();
    formData.append('memory_date', memoryDate);
    formData.append('memory', memoryText);
    if (fileUpload) {
    formData.append('memory_file', fileUpload);
    }
    console.log(formData.keys, formData.values)
    $.ajax({
      url: 'http://localhost:8000/memory/add_memory',
      method: 'POST',
      data: formData,
      processData: false,
      contentType: false,
      success: function() {
        $('#drawer').removeClass('open');
        fetchCards();
      },
      error: function(error) {
        console.error('Error submitting form', error);
      }
    });
  });
});
