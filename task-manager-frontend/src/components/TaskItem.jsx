import api from '../api/axios';

function TaskItem({ task, onUpdate }) {
  const handleToggle = async () => {
    try {
      await api.patch(`tasks/${task.id}/`, { completed: !task.completed });
      onUpdate();
    } catch (err) {
      console.error(err);
    }
  };

  const handleDelete = async () => {
    try {
      await api.delete(`tasks/${task.id}/`);
      onUpdate();
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: 10, padding: '6px 0', borderBottom: '1px solid #f0f0f0' }}>
      <input
        type="checkbox"
        checked={task.completed}
        onChange={handleToggle}
      />
      <span style={{
        flex: 1,
        fontSize: 14,
        textDecoration: task.completed ? 'line-through' : 'none',
        color: task.completed ? '#999' : '#000'
      }}>
        {task.title}
      </span>
      <button onClick={handleDelete} style={{ color: 'red', border: 'none', background: 'none', cursor: 'pointer', fontSize: 14 }}>
        Delete
      </button>
    </div>
  );
}

export default TaskItem;