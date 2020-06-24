import React, { useEffect } from 'react';
import axios from 'axios';
import './ManagerDashboard.css';
import { render } from 'react-dom';

function handleSubmit(event) {
  const text = document.querySelector('#client-name-input').value
  //axios.post()
}

function getClients() {
    // axios.get('/clients/manager_dashboard/clients/').then(response => {
    //     if (response.status === 201) {
    //         return response.data;
    //     }
    //     else {
    //         return 400;
    //     }
    // });
}

function ManagerDashboard() {
    // useEffect(() => {
    //     let clients = getClients();
    //     const displayClients = clients.map(client => (
    //         <div>
    //             <h3>client.name</h3>
    //         </div>
    //     ));
    // });

    const clientList = [
        { id: 1, name: 'MetisGenetics' },
        { id: 2, name: 'SurveySaurus' },
    ];

    return (
        <div className="ManagerDashboard">
            <div>
                <label htmlFor='client-name-input'>What is the name of your new client?</label>
                <input id='client-name-input' type='text' />
                <button onClick={handleSubmit}>Submit</button>
            </div>

            <div>
                <h3 id='client-name'></h3>
            </div>
            <br />
            {clientList.map(client => (
                <div>
                    <h3>{client.name}</h3>
                </div>
            ))}
        </div>
    );
}

export default ManagerDashboard;
