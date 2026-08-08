
function TaskItem({ task, onEdit, onDelete }) {

    return (

        <div className="task-item">

            <span className="task-name">
                {task.task}
            </span>


            <div className="task-buttons">

                <button
                    type="button"
                    onClick={() => onEdit(task)}
                >
                    Edit
                </button>


                <button
                    type="button"
                    onClick={() => onDelete(task.id)}
                >
                    Delete
                </button>

            </div>

        </div>

    );
}


export default TaskItem;

