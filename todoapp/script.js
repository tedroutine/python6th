const todoInput = document.getElementById("todo-input")
const todoResult = document.getElementById("todo-result")

function addTask() {
    if(todoInput.value === '') {
        alert("write something!")
    }
    else {
        // 요소를 생성해주고
        let li = document.createElement("li");
        // 그 요소에 어떤 HTML 값을 넣을 것인지 정하고
        li.innerHTML = todoInput.value;
        // 그 값을 어디에 넣을건지 정해기
        todoResult.appendChild(li);

        let span = document.createElement("span");
        // innerHTNL 은 unicode로 받는다.
        span.innerHTML = "\u00d7";
        li.appendChild(span);
    }
    todoInput.value = "";
    saveData();
}

todoResult.addEventListener("click", function(e){
    if(e.target.tagName === "LI"){
        e.target.classList.toggle("checked"); // checked 로 켰다가 껐다가
        saveData();
    }
    else if(e.target.tagName === "SPAN"){
        e.target.parentElement.remove();
        saveData();
    }
}, false);

function saveData() {
    localStorage.setItem("data", todoResult.innerHTML);
}

function showTask(){
    todoResult.innerHTML = localStorage.getItem("data")
}
showTask();