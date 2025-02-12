const textColors = ["#1477e8", "#23808d", "#3a618f", "#a5db31", "#22818d", "#87d5a4", "#9ed946", "#7ad04e", "#50c46b", "#27ae60"];
function getRandomTextColorFromArray() {
    return textColors[Math.floor(Math.random() * textColors.length)];
}
function setRandomTextColors() {
    const elements = document.querySelectorAll('.randomColorBox');
    elements.forEach((element) => {
        const randomTextColor = getRandomTextColorFromArray();
        element.style.color = randomTextColor;
    });
}
window.onload = setRandomTextColors;