import React, {Fragment} from "react";
import { connect } from "react-redux";
import apiHelper from '../apiHelper';

class Home extends React.Component {

    componentWillUnmount(){
        // Clear prevous state when retrun to another route
        
    }


    componentDidMount(){
        // get user list on reload the page
         apiHelper.getQuestionList().then((response) => {
           // handle success
           this.props.dispatch({ type: 'GET', response }) 
         }, () => {
            // handle error
            
         });
     }

     next = (id) => {
        var q = document.getElementById('haha');
        console.log(q, id);
		q.style.display = "none"
	}

    render() {
        return (
            <Fragment>
                {this.props.question.map((user, index) => (
                    <div style={{display: "block"}} id='haha' key={index}>
                        
                        <h1>{ user.title }</h1>

                        {user.choices.map((choice, index) => (
                            <div key={index}>
                                
                                <input
                                id={choice.id}
                                type="radio">
                                </input>
                                <label htmlFor={choice.id}>{choice.choice_text}</label>
                            </div>
                            
                        ))}
                        
                        <button onClick={this.next}>Submit</button>
                    </div>
                ))}
            </Fragment>
        );
    }
}

const mapStateToProps = (state) => ({ question: state.question });

export default connect(mapStateToProps)(Home);