// When a user clicks add exercise, a new exercise field will be populated along with weight and reps.
// When a new exercise is populated a + button is also added to add a new set.

// When user clicks + button a new set of weight and reps are populated.
// when button click a new set of LI is populated of input fields.


// this funciton works but the style on the containers arent working. Need to figure out how to target the container for the syle.
function addExercise() { 
  const exerciseList = document.getElementById("exercise-list");
  const cardExercise = document.querySelector(".card-exercise")

  const setElement = document.querySelector(".add-set-button");
 
  const newCardExercise = cardExercise.cloneNode(true);
  const newSetElement = setElement.cloneNode(true);


  exerciseList.appendChild(newCardExercise);
  exerciseList.appendChild(newSetElement);
};


document.getElementById('addExercise').onclick = addExercise;




// function addExercise() {
// 	const exerciseList = document.getElementById("exercise-list");
// 	const exerciseTemplate = document.querySelector(".card-exercise");
//   const addSetButton = document.querySelector(".card-addset")

// 	const exerciseClone = exerciseTemplate.cloneNode(true);
//   const addSetButtonClone = addSetButton.cloneNode(true);
  
//   const exerciseInput = exerciseClone.querySelector(".exerciseInput");
//   const weightInput = exerciseClone.querySelector(".weightInput");
//   const repsInput = exerciseClone.querySelector(".repsInput");

//   exerciseInput.value = "";
//   weightInput.value = "";
//   repsInput.value = "";


//   exerciseList.appendChild(addSetButtonClone);
// 	exerciseList.appendChild(exerciseClone);
// }







