
import axios from "axios";


// FastAPI backend URL
const API_URL = "http://127.0.0.1:8000/tasks";


// ==========================================
// GET ALL TASKS
// ==========================================

export const getTasks = async () => {

    const response = await axios.get(`${API_URL}/`);

    return response.data;
};


// ==========================================
// CREATE TASK
// ==========================================

export const createTask = async (task) => {

    const response = await axios.post(
        `${API_URL}/`,
        {
            task: task
        }
    );

    return response.data;
};


// ==========================================
// UPDATE TASK
// ==========================================

export const updateTask = async (id, task) => {

    const response = await axios.put(
        `${API_URL}/${id}`,
        {
            task: task
        }
    );

    return response.data;
};


// ==========================================
// DELETE TASK
// ==========================================

export const deleteTask = async (id) => {

    const response = await axios.delete(
        `${API_URL}/${id}`
    );

    return response.data;
};

