import React, { Component } from 'react';
import axios from "axios";

class Prediction extends Component {
    constructor() {
        super()
        this.state = {
            class: "1",
            gender: "0",
            prediction: "",
            accuracy: "",
        }
        this.handleChange = this.handleChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
    }


    handleSubmit = event => {
        event.preventDefault();
        // const user = {
        //     bottomText: this.state.bottomText
        // }
        console.log(this.state.class)
        console.log(this.state.gender)
        axios.get("make-prediction", {
            params: {
                sex: parseInt(this.state.gender),
                pclass: parseInt(this.state.class)
            }
        })
            .then(res => {
                console.log(res)
                this.setState({
                    prediction: res.data.prediction
                });
                this.setState({
                    accuracy: res.data.accuracy
                })
            })
    }

    handleChange = event => {
        const { name, value } = event.target;
        this.setState({
            [name]: value
        });
    }

    render() {
        return (
            <div>
                <form onSubmit={this.handleSubmit}>
                    <label>
                        Gender:
                        <input type="radio" value="0" name="gender" checked={this.state.gender === "0"} onChange={this.handleChange} /> Male
                        <input type="radio" value="1" name="gender" checked={this.state.gender === "1"} onChange={this.handleChange} /> Female
                    </label>
                    <br />
                    <label>
                        Class:
                        <select name="class" value={this.state.value} onChange={this.handleChange}>
                            <option value="1">First class</option>
                            <option value="2">Second class</option>
                            <option value="3">Third class</option>
                        </select>
                    </label>
                    <br />
                    <button type="submit"> Predict </button>
                </form>

                <br />
                <div >
                    {this.state.prediction === "" ? "" :
                        <h2 className="top">Prediction: {this.state.prediction}</h2>}
                    {this.state.accuracy === "" ? "" :
                        <h3 className="top">Accuracy: {this.state.accuracy}</h3>}
                </div>
            </div>
        );
    }
}
export default Prediction;