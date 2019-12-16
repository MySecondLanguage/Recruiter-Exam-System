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
        console.log(this.props.summeries)   
        return (
            <Fragment>
                <table className="table">
                    <thead>
                        <tr>
                        <th scope="col">Rank</th>
                        <th scope="col">Username</th>
                        
                        </tr>
                    </thead>
                    <tbody>
                        {this.props.summeries.map((summery, index) => (
                            <tr key={index}>
                                <th>{index}</th>
                                <td>{summery.user.username}</td>
                                
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