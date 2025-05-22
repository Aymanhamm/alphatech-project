// Main JavaScript file for Alphatech Solutions

// Form submission handling
document.addEventListener('DOMContentLoaded', function() {
    // Handle form submissions with file uploads
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const fileInputs = this.querySelectorAll('input[type="file"]');
            if (fileInputs.length > 0) {
                e.preventDefault();
                const formData = new FormData(this);
                
                // Show loading state
                const submitButton = this.querySelector('button[type="submit"]');
                const originalText = submitButton.innerHTML;
                submitButton.innerHTML = '<i class="bi bi-hourglass"></i> En cours...';
                submitButton.disabled = true;
                
                // Send AJAX request
                fetch(this.action, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest'
                    }
                })
                .then(response => response.json())
                .then(data => {
                    // Handle success
                    if (data.success) {
                        window.location.href = data.redirect_url;
                    } else {
                        // Handle errors
                        const errorList = document.createElement('div');
                        errorList.className = 'alert alert-danger';
                        errorList.innerHTML = data.errors.join('<br>');
                        this.insertBefore(errorList, this.firstChild);
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('Une erreur est survenue lors de la soumission du formulaire.');
                })
                .finally(() => {
                    // Reset button
                    submitButton.innerHTML = originalText;
                    submitButton.disabled = false;
                });
            }
        });
    });

    // Handle date input calendar
    const dateInputs = document.querySelectorAll('input[type="date"]');
    dateInputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.showPicker();
        });
    });

    // Handle file upload preview
    const fileInputs = document.querySelectorAll('input[type="file"][data-preview]');
    fileInputs.forEach(input => {
        input.addEventListener('change', function() {
            const preview = document.querySelector(this.dataset.preview);
            if (preview) {
                const file = this.files[0];
                if (file) {
                    const reader = new FileReader();
                    reader.onload = function(e) {
                        preview.src = e.target.result;
                    };
                    reader.readAsDataURL(file);
                }
            }
        });
    });

    // Handle tab navigation
    const tabLinks = document.querySelectorAll('.nav-link[data-toggle="tab"]');
    tabLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = this.getAttribute('href');
            const tabContent = document.querySelector('.tab-content');
            
            // Remove active classes from current tabs
            document.querySelector('.nav-link.active').classList.remove('active');
            document.querySelector('.tab-pane.active').classList.remove('active');
            
            // Add active classes to new tabs
            this.classList.add('active');
            tabContent.querySelector(target).classList.add('active');
        });
    });

    // Handle dynamic form fields
    const addFieldButtons = document.querySelectorAll('.add-field');
    addFieldButtons.forEach(button => {
        button.addEventListener('click', function() {
            const template = this.dataset.template;
            const container = this.closest('.form-group').querySelector('.fields-container');
            const newField = document.createElement('div');
            newField.innerHTML = template;
            container.appendChild(newField);
        });
    });

    // Handle delete confirmation
    const deleteButtons = document.querySelectorAll('.btn-danger[data-confirm]');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm(this.dataset.confirm)) {
                e.preventDefault();
            }
        });
    });
});
