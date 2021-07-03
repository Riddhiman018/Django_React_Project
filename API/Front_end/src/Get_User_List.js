import React from 'react';
import axios from 'axios';

export default class UserList extends React.Component{
    state = {
        user: [],
    };

    componentDidMount()
    {
        axios.get("http://127.0.0.1:8000/?format=json").then(res =>{console.log(res);
        this.setState({user: res.data});
    });
    }
    render(){
        return(
            <ul>
                {this.state.user.map(user =><li>{user.username}</li>)}
            </ul>
        )
    }
}