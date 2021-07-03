import React from 'react';
import axios from 'axios';

export default class Form extends React.Component{
    state = {
        user_id : '',
        username: '',
        user_DOB: '',
        user_pwd: ''
    }

    changeHandler = event =>{
        this.setState({[event.target.name]:event.target.value})
    }
    SubmitHandler = event =>{
        event.preventDefault();
        axios.post("http://127.0.0.1:8000/",this.state).then(
            response => {console.log(response)}
        )
    }
    render(){
            const {user_id,username,user_DOB,user_pwd} = this.state
        return(
            <form onSubmit = {this.SubmitHandler}>
                <input type = "text" name = "user_id" value = {user_id} onChange = {this.changeHandler}/>
                <p></p>
                <input type = "text" name = "username" value = {username} onChange = {this.changeHandler}/>
                <p></p>
                <input type = "date" name = "user_DOB" value = {user_DOB} onChange = {this.changeHandler}/>
                <p></p>
                <input type = "password" name = "user_pwd" value = {user_pwd} onChange = {this.changeHandler}/>
                <p></p>
                <button type = "submit">SUBMIT</button>
            </form>
        )
    }
};