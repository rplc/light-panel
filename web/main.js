const picker = document.querySelector("color-picker");

picker.addEventListener("color-change", () => {
  const { state } = picker;
  console.log(state); // => object containing the current rgb, hsb and hex values
  //TODO set post to udp server
});

//set color:
function setColor() {
    picker.hexInput.value = '876B9C';
    picker.hexInput.dispatchEvent(new Event('input', {
        'bubbles': true,
        'cancelable': true
    }));
}

function saveColor() {
    currentColor = picker.state.hex;
    colors = LSgetColors();

    if (!~colors.indexOf(currentColor)) {
        colors.unshift(currentColor);
        LSsaveColors(colors);
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
        innerHTML += '<div class="outerField"><div class="colorField" style="background-color: ' + c + ';"><span>#' + c + '</span></div></div>';
    });

    element.innerHTML = innerHTML;
}

updateSavedColors();