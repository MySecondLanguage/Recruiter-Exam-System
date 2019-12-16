var initialState = {
    question: {},
    summery: [],
  };
  
  var Reducer = (state = initialState, action) => {
    switch (action.type) {
      
      case 'GET':
        return {
          ...state,
          question: action.response.data,
        }
      
      case 'GETRESULT':
        return {
          ...state,
          summery: [...action.response.data],
        }

      default:
        return state;
    }
  };
  
  
  export default Reducer;