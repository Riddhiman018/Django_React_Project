import React from 'react';
import axios from 'axios';

export default class validationPrac extends React.Component{
    state = {
        user_id: '',
        user_pwd: ''
    }
    SubmitHandler = event =>{
        event.preventDefault();
        axios.post("http://127.0.0.1:8000/verify",this.state).then(
            response => {console.log(response)}
        )
    }
    changeHandler = event =>{
        this.setState({[event.target.name]:event.target.value})
    }
    render(){
        const {user_id,user_pwd} = this.state
        return(
            <form onSubmit = {this.SubmitHandler}>
                <label>ID</label>
                <input type = "text" name = "user_id" onChange = {this.changeHandler} value = {user_id}></input>
                <p></p><p></p>
                <label>Pwd</label>
                <input type = "password" name = "user_pwd" onChange = {this.changeHandler} value = {user_pwd}></input>
                <p></p>
                <button type = "submit">Submit</button>
            </form>
        )
    }
};