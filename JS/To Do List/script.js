New = document.getElementById("New");
taskList = document.getElementById("taskList");

// Task Counter

let taskcounter = 1;

New.onclick = function() {

    // Afficher un formulaire afin de formuler la tâche
    
    // Creer un template
    taskList.innerHTML += `
        <div class="task">
            <input type="checkbox">
            <label for="taskname">Template</label>
            <p id="delete-task">X</p>
        </div>
    `;
};

// fonction pour supprimer la tache sur click X

// fonction rename

// clear list ( demande une confirmation )