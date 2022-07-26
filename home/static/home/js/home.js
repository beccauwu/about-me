const accountspy = document.getElementById('accountspy');
const business = document.getElementById('business');
const snake = document.getElementById('snake');
const aBtn = document.getElementById('accountspyBtn');
const bBtn = document.getElementById('businessBtn');
const sBtn = document.getElementById('snakeBtn');
const projectsPanel = document.getElementById('projectsPanel');
const projectThree = document.getElementById('projectThree');
const projectTwo = document.getElementById('projectTwo');
const projectOne = document.getElementById('projectOne');

const itmArray = [accountspy, snake, business]
const panelArray = [projectThree, projectTwo, projectOne]
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
