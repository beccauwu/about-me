const accountspy = document.getElementById('accountspy');
const business = document.getElementById('business');
const snake = document.getElementById('snake');
const aBtn = document.getElementById('accountspyBtn');
const bBtn = document.getElementById('businessBtn');
const sBtn = document.getElementById('snakeBtn');
const projectsPanel = document.getElementById('projectsPanel');
const accountspyPanel = document.getElementById('accountspyPanel');
const snakePanel = document.getElementById('snakePanel');
const portfolioPanel = document.getElementById('portfolioPanel');

const itmArray = [accountspy, snake, business]
const panelArray = [accountspyPanel, snakePanel, portfolioPanel]
for (let i = 0; i < itmArray.length; i++) {
    const element = itmArray[i];
    const panel = panelArray[i];
    const panId = panel.id;
    console.log(panId)
    $(element).on('click', () => {
        if (!projectsPanel.classList.contains('show')) {
            projectsPanel.setAttribute('class', 'show')
        }
        if (!panel.classList.contains('show')) {
            panel.setAttribute('class', 'show');
        }
        location.href = `#${panId}`
    })
}
