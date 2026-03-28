import { useState } from 'react';
import api from '../api/axios';
import TaskItem from './TaskItem';

function GoalCard({ goal, onUpdate }) {
  const [tasks, setTasks] = useState([]);
  const [showTasks, setShowTasks] = useState(false);
  const [taskTitle, setTaskTitle] = useState('');

  const fetchTasks = async () => {
    try {
      const res = await api.get(`tasks/?goal=${goal.id}`);
      setTasks(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  const toggleTasks = () => {
    if (!showTasks) fetchTasks();
    setShowTasks(!showTasks);
  };

  const handleAddTask = async (e) => {
    e.preventDefault();
    try {
      await api.post('tasks/', { title: taskTitle, goal: goal.id });
      setTaskTitle('');
      fetchTasks();
    } catch (err) {
      console.error(err);
    }
  };

  const handleDeleteGoal = async () => {
    try {
      await api.delete(`goals/${goal.id}/`);
      onUpdate();
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div style={{ border: '1px solid #ddd', borderRadius: 8, padding: 16 }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <div>
          <h3 style={{ margin: 0 }}>{goal.title}</h3>
          {goal.description && (
            <p style={{ margin: '4px 0 0', color: '#666', fontSize: 14 }}>{goal.description}</p>
          )}
        </div>
        <div style={{ display: 'flex', gap: 8 }}>
          <button onClick={toggleTasks} style={{ padding: '6px 12px' }}>
            {showTasks ? 'Hide tasks' : 'Show tasks'}
          </button>
          <button onClick={handleDeleteGoal} style={{ padding: '6px 12px', color: 'red' }}>
            Delete
          </button>
        </div>
      </div>

      {showTasks && (
        <div style={{ marginTop: 16 }}>
          {tasks.map((task) => (
            <TaskItem key={task.id} task={task} onUpdate={fetchTasks} />
          ))}
          <form onSubmit={handleAddTask} style={{ display: 'flex', gap: 8, marginTop: 12 }}>
            <input
              placeholder="Task title"
              value={taskTitle}
              onChange={(e) => setTaskTitle(e.target.value)}
              style={{ flex: 1, padding: 8 }}
            />
            <button type="submit" style={{ padding: '8px 16px' }}>
              + Add
            </button>
          </form>
        </div>
      )}
    </div>
  );
}

export default GoalCard;