
import TaskItem from "./TaskItem";


function TaskList({ tasks, onEdit, onDelete }) {

    return (

        <div className="task-list">

            <h2>My Tasks</h2>


            {tasks.length === 0 ? (

                <p className="no-tasks">
                    No tasks to display.
                </p>

            ) : (

                tasks.map((task) => (

                    <TaskItem
                        key={task.id}
                        task={task}
                        onEdit={onEdit}
                        onDelete={onDelete}
                    />

                ))

            )}

        </div>

    );
}


export default TaskList;

