import React from 'react';
import { NavLink } from 'react-router-dom';
// import { BackButton } from '../../components';
import './style.css'

export const Header = () => {
    return(
        <nav>

            <NavLink to='/dashboard'>Home</NavLink>
            {/* <BackButton /> */}
        </nav>
    )
};
