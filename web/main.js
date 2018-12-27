const picker = document.querySelector("color-picker");

picker.addEventListener("color-change", () => {
  const { state } = picker;
  //TODO set post to udp server
});

function saveColor() {
    currentColor = picker.state.hex;
    colors = LSgetColors();

    if (!~colors.indexOf(currentColor)) {
        colors.unshift(currentColor);
        LSsaveColors(colors);
        updateSavedColors();
    } else {
        console.warn('color already saved');
    }
}

function LSgetColors() {
    return JSON.parse(localStorage.getItem('colors')) || [];
}

function LSsaveColors(colors) {
    if (!colors || !colors.length) {
        localStorage.removeItem('colors');
    } else {
        localStorage.setItem('colors', JSON.stringify(colors));
    }
}

function updateSavedColors() {
    const element = document.getElementById('colorsHolder'),
        colors = LSgetColors();
    let innerHTML = '';

    colors.forEach(c => {
        innerHTML += '<div class="outerField" data-color="' + c + '"><div class="removeButton" onclick="javascript:removeColor(this)">X</div><div class="colorField" style="background-color: ' + c + ';" onclick="javascript:setColor(this)"><span>#' + c + '</span></div></div>';
    });

    element.innerHTML = innerHTML;
}

updateSavedColors();

function removeColor(btn) {
    const c = btn.parentElement.getAttribute('data-color'),
        colors = LSgetColors()
        idx = colors.indexOf(c);
    
    if (!~idx) {
        console.warn('Warning: Color ' + c + ' not found.');
        return;
    }

    colors.splice(idx, 1);
    LSsaveColors(colors);

    updateSavedColors();
}

function setColor(btn) {
    const c = btn.parentElement.getAttribute('data-color');

    if (!c) {
        console.warn('Warning: missing color attribute!');
    }

    picker.hexInput.value = c;
    picker.hexInput.dispatchEvent(new Event('input', {
        'bubbles': true,
        'cancelable': true
    }));
}