import React, { useEffect, useState } from 'react';
import Navbar from './Navbar';
import './CustomerList.css';

const CustomerList = () => {
    const [customers, setCustomers] = useState([]);

    useEffect(() => {
        fetch('http://localhost:4000/api/customers')
            .then(response => response.json())
            .then(data => setCustomers(data))
            .catch(error => console.error('Error:', error));
    }, []);

    const getInitials = name => name.split(' ').map(part => part[0]).join('').toUpperCase();

    return (
        <div className="container">
            <Navbar />
            <h1>Customers List</h1>
            <p>You have a total of {customers.length} customers.</p>

            {/* conteneur pour les bouton */}
            <div className="action-buttons">
                <div className="bulk-actions">
                    <button>Bulk Action</button>
                    <button>Apply</button>
                </div>

                <div className="right-actions">
                    <button>Export</button>
                    <button className="add-button">+</button>
                </div>
            </div>

            <table className="customer-table">
                <thead>
                    <tr>
                        <th>Customer</th>
                        <th>Email</th>
                        <th>Phone</th>
                        <th>Payment Methods</th>
                        <th>Coach Assigned</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {customers.map((customer, index) => (
                        <tr key={index}>
                            <td>
                                <div className="checkbox-customer">
                                    <input type="checkbox" />
                                    <div className="customer-name">
                                        <div className={`initial-circle bg-color${(index % 5) + 1}`}>
                                            {getInitials(customer.name)}
                                        </div>
                                        {customer.name}
                                    </div>
                                </div>
                            </td>
                            <td>{customer.email}</td>
                            <td>{customer.phone}</td>
                            <td className="payment-methods">{customer.paymentMethods}</td>
                            <td>{customer.coach}</td>
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

export default CustomerList;
