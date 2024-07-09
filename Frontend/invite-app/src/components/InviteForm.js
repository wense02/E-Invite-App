import React, { useState } from 'react';
import axios from 'axios';
import '../App.css';

const InviteForm = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const inviteData = { name, email };
    try {
      await axios.post('http://localhost:8000/api/invites/', inviteData, {
        headers: {
          'Content-Type': 'application/json',
        },
      });
      setSuccess('Invite sent successfully!');
      setName('');
      setEmail('');
    } catch (error) {
      setError('Error sending invite. Please try again.');
    }
  };

  return (
    <div className="container">
      <h2>Send an Invite</h2>
      <form className="form" onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <button type="submit">Send Invite</button>
      </form>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {success && <p style={{ color: 'green' }}>{success}</p>}
    </div>
  );
};

export default InviteForm;
