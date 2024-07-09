import React, { useState } from 'react';
import Register from './components/Register';
import Login from './components/Login';
import InviteForm from './components/InviteForm';
import InviteList from './components/InviteList';
import './App.css';

function App() {
    const [token, setToken] = useState('');

    return (
        <div className="App">
            <h1>Electronic Invite App</h1>
            {!token ? (
                <>
                    <Register />
                    <Login setToken={setToken} />
                </>
            ) : (
                <>
                    <InviteForm token={token} />
                    <InviteList token={token} />
                </>
            )}
        </div>
    );
}

export default App;
