import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../App.css'; // Import the CSS file

const InviteList = () => {
  const [invites, setInvites] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchInvites = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/invites/', {
          headers: {
            'Content-Type': 'application/json',
          },
        });
        setInvites(response.data);
      } catch (error) {
        setError('Error fetching invites. Please try again.');
      }
    };

    fetchInvites();
  }, []);

  const handleDelete = async (id) => {
    try {
      await axios.delete(`http://localhost:8000/api/invites/${id}/`, {
        headers: {
          'Content-Type': 'application/json',
        },
      });
      setInvites(invites.filter((invite) => invite.id !== id));
    } catch (error) {
      setError('Error deleting invite. Please try again.');
    }
  };

  return (
    <div className="container">
      <h2>Invite List</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <div className="invite-list">
        {invites.map((invite) => (
          <div key={invite.id} className="invite-item">
            <div className="details">
              <p>Name: {invite.name}</p>
              <p>Email: {invite.email}</p>
            </div>
            <div className="actions">
              <button onClick={() => handleDelete(invite.id)}>Delete</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default InviteList;
