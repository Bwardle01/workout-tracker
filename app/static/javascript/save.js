// When save button is clicked, all data is saved to the user profile.

// Data includes:
// workout name, weight, reps, exercise name.

async function saveWorkout() {
  

  const date = document.getElementById("dateInput").value;
  const workoutName = document.getElementById("workoutNameInput").value;
  const exerciseName = document.getElementById("exerciseInput").value;
  const weight = document.getElementById("weightInput").value;
  const reps = document.getElementById("repsInput").value;

  const data = {
    workoutName: workoutName,
    date: date,
    exerciseName: exerciseName,
    weight: weight,
    reps: reps,
  };

  if (data) {
    const response = await fetch("/api/save", {
      method: "POST",
      body: JSON.stringify({
        data
      }),
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (response.ok) {
      document.location.reload('/');
    } else{
      alert(response.statustext);
    }
   
  }
}

document.getElementById("saveButton").onclick = saveWorkout;