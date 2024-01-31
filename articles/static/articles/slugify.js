document.addEventListener('DOMContentLoaded', function() {
    const titleInput = document.querySelector('input[name=title]');
    const slugInput = document.querySelector('input[name=slug]');

    const slugify = (val) => {
        return val.toString().toLowerCase().trim()
            .replace(/&/g, '-and-')
            .replace(/[\s\W-]+/g, '-');
    };

    if (titleInput && slugInput) {
        titleInput.addEventListener('input', function() {
            slugInput.value = slugify(titleInput.value);
        });
    }
});
