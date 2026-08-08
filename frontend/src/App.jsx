
import { useState } from "react";

import "./App.css";

import TaskForm from "./components/TaskForm";
import TaskList from "./components/TaskList";

import {
    getTasks,
    createTask,
    updateTask,
    deleteTask
} from "./services/taskService";


function App() {

    // Tasks currently displayed on the screen
    const [tasks, setTasks] = useState([]);

    // Task currently being edited
    const [editingTask, setEditingTask] = useState(null);


    // ==========================================
    // DISPLAY TASKS
    // ==========================================

    const handleDisplayTasks = async () => {

        try {

            const data = await getTasks();

            setTasks(data);

        } catch (error) {

            console.error(
                "Error fetching tasks:",
                error
            );

            alert("Unable to load tasks");

        }
    };


    // ==========================================
    // ADD / UPDATE TASK
    // ==========================================

    const handleAddTask = async (taskText) => {

        try {

            // ----------------------------------
            // UPDATE EXISTING TASK
            // ----------------------------------

            if (editingTask) {

                await updateTask(
                    editingTask.id,
                    taskText
                );

                alert("Task updated successfully");

                setEditingTask(null);


                // Refresh the displayed list
                // because the user was already
                // viewing tasks.

                await handleDisplayTasks();

            }


            // ----------------------------------
            // CREATE NEW TASK
            // ----------------------------------

            else {

                await createTask(taskText);

                alert("Task added successfully");


                // IMPORTANT:
                //
                // We DON'T call handleDisplayTasks()
                // here.
                //
                // Therefore the newly added task
                // will NOT automatically appear.
            }

        } catch (error) {

            console.error(
                "Error saving task:",
                error
            );

            alert("Unable to save task");

        }
    };


    // ==========================================
    // EDIT TASK
    // ==========================================

    const handleEdit = (task) => {

        setEditingTask(task);

    };


    // ==========================================
    // DELETE TASK
    // ==========================================

    const handleDelete = async (id) => {

        try {

            await deleteTask(id);

            alert("Task deleted successfully");


            // Remove deleted task
            // from currently displayed list

            setTasks((currentTasks) =>
                currentTasks.filter(
                    (task) => task.id !== id
                )
            );

        } catch (error) {

            console.error(
                "Error deleting task:",
                error
            );

            alert("Unable to delete task");

        }
    };


    return (

        <div className="app">

            <h1>Note App</h1>


            {/* ==================================
                ADD / UPDATE FORM
            ================================== */}

            <TaskForm
                onAddTask={handleAddTask}
                editingTask={editingTask}
            />


            {/* ==================================
                DISPLAY TASKS BUTTON
            ================================== */}

            <button
                type="button"
                className="display-button"
                onClick={handleDisplayTasks}
            >
                Display Tasks
            </button>


            {/* ==================================
                TASK LIST
            ================================== */}

            <TaskList
                tasks={tasks}
                onEdit={handleEdit}
                onDelete={handleDelete}
            />

        </div>

    );
}


export default App;

