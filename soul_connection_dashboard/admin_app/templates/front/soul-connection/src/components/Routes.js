
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
//import Navbar from './Navbar';
import Dashboard from './Dashbord';
import CoachList from './CoachList';
import CustomerList from './CustomerList';

const CRoute = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Dashboard />} />
                <Route path="/coaches" element={<CoachList />} />
                <Route path="/customers" element={<CustomerList />} />
            </Routes>
        </Router>
    );
};

export default CRoute;
