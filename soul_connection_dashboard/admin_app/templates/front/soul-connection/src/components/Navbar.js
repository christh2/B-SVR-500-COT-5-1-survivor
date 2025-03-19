// import React from 'react';
// import { Link } from 'react-router-dom';
// import './Navbar.css';

// const Navbar = () => {
//   return (
//     <nav className="navbar">
//       <div className="logo">Soul Connection</div>
//       <div>
//         <Link to="/">Dashboard</Link>
//         <Link to="/coaches">Coaches</Link>
//         <Link to="/customers">Customers</Link>
//         <Link to="/tips">Tips</Link>
//         <Link to="/events">Events</Link>
//       </div>
//       <div className="right-icons">
//         <div className="icon">🌍</div>
//         <div className="icon">👤</div>
//       </div>
//     </nav>
//   );
// };

// export default Navbar;


import React from 'react';
import { NavLink } from 'react-router-dom';
import './Navbar.css';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="logo">Soul Connection</div>
      <div>
        <NavLink
          exact
          to="/"
          activeClassName="active-link"
        >
          Dashboard
        </NavLink>

        <NavLink
          to="/coaches"
          activeClassName="active-link"
        >
          Coaches
        </NavLink>
        <NavLink
          to="/customers"
          activeClassName="active-link"
        >
          Customers
        </NavLink>
        <NavLink
          to="/tips"
          activeClassName="active-link"
        >
          Tips
        </NavLink>
        <NavLink
          to="/events"
          activeClassName="active-link"
        >
          Events
        </NavLink>
      </div>
      <div className="right-icons">
        <div className="icon">🌍</div>
        <div className="icon">👤</div>
      </div>
    </nav>
  );
};

export default Navbar;
