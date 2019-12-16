import React, {Fragment} from "react";
import apiHelper from '../apiHelper';
import { connect } from "react-redux";

class ResultSummery extends React.Component {
    constructor() {
        super();

       
    }

    

    // componentDidUpdate(prevProps, prevState){
        
    // }

    componentDidMount() {
        apiHelper.getResultSummery().then((response) => {
            this.props.dispatch({ type: 'GETRESULT', response })
        }, () => {

        });
    }


    render() { 
        return (
            <Fragment>
                <div className="text-center">
                    <p>You have taken the exam already, Here is the score</p>
                    <h4>Find yourself where you positioned</h4>
                </div>
                
                <hr></hr>
                <table className="table">
                    <thead>
                        <tr>
                        <th># Rank</th>
                        <th>Username</th>
                        <th>Total Marks</th>
                        <th>Elapsed</th>
                        
                        </tr>
                    </thead>
                    <tbody>
                        {this.props.summeries.map((summery, index) => (
                            <tr key={index}>
                                <th>{index + 1}</th>
                                <td>{summery.user.username}</td>
                                <td>{summery.total_marks}</td>
                                <td>{summery.total_elapsed_second} Seconds</td>
                                
                            </tr>
                        ))}
                        
                       
                    </tbody>
                </table>
            </Fragment>
        );
    }
}




const mapStateToProps = (state) => ({ summeries: state.summery });

export default connect(mapStateToProps)(ResultSummery);