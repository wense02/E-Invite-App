import React from 'react';
import { Navigate } from 'react-router-dom';

const PrivateRoute = ({ element }) => {
  const isAuthenticated = !!localStorage.getItem('access_token'); // Check if the user is authenticated

  return isAuthenticated ? element : <Navigate to="/login" />;
};

export default PrivateRoute;
