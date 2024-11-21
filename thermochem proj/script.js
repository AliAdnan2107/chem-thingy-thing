document.addEventListener('DOMContentLoaded', () => {
    const introScreen = document.getElementById('intro-screen');
    const mainContent = document.getElementById('main-content');

    // Add click event to transition to main content
    introScreen.addEventListener('click', () => {
        introScreen.style.opacity = '0';
        introScreen.style.transition = 'opacity 1s ease-out';

        // Wait for transition to finish before hiding intro
        setTimeout(() => {
            introScreen.style.display = 'none';
            mainContent.style.display = 'block';
            document.body.style.overflow = 'auto'; // Re-enable scrolling
        }, 1000);
    });

    // Removed button click event listeners and section toggle functionality
});
