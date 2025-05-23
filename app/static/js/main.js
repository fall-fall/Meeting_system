// Function to confirm deletion
function confirmDelete(message) {
    return confirm(message || '确定要删除此项目吗？');
}

// Function to add agenda item form with animation
function addAgendaItemForm() {
    const agendaItems = document.getElementById('agenda-items');
    const itemCount = agendaItems.children.length;

    const newItem = document.createElement('div');
    newItem.className = 'agenda-item card mb-3';
    newItem.style.opacity = '0';
    newItem.style.transform = 'translateY(20px)';
    newItem.style.transition = 'opacity 0.3s ease, transform 0.3s ease';

    newItem.innerHTML = `
        <div class="card-body">
            <div class="row">
                <div class="col-md-6">
                    <div class="form-group">
                        <label for="start_time_${itemCount}">开始时间</label>
                        <input type="text" id="start_time_${itemCount}" name="start_time" class="form-control" placeholder="例如: 09:00" required>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="form-group">
                        <label for="end_time_${itemCount}">结束时间</label>
                        <input type="text" id="end_time_${itemCount}" name="end_time" class="form-control" placeholder="例如: 10:00" required>
                    </div>
                </div>
            </div>
            <div class="form-group">
                <label for="title_${itemCount}">标题</label>
                <input type="text" id="title_${itemCount}" name="title" class="form-control" placeholder="议程项目标题" required>
            </div>
            <div class="form-group">
                <label for="speaker_${itemCount}">演讲者</label>
                <input type="text" id="speaker_${itemCount}" name="speaker" class="form-control" placeholder="演讲者姓名" required>
            </div>
            <button type="button" class="btn btn-danger" onclick="removeAgendaItem(this)">删除</button>
        </div>
    `;

    agendaItems.appendChild(newItem);

    // Trigger animation after a small delay
    setTimeout(() => {
        newItem.style.opacity = '1';
        newItem.style.transform = 'translateY(0)';
    }, 10);
}

// Function to remove agenda item with animation
function removeAgendaItem(button) {
    const item = button.closest('.agenda-item');

    // Add fade out animation
    item.style.opacity = '0';
    item.style.transform = 'translateY(20px)';

    // Remove the element after animation completes
    setTimeout(() => {
        item.remove();
    }, 300);
}

// Add animation to cards
function animateCards() {
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'opacity 0.3s ease, transform 0.3s ease';

        // Stagger the animations
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 100 * index);
    });
}

// Document ready function
document.addEventListener('DOMContentLoaded', function() {
    // Add event listeners for delete confirmations
    const deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirmDelete(this.getAttribute('data-confirm-message'))) {
                e.preventDefault();
            }
        });
    });

    // Add event listener for add agenda item button
    const addAgendaButton = document.getElementById('add-agenda-item');
    if (addAgendaButton) {
        addAgendaButton.addEventListener('click', addAgendaItemForm);
    }

    // Animate cards on page load
    animateCards();

    // Add form input animations
    const formInputs = document.querySelectorAll('input, textarea, select');
    formInputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentElement.classList.add('input-focused');
        });

        input.addEventListener('blur', function() {
            this.parentElement.classList.remove('input-focused');
        });
    });
});
