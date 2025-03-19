import React from 'react';
import Navbar from './components/Navbar';
import CoachList from './components/CoachList';
import CustomerList from './components/CustomerList';
import CRoute from './components/Routes';
const App = () => {
  return (
    <div>
      
      <CRoute />
      {/* <CoachList />
      <CustomerList /> */}
    </div>
  );
};

export default App;
