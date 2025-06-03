import React from 'react';
import CarForm from '../components/CarForm';
import CarList from '../components/CarList';

const AdminDashboard = () => {
  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold">Admin Dashboard</h1>
      <CarForm />
      <CarList />
    </div>
  );
};

export default AdminDashboard;
