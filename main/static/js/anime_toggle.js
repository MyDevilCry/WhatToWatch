document.addEventListener('DOMContentLoaded',function() {
    const typeSelect = document.querySelector('#id_anime_type');

    const inlineGroups = document.querySelectorAll('.inline-group');
    let seasonsGroup = null;

    inlineGroups.forEach(group => {
        const heading = group.querySelector('h2');
        if (heading && heading.textContent.toLowerCase().includes('сезони')) {
        seasonsGroup=group;
        }
    });

    function toggleSeasons() {
        if (!typeSelect || !seasonsGroup) return;

        if (typeSelect.value == 'Feature') {
            seasonsGroup.style.display = 'none';
        } else {
        seasonsGroup.style.display = 'block';
        }

    }

    if (typeSelect) {
        toggleSeasons();
        typeSelect.addEventListener('change',toggleSeasons);
    }
});