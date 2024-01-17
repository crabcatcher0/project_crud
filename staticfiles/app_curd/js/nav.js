// Function to show dropdown menu
function showDropdown(element) {
    element.querySelector('.dropdown-toggle').classList.add('show');
    element.querySelector('.dropdown-menu').classList.add('show');
}

// Function to hide dropdown menu
function hideDropdown(element) {
    element.querySelector('.dropdown-toggle').classList.remove('show');
    element.querySelector('.dropdown-menu').classList.remove('show');
}

//For animated Notice

$(document).ready(function () {
    // Fetch latest three notice titles using AJAX
    $.ajax({
        url: '{% url "get_latest_notice_data" %}',
        type: 'GET',
        dataType: 'json',
        headers: {'X-CSRFToken': '{{ csrf_token }}'},
        success: function (data) {
            // Limit the data to the latest three items
            var latestNotices = data.slice(0, 3);

            // Set the text of the element with id 'movingNotices'
            $('#movingNotices').text(latestNotices.map(item => item.title).join(' || '));
        },
        error: function (error) {
            console.log('Error fetching notice data:', error);
        }
    });
});
//pausing on hover
$(document).ready(function () {
    // Hover event for the 'movingNotices' element
    var movingNotices = $('#movingNotices');
    movingNotices.hover(
        function () {
            movingNotices.addClass('paused');
        },
        function () {
            movingNotices.removeClass('paused');
        }
    );
});

// Vanilla JavaScript event listener when DOM content is loaded
document.addEventListener('DOMContentLoaded', function () {
    // Get the 'phone' button element
    var phoneButton = document.querySelector('.phone');

    // Add event listener to show Bootstrap modal when 'phone' button is clicked
    phoneButton.addEventListener('click', function () {
        var phoneModal = new bootstrap.Modal(document.getElementById('phoneModal'));
        phoneModal.show();
    });
});
