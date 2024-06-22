$(document).ready(function() {
  let simplemde = new SimpleMDE({ element: $("#memoryText")[0] });
  
  // Fetch and display cards
  function fetchCards(page = 1) {
    $.ajax({
      url: 'https://t9kqble7me.execute-api.ap-south-1.amazonaws.com/dev/memory/',
      method: 'GET',
      success: function(response) {
        const cards = response;
        const cardContainer = $('#cardContainer');
        cardContainer.empty();
        
        // Pagination logic
        const cardsPerPage = 4;
        const totalPages = Math.ceil(cards.length / cardsPerPage);
        const start = (page - 1) * cardsPerPage;
        const end = start + cardsPerPage;
        const paginatedCards = cards.slice(start, end);
        
        // Render cards
        paginatedCards.forEach(cardData => {
          const card = `
            <div class="card mb-4">
              <div class="card-header">
                <span>${cardData.created_by}</span>
                <span class="float-right">${new Date(cardData.memory_date).toLocaleDateString()}</span>
              </div>
              <div class="card-body row">
                <div class="col-md-4">
                  <img src="${cardData.file_url}" class="img-fluid" alt="Memory Image">
                </div>
                <div class="col-md-8">
                  <p>${marked(cardData.memory)}</p>
                </div>
              </div>
            </div>
          `;
          cardContainer.append(card);
        });

        // Render pagination
        const pagination = $('#pagination');
        pagination.empty();
        for (let i = 1; i <= totalPages; i++) {
          pagination.append(`
            <li class="page-item ${i === page ? 'active' : ''}">
              <a class="page-link" href="#">${i}</a>
            </li>
          `);
        }
        
        // Pagination click event
        $('.page-link').click(function(e) {
          e.preventDefault();
          const pageNum = parseInt($(this).text());
          fetchCards(pageNum);
        });
      },
      error: function(error) {
        console.error('Error fetching cards', error);
      }
    });
  }

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
        $('#removeImageButton').show();
      };
      reader.readAsDataURL(file);
    }
  });

  // Handle remove image
  $('#removeImageButton').click(function() {
    $('#fileUpload').val('');
    $('#filePreview').hide().attr('src', '');
    $(this).hide();
  });

  // Handle form submission
  $('#newCardForm').submit(function(event) {
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
        for (var pair of formData.entries()) {
        console.log(pair[0]+ ', ' + pair[1], simplemde.value());
    }


      $.ajax({
        url: 'https://hmago5j35khdhox4w5gzc74jee0wlyfi.lambda-url.ap-south-1.on.aws/memory/add_memory',

        method: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response) {
          $('#drawer').removeClass('open');
          fetchCards();
        },
        error: function(error) {
          console.error('Error submitting form', error);
        }
      });
    
  });

  // Handle login modal opening
  $('#loginButton').click(function() {
    $('#loginModal').modal('show');
  });

  // Handle login form submission
  $('#loginForm').submit(function(event) {
    event.preventDefault();
    const email = $('#loginUsername').val();
    const password = $('#loginPassword').val();

    $.ajax({
      url: 'https://t9kqble7me.execute-api.ap-south-1.amazonaws.com/dev/user/login',

      method: 'POST',
      data: JSON.stringify({ email, password }),
      contentType: 'application/json',
      success: function(response) {
        const { token, user } = response;
        localStorage.setItem('token', token);
        localStorage.setItem('user', JSON.stringify(email));
        $('#loginModal').modal('hide');
        updateAuthUI();
      },
      error: function(error) {
        console.error('Error logging in', error);
        alert("Invalid authentication")
      }
    });
  });

  // Handle register link click
  $('#registerLink').click(function(e) {
    e.preventDefault();
    $('#loginModal').modal('hide');
    $('#registerModal').modal('show');
  });

  // Handle register form submission
  $('#registerForm').submit(function(event) {
    event.preventDefault();
    const email = $('#registerUsername').val();
    const password = $('#registerPassword').val();

    $.ajax({

      url: 'https://t9kqble7me.execute-api.ap-south-1.amazonaws.com/dev/register',

      method: 'POST',
      data: JSON.stringify({ email, password }),
      contentType: 'application/json',
      success: function(response) {
        $('#registerModal').modal('hide');
        $('#loginModal').modal('show');
      },
      error: function(error) {
        console.error('Error registering', error);
        alert("Error in registration")
      }
    });
  });

  // Update UI based on authentication state
  function updateAuthUI() {
    const user = JSON.parse(localStorage.getItem('user'));
    if (user) {
      $('#loginNavItem').hide();
      $('#logoutNavItem').show();
      $('#usernameDisplay').text(user);
    } else {
      $('#loginNavItem').show();
      $('#logoutNavItem').hide();
    }
  }

  // Handle logout
  $('#logoutButton').click(function() {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    updateAuthUI();
  });

  updateAuthUI();
});
