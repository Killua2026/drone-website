const mediaInput = document.getElementById('mediaInput');
const galleryGrid = document.getElementById('galleryGrid');

// 1. Function to handle Deleting Items
function deleteItem(button) {
    // Find the parent div (.gallery-item) of the button that was clicked
    const itemToRemove = button.parentElement;
    
    // Remove it from the grid
    itemToRemove.remove();
}

// 2. Event Listener for Uploads
mediaInput.addEventListener('change', function(event) {
    const file = event.target.files[0];

    if (file) {
        const reader = new FileReader();

        reader.onload = function(e) {
            // Create the wrapper div
            const div = document.createElement('div');
            div.classList.add('gallery-item');

            // Create the Delete Button
            const btn = document.createElement('button');
            btn.classList.add('delete-btn');
            btn.innerText = 'X';
            btn.onclick = function() { deleteItem(btn); }; // Add delete logic
            
            // Create the Media Element (Image or Video)
            let mediaElement;

            if (file.type.startsWith('image/')) {
                // If it's an image
                mediaElement = document.createElement('img');
                mediaElement.src = e.target.result;
            } else if (file.type.startsWith('video/')) {
                // If it's a video
                mediaElement = document.createElement('video');
                mediaElement.src = e.target.result;
                mediaElement.controls = true; // Add play/pause buttons
            }

            // Assemble the parts
            if (mediaElement) {
                div.appendChild(btn);          // Add button to div
                div.appendChild(mediaElement); // Add image/video to div
                galleryGrid.appendChild(div);  // Add div to the page
            }
        }

        reader.readAsDataURL(file);
    }
});