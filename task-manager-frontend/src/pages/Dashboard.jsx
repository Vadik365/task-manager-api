import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../api/axios';
import GoalCard from '../components/GoalCard';

function Dashboard() {
  const [goals, setGoals] = useState([]);
  const [categories, setCategories] = useState([]);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [categoryId, setCategoryId] = useState('');
  const navigate = useNavigate();

  const fetchGoals = async () => {
    try {
      const res = await api.get('goals/');
      const data = res.data;
      setGoals(Array.isArray(data) ? data : data.results ?? []);
    } catch (err) {
      console.error(err);
    }
  };

  const fetchCategories = async () => {
    try {
      const res = await api.get('categories/');
      const data = res.data;
      setCategories(Array.isArray(data) ? data : data.results ?? []);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    fetchGoals();
    fetchCategories();
  }, []);

  const handleAddGoal = async (e) => {
    e.preventDefault();
    if (!categoryId) return alert('Please select a category');
    try {
      await api.post('goals/', { title, description, category: categoryId });
      setTitle('');
      setDescription('');
      setCategoryId('');
      fetchGoals();
    } catch (err) {
      console.error(err);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');
    navigate('/login');
  };

  return (
    <div style={{ maxWidth: 800, margin: '40px auto', padding: 24 }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 24 }}>
        <h1>My Goals</h1>
        <button onClick={handleLogout} style={{ padding: '8px 16px' }}>
          Exit
        </button>
      </div>

      <form onSubmit={handleAddGoal} style={{ marginBottom: 32, display: 'flex', gap: 8 }}>
        <input
          placeholder="Goal title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          style={{ flex: 1, padding: 8 }}
        />
        <input
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          style={{ flex: 1, padding: 8 }}
        />
        <select
          value={categoryId}
          onChange={(e) => setCategoryId(e.target.value)}
          style={{ padding: 8 }}
        >
          <option value="">Select category</option>
          {categories.map((cat) => (
            <option key={cat.id} value={cat.id}>{cat.name}</option>
          ))}
        </select>
        <button type="submit" style={{ padding: '8px 16px' }}>
          + Add
        </button>
      </form>

      <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
        {goals.map((goal) => (
          <GoalCard key={goal.id} goal={goal} onUpdate={fetchGoals} />
        ))}
      </div>
    </div>
  );
}

export default Dashboard;