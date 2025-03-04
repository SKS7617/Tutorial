function showSection(sectionId) {
  // Hide all sections
  document.querySelectorAll('.section').forEach(section => {
      section.style.display = 'none';
  });

  // Show the selected section
  document.getElementById(sectionId).style.display = 'block';
}

// Show the home section by default when the page loads
document.addEventListener('DOMContentLoaded', () => {
  showSection('home');
});