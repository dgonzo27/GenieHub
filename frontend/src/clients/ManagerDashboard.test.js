import React from 'react';
import ReactDOM from 'react-dom';
import ManagerDashboard from './ManagerDashboard';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<ManagerDashboard />, div);
  ReactDOM.unmountComponentAtNode(div);
});
