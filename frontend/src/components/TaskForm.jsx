
import { useEffect, useState } from "react";


function TaskForm({ onAddTask, editingTask }) {

    const [task, setTask] = useState("");


    // ==========================================
    // LOAD TASK WHEN EDIT IS CLICKED
    // ==========================================

    useEffect(() => {

        if (editingTask) {

            setTask(editingTask.task);

        } else {

            setTask("");

        }

    }, [editingTask]);


    // ==========================================
    // SUBMIT
    // ==========================================

    const handleSubmit = (e) => {

        e.preventDefault();


        if (task.trim() === "") {

            alert("Please enter a task");

            return;
        }


        onAddTask(task.trim());

        setTask("");

    };


    return (

        <form
            className="task-form"
            onSubmit={handleSubmit}
        >

            <input
                type="text"
                placeholder="Enter your task..."
                value={task}
                onChange={(e) => setTask(e.target.value)}
            />


            <button type="submit">

                {editingTask
                    ? "Update Task"
                    : "Add Task"
                }

            </button>

        </form>

    );
}


export default TaskForm;

