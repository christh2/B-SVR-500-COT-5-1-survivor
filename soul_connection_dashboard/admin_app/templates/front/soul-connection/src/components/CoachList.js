
import React, { useEffect, useState } from 'react';
import Navbar from './Navbar';
import './CoachList.css';

const CoachList = () => {
    const [coaches, setCoaches] = useState([]);

    useEffect(() => {
        fetch('http://localhost:4000/api/coaches')
            .then(response => response.json())
            .then(data => setCoaches(data))
            .catch(error => console.error('Error:', error));
    }, []);

    const getInitials = name => name.split(' ').map(part => part[0]).join('').toUpperCase();

    return (
        <div className="container">
            <Navbar />
            <h1>Coaches List</h1>
            <p>You have total {coaches.length} coaches.</p>
            
            <div className="top-controls">
                <div className="bulk-actions">
                    <select>
                        <option value="bulk-action">Bulk Action</option>
                        <option value="delete">Delete</option>
                        <option value="edit">Edit</option>
                    </select>
                    <button>Apply</button>
                </div>
                <div className="right-buttons">
                    <button>Export</button>
                    <button className="icon-button">+</button>
                </div>
            </div>
            
            <table className="coach-table">
                <thead>
                    <tr>
                        <th>Coach</th>
                        <th>Email</th>
                        <th>Phone</th>
                        <th>Number of customers</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {coaches.map((coach, index) => (
                        <tr key={index}>
                            <td>
                                <div className="checkbox-coach">
                                    <input type="checkbox" />
                                    <div className="coach-name">
                                        <div className={`initial-circle bg-color${(index % 5) + 1}`}>
                                            {getInitials(coach.name)}
                                        </div>
                                        {coach.name}
                                    </div>
                                </div>
                            </td>
                            <td>{coach.email}</td>
                            <td>{coach.phone}</td>
                            <td>{coach.customers}</td>
                            <td>
                                <button className="action-button"><span className="dots">...</span></button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default CoachList;
