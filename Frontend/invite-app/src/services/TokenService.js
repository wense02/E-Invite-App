// src/services/tokenService.js
import axios from 'axios';

const refreshToken = async () => {
  try {
    const refresh = localStorage.getItem('refresh_token');
    const response = await axios.post('http://localhost:8000/api/token/refresh/', {
      refresh,
    });
    localStorage.setItem('access_token', response.data.access);
    axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.access}`;
    return response.data.access;
  } catch (error) {
    console.error('Error refreshing token:', error);
    // Handle token refresh failure (e.g., redirect to login)
  }
};

export default refreshToken;
